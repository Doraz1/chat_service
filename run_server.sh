#!/bin/bash

# Path to the Python virtual environment
ENV_PATH="/Users/dorraz/Documents/autodidact/miniprojects/env"

# Path to the Python script to run
SCRIPT_PATH="/Users/dorraz/Documents/autodidact/miniprojects/chat_service/server.py"

# Activate the Python virtual environment
source "$ENV_PATH/bin/activate"

# Check if activation was successful
if [ $? -ne 0 ]; then
  echo "Failed to activate the Python environment at $ENV_PATH."
  exit 1
fi

# Run the Python script
python "$SCRIPT_PATH"

# Check if the script ran successfully
if [ $? -ne 0 ]; then
  echo "Failed to run the Python script at $SCRIPT_PATH."
  exit 1
fi

# Deactivate the Python environment
deactivate

echo "Script executed successfully."
