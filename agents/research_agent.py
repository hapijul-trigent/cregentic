from crewai import Agent
from tools.search_tools import serper_search_tool, duck_search_tool
from utils.constants import MODEL_NAME, RESEARCH_LLM

class TrendResearcherAgent:
    """Agent responsible for finding trending AI topics using online tools."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='AI Trend Researcher',
            goal='Use search tools to identify trending AI topics and provide verified, well-researched summaries.',
            tools=[duck_search_tool],
            backstory='You are a specialized AI researcher responsible for identifying current trends in AI, ensuring that the information is accurate and supported by trustworthy sources.',
            llm=RESEARCH_LLM
        )
