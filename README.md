# chat service for learning scale-up apps
the first thing to do is createa  config.py with custom parameters for the project - these parameters are personal and should not be shared, and area must for the server to run
go to mongoDB and ensure the ip is configured properly - otherwise the api may prevent access for your server
Then# Chat Service for Learning Scale-Up Apps

This project is a simple chat service designed to help users understand how to scale up applications. Follow the steps below to set up and run the project on your local machine.

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
, run the server to accept and process all requests in back end
then, run the client-side code. code may include requests like get all users, send a message and get the message history between two users\
all code is updated in the mongoDB defined in the config.py file

### 4. Run the Client-Side Code
Execute the client-side code to interact with the server. This may include operations such as:

Get all users
Send messages
Receive messages

### 5. Data Storage
All data is stored in the MongoDB database specified in the config.py file.
