# Cregentic

**Cregentic** is an agent-based platform designed to automate various aspects of content generation, such as research, outlining, storytelling, writing, editing, and publishing. It leverages multiple agents that collaborate to complete complex tasks related to article creation.

## Features

- **Research Agent**: Gathers information and trending topics for the content.
- **Outline Agent**: Creates detailed outlines for structured content.
- **Storytelling Agent**: Improves the narrative style and flow of the content.
- **Writer Agent**: Generates coherent drafts of the content.
- **Editor Agent**: Edits and refines the content based on feedback.
- **Publishing Agent**: Prepares the content for publication.

## Project Structure

- **agents/**: Contains the main agent scripts for each specific task (editor, outline, storytelling, etc.).
- **config/**: Houses configuration files for each agent, as well as general settings.
- **core/**: Core management scripts for agents and task scheduling.
- **data/**: Stores various data used by the agents, including drafts, feedback, and trending topics.
- **tools/**: Contains the tools files for agents.
- **tasks**: Containe Tasks assigned to agents.
- **tests/**: Unit tests for various agents and core functionality.
- **utils/**: Utility scripts for file I/O, data validation, and other common operations.

## Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hapijul-trigent/cregentic.git
cd cregentic
```

### 2. Install Dependencies

Ensure you have the necessary dependencies installed by running the following commands. You might need `pip` or a similar package manager:

```bash
pip install -r requirements.txt
```

### 3. Set Up Ollama Locally
For running the agents that require the Ollama model, follow these steps:

1. Run the provided setup script:
   ```bash
   bash setup_ollama_locally.sh     # Terminal 1
   bash run_ollama_locally.sh       # Terminal 2
   ```

   This will install the Ollama CLI and download the `llama3.1:8b` model.
   
2. Ollama will be accessible at:
   ```
   http://localhost:11434/api/generate
   ```

### 4. Running the Agents

- **Run all agents**:  
  To execute all agents, use the following command:

  ```bash
  python run_all_agents.py
  ```

- **Run a specific agent**:  
  If you want to run a specific agent, such as the writer, use:

  ```bash
  python run_single_agent.py writer_agent
  ```

### 5. Reset Data

To reset all the data (drafts, outlines, feedback), you can run the following script:

```bash
python reset_data.py
```

## Testing

Run the unit tests for each agent and core functionalities using:

```bash
pytest tests/
```
