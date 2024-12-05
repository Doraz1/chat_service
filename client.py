import requests
from datetime import datetime, timedelta
from config import BASE_URL

# Configuration
def register_user(username):
    """Register a new user."""
    response = requests.post(f"{BASE_URL}/register", json={"username": username})
    if response.status_code == 200:
        print(f"User '{username}' registered successfully.")
    else:
        print(f"Failed to register user '{username}': {response.json().get('error')}")


def send_message(sender, receiver, content):
    """Send a message from sender to receiver."""
    response = requests.post(f"{BASE_URL}/send", json={
        "sender": sender,
        "receiver": receiver,
        "content": content
    })
    if response.status_code == 200:
        print(f"Message from '{sender}' to '{receiver}' sent successfully.")
    else:
        print(f"Failed to send message: {response.json().get('error')}")


def get_all_users():
    response = requests.get(f"{BASE_URL}/get_users", params={})
    
    if response.status_code == 200:
        try:
            users = response.json()
            print("-----------")
            print("Users in the database are:")
            for user in users:
                print(f"  - {user}")
            print("-----------")
        except requests.exceptions.JSONDecodeError:
            print("Error: Received a non-JSON response from the server.")
    
    else:
        # Handle cases where the server returns an error but no JSON
        try:
            error_message = response.json().get("error", "Unknown error")
        except requests.exceptions.JSONDecodeError:
            error_message = "Server returned an error with no details."
        print(f"Failed to retrieve user list: {error_message}")


def get_chat_history(sender, receiver):
    response = requests.get(f"{BASE_URL}/history", params={"sender": sender, "receiver": receiver})
    if response.status_code == 200:
        messages = response.json()
        print(f"-----------")
        print(f"Chat history between '{sender}' and '{receiver}':")
        for msg in messages:
            msg_ts = msg['timestamp']
            parsed_datetime = datetime.strptime(msg_ts, "%a, %d %b %Y %H:%M:%S %Z")
            print(f"  [{parsed_datetime}] {msg['sender']}: {msg['content']}")
        print(f"-----------")
        
    else:
        print(f"Failed to retrieve chat history: {response.json().get('error')}")


# Usage Example
if __name__ == "__main__":
    user = "Dor"
    user_2 = "Grace"
    
    create_users = False
    if create_users:
        register_user(user)
        register_user(user_2)

    get_all_users()

    message_content = "Hello Grace! What event are you editing?"
    message_content = "A Hena party for a couple called Or and Dror :)"
    # imageData = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAA7AAAAOwBeShxvQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAABSdEVYdENvcHlyaWdodABDQzAgUHVibGljIERvbWFpbiBEZWRpY2F0aW9uIGh0dHA6Ly9jcmVhdGl2ZWNvbW1vbnMub3JnL3B1YmxpY2RvbWFpbi96ZXJvLzEuMC/G4735AAABeklEQVRYhe2XMU7DMBiFv1RiYGJg4AJIXVqpdGBhQZwBiYkDcQJugASn6FKJpRsdKlWiQ4dKLEwgVWIC8RgSVQpN89yQDlTqm5zY'
    # send_message("Grace", "Dor", message_content)

   # Retrieve chat history
    get_chat_history("Dor", "Grace")