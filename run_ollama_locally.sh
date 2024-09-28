#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y


echo "Pulling llama3.1:8b model..."
ollama pull llama3.1:8b

echo "Connect llama3.1:8b at localhost: http://localhost:11434/api/generate"
