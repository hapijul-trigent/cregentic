# **Cregentic: AI-Powered Content Creation Platform**

Cregentic is an AI-driven article generation platform that streamlines the entire content creation process. It utilizes specialized agents to automate tasks such as researching trending topics, drafting content, reviewing, and preparing articles for publication. Whether you're a content creator, editor, or publisher, Cregentic provides a collaborative workflow powered by artificial intelligence.

## **Table of Contents**
1. [Overview](#overview)
2. [Key Features](#key-features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configuration](#configuration)
6. [Agents](#agents)
7. [Tasks](#tasks)
8. [Testing](#testing)
---

## **Overview**

Cregentic is designed to support a wide range of content creation activities by leveraging AI agents. Each agent focuses on a specific task in the content pipeline, ensuring seamless collaboration and efficiency. From ideation and drafting to revision and publishing, Cregentic can either fully automate the process or assist human creators by speeding up their workflows.

## **Key Features**

- **AI Agents** for various stages of content creation: research, drafting, editing, and publishing.
- **Task Scheduler** to automate content workflows.
- **Feedback Loop** enabling iterative improvements.
- **Configurable Agents**: Customize agent behaviors with YAML configuration files.
- **Support for Drafts and Final Publishing**: Easily save, modify, and publish content with minimal intervention.

---

## **Installation**

Follow these steps to set up Cregentic locally:

### 1. **Clone the Repository**
   ```bash
   git clone https://github.com/hapijul-trigent/cregentic.git
   cd cregentic
   ```

### 2. **Install Dependencies**
   Ensure Python is installed, then install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Set Environment Variables**
   Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   ```
   Modify `.env` with the necessary credentials and settings.

### 4. **Optional: Set Up Ollama Locally**
   To run locally with Ollama, execute:
   ```bash
   ./setup_ollama_locally.sh
   ```

---

## **Usage**

You can run the application in different modes, depending on your requirements:

1. **Run the Main Application**:
   ```bash
   python app.py
   ```

2. **Alternative Version**:
   ```bash
   python app_v2.py
   ```

3. **Run with Story Drafting**:
   ```bash
   python main_with_storydrafter.py
   ```

4. **Resetting Data**:
   If you need to reset draft or article data:
   ```bash
   python reset_data.py
   ```

---

## **Configuration**

Configuration settings allow you to fine-tune agent behavior and system settings. Configuration files are located in the `/config` directory.

- **Global Configuration**: `config.yaml`
- **Agent-Specific Configurations**: Found in `/config/agent_configs/`, these files allow you to customize each agent’s parameters (e.g., `editor_agent.yaml`, `writer_agent.yaml`).

---

## **Agents**

Cregentic is powered by a set of modular agents, each designed to handle a specific content creation task:

### 1. **Research Agent**
   - **Path**: `agents/research_agent.py`
   - **Function**: Gathers relevant research material, including trending topics.

### 2. **Outline Agent**
   - **Path**: `agents/outline_agent.py`
   - **Function**: Constructs structured outlines for articles based on research data.

### 3. **Writer Agent**
   - **Path**: `agents/writer_agent.py`
   - **Function**: Converts outlines into intial draft articles.

### 4. **Editor Agent**
   - **Path**: `agents/editor_agent.py`
   - **Function**: Reviews drafts and suggests revisions for improvements.

### 5. **Story Drafter Agent**
   - **Path**: `agents/story_drafter_agent.py`
   - **Function**: Finalizes drafts into polished articles, ready for publishing.

### 6. **Publisher Agent**
   - **Path**: `agents/publisher_agent.py`
   - **Function**: Formats and prepares articles for publication.

---

## **Tasks**

Cregentic’s agents are driven by task scripts that define specific actions:

- **Draft Writing**: `tasks/draft_writing_task.py`
- **Outline Drafting**: `tasks/outline_drafting_task.py`
- **Editor Reviewing**: `tasks/editor_reviewing_task.py`
- **Story Drafting**: `tasks/story_drafting_task.py`
- **Research Tasks**: `tasks/research_tasks.py`
- **Publishing Task**: `tasks/publishing_task.py`

---

## **Testing**

Unit tests are included to ensure the core functionality of the agents and tasks. To run the tests, use:

```bash
pytest tests/
```

Tests cover various components, including agent management, editor functions, and task execution.

---

## **Contributing**

We welcome contributions to Cregentic! Follow these steps:

1. Fork the repository and clone it locally.
2. Create a new branch for your feature or bug fix.
3. Push your changes and submit a pull request with a detailed explanation of your work.

For major changes, please open an issue to discuss what you would like to contribute.

---

## **License**

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.

---

This README serves as a comprehensive guide for users and contributors. For additional documentation, refer to the in-line comments within each Python script and the configuration files.

