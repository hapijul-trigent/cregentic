#!/bin/bash

echo "Pulling llama3.1:8b model..."
ollama pull llama3.1:8b


echo "Running Ollama with LLaMA-3 model..."
ollama run llama3.

echo "Connect at localhost: http://localhost:11434/api/generate"