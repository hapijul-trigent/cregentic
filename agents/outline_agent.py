from crewai import Agent
from tools.search_tool import serper_search_tool


class OutlineDrafterAgent:
    """Agent Responsible for drafting outline with reasearch links references."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Outline Creator',
                goal='Create a detailed outline for article on given {topic} with research links.',
                verbose=True,
                memory=True,
                backstory="You are skilled at breaking down topics into structured outlines with helpful references for article writing.",
                tools=[serper_search_tool],
                llm="ollama/mistral-nemo:latest"
            )
