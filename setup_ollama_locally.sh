#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

echo "Installing Ollama CLI..."
curl -fsSL https://ollama.com/install.sh | sh

echo "Connect at localhost: http://localhost:11434/api/generate"
echo "Running Ollama with llama3.1:8b model..."
ollama serve