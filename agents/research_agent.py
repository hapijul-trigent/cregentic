
from crewai import Agent
from tools.search_tools import serper_search_tool, duck_search_tool

class TrendResearcherAgent:
    """Agent Responsible for giving the Finding Trending topics in AI."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Artificial Intelligence Trend Researcher',
                goal=' Identify and provide concise, two-line summaries of the latest trends in artificial intelligence through online research.',
                verbose= True,
                memory=True,
                backstory='A seasoned AI researcher known for efficiently distilling complex information into insightful summaries. Equipped with years of expertise in tracking emerging technologies and innovations in AI.',
                tools=[duck_search_tool],
                llm = 'ollama/mistral-nemo',
                max_retry_limit=3
            )
