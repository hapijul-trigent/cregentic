import os
from crewai import Agent, Task, Crew, Process

# Setup your environment for the local Llama2 model
os.environ["OPENAI_API_KEY"] = "DUMMY_API"

agent = Agent(
    role='AI Expert',
    goal='Generative AI Trainer',
    backstory="You are experience intraininf people in GenAI",
    llm='ollama/llama3.1:8b'
)

# Define a simple task for the agent
task = Task(
    description="Give Some Generative AI Learning Path for fresher",
    expected_output="As markdown format",
    agent=agent,
)

# Form a crew with just this agent and task
crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential
)

# Input data for the task
input_data = {"topic": "Artificial Intelligence is rapidly advancing, transforming industries..."}

# Kick off the crew process
result = crew.kickoff()

# Output the result
print(result)
