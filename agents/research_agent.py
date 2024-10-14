from crewai import Agent
from tools.search_tools import serper_search_tool, duck_search_tool

class TrendResearcherAgent:
    """Agent Responsible for Finding Trending Topics in AI."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='AI Trend Researcher',
            goal=(
                'Identify the latest AI trends using online research. '
                'For each trend, validate relevance with at least two trusted sources. '
                'Summarize findings with verified data, avoiding speculative content.'
            ),
            verbose=True,
            memory=True,
            backstory=(
                'An expert AI researcher specializing in finding trends with high precision. '
                'Known for identifying the most relevant developments in AI and ensuring they are well-backed by trusted sources.'
            ),
            tools=[duck_search_tool],
            llm='ollama/mistral-nemo',
            max_retry_limit=3
        )
