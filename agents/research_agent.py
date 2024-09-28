
from crewai import Agent
from tools.search_tool import serper_search_tool

class TrendResearcherAgent:
    """Agent Responsible for giving the Finding Trending topics in AI."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Artificial Intelligence Trend Researcher',,
                goal='Search the internet for trending topics on AI'
                verbose=True,
                memory=True,
                backstory='An expert analyst with a keen eye for market trends.', 
                tools=[serper_search_tool],
                llm="ollama/mistral-nemo:latest",
                max_retry_limit=3
            )