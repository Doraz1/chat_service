# Chat service for learning scale-up apps
This project is a simple chat service designed to help me understand the secrets of back-end programming users understand how to scale up applications.
Follow the steps below to set up and run the project on your local machine

## Setup Instructions

### 1. Create a `config.py` File  
Create a `config.py` file in the project directory with your custom configurations. Include parameters such as:  
- **MongoDB connection string**  
- **API keys (if any)**  
- **Other required settings**

### 2. Configure MongoDB  
Ensure your MongoDB instance is set up correctly and accessible. Make sure your IP address is whitelisted to allow the API to connect to the database.

### 3. Run the Server  
Start the server to handle backend requests by running:  
```bash
python server.py
```
Run the server to accept and process all requests in back end.

### 4. Run the Client-Side Code
Execute the client-side code to interact with the server. This may include operations such as
- register user
- get all users 
- send a message between users
- get the message history between two users

### 5. Data Storage
All data is stored in the MongoDB database specified in the config.py file.
