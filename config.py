import os
from datetime import timedelta

# MongoDB Configuration
MONGODB_URI = "mongodb+srv://razdor1:SdlBqADq57BgFJoz@miniproj-cluster.mr2v1.mongodb.net/?retryWrites=true&w=majority&appName=miniproj-cluster"
DATABASE_NAME = "ChatService"

# Database path
CWD = os.path.join(os.getcwd(), "chat_service")
DATABASE_PATH = os.path.join(CWD, "chat_service.db")

# Log file paths
LOG_DIR = os.path.join(CWD, "logs")
USER_LOG_PATH = os.path.join(LOG_DIR, "user_activity.log")
ERROR_LOG_PATH = os.path.join(LOG_DIR, "error.log")

# Message retrieval settings
DEFAULT_MESSAGE_HISTORY_DAYS = 1  # Retrieve messages from the last day by default
DEFAULT_HISTORY_TIMEDELTA = timedelta(days=DEFAULT_MESSAGE_HISTORY_DAYS)
MAX_MESSAGES_QUERIED = 10

# Application settings
BASE_URL = "http://127.0.0.1:5000"  # Adjust to match the deployment URL of your backend
APP_NAME = "Chat Service with MongoDB"
DEBUG_MODE = True  # Set to False in production
PORT = 5000  # Flask server port
HOST = "127.0.0.1"  # Localhost for development; adjust for production

# Other parameters
MAX_MESSAGE_LENGTH = 1000  # Maximum characters allowed in a message
