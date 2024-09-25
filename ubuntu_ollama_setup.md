# Setting Up Ollama Locally

This guide will help you install and set up Ollama on your local machine using the provided script.

## Prerequisites
- A Unix-based operating system (Linux or macOS)
- Internet connection

## Steps to Set Up Ollama

1. **Clone the Repository**  
   Open a terminal and clone the repository:

   ```bash
   git clone https://github.com/hapijul-trigent/cregentic.git
   cd cregentic
   ```

2. **Run the Setup Script**  
   Execute the following command to install Ollama and set up the model:

   ```bash
   bash setup_ollama_locally.sh
   ```

   This script will:
   - Update system packages.
   - Install the Ollama CLI.
   - Pull the `llama3.1:8b` model.
   - Run Ollama, which can be accessed at: `http://localhost:11434/api/generate`.

3. **Access Ollama**  
   Once the setup is complete, you can access the Ollama API at:

   ```
   http://localhost:11434/api/generate
   ```

   The Ollama service will be running with the `llama3.1:8b` model.

---