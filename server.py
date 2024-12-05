from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime, timedelta
from config import MONGODB_URI, DATABASE_NAME, DEBUG_MODE, HOST, PORT, MAX_MESSAGE_LENGTH, DEFAULT_MESSAGE_HISTORY_DAYS, MAX_MESSAGES_QUERIED

app = Flask(__name__)

# MongoDB client and database initialization
client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
users_collection = db["users"]
messages_collection = db["messages"]


# Helper: Validate username
def user_exists(username):
    return users_collection.find_one({"username": username}) is not None

# Route: Register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if user_exists(username):
        return jsonify({"error": "Username already exists"}), 400

    users_collection.insert_one({"username": username})
    return jsonify({"message": f"User '{username}' registered successfully"})



# Route: Send a message
@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    sender = data.get("sender")
    receiver = data.get("receiver")
    content = data.get("content")

    if not sender or not receiver or not content:
        return jsonify({"error": "Sender, receiver, and content are required"}), 400

    if len(content) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": "Message exceeds maximum length"}), 400

    if not user_exists(sender) or not user_exists(receiver):
        return jsonify({"error": "Sender or receiver does not exist"}), 400

    message = {
        "sender": sender,
        "receiver": receiver,
        "content": content,
        "timestamp": datetime.utcnow()
    }
    messages_collection.insert_one(message)
    return jsonify({"message": "Message sent successfully"})



# Route: Retrieve chat history
@app.route('/history', methods=['GET'])
def get_chat_history():
    sender = request.args.get("sender")
    receiver = request.args.get("receiver")
    since = datetime.now() - timedelta(days=DEFAULT_MESSAGE_HISTORY_DAYS)

    if not sender or not receiver:
        return jsonify({"error": "Sender and receiver are required"}), 400

    if not user_exists(sender) or not user_exists(receiver):
        return jsonify({"error": "Sender or receiver does not exist"}), 400

    # Query messages between sender and receiver
    messages = list(messages_collection.find({
        "$or": [
            {"sender": sender, "receiver": receiver},
            {"sender": receiver, "receiver": sender}
        ],
        "timestamp": {"$gte": since}
    }).sort("timestamp", 1))

    for message in messages:
        message["_id"] = str(message["_id"])  # Convert ObjectId to string for JSON serialization

    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE, host=HOST, port=PORT)
