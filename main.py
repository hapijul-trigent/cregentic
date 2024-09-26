import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


class EnvironmentSetup:
    @staticmethod
    def setup(api_key: str):
        os.environ["OPENAI_API_KEY"] = api_key


class AgentCreator:
    def __init__(self, role: str, goal: str, backstory: str, llm: str):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm

    def create_agent(self) -> Agent:
        return Agent(
            role=self.role,
            goal=self.goal,
            backstory=self.backstory,
            llm=self.llm
        )


class TaskDefinition:
    def __init__(self, description: str, expected_output: str, agent: Agent):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent

    def create_task(self) -> Task:
        return Task(
            description=self.description,
            expected_output=self.expected_output,
            agent=self.agent
        )


class CrewManager:
    def __init__(self, agents: list, tasks: list):
        self.crew = Crew(
            agents=agents,
            tasks=tasks,
            process=Process.sequential
        )

    def kickoff(self):
        return self.crew.kickoff()


def main():
    EnvironmentSetup.setup("DUMMY_API")

    agent_creator = AgentCreator(
        role='AI Expert',
        goal='Generative AI Trainer',
        backstory="You are experienced in training people in Generative AI",
        llm='ollama/llama3.1:8b'
    )
    agent = agent_creator.create_agent()

    task_definition = TaskDefinition(
        description="Give Some Generative AI Learning Path for fresher",
        expected_output="As markdown format",
        agent=agent
    )
    task = task_definition.create_task()

    crew_manager = CrewManager(agents=[agent], tasks=[task])
    result = crew_manager.kickoff()

    print(result)


if __name__ == "__main__":
    main()
