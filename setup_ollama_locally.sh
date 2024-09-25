#!/bin/bash

echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y



echo "Installing Ollama CLI..."
curl -fsSL https://ollama.com/install.sh | sh


echo "Running Ollama with LLaMA-3 model..."
ollama serve

echo "Connect at localhost: http://localhost:11434/api/generate"