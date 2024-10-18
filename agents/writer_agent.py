from crewai import Agent
from tools.search_tools import duck_search_tool
from utils.constants import MODEL_NAME

class DraftWriterAgent:
    """Agent responsible for writing the initial draft of the article based on the outline provided by OutlineDrafterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Article Draft Writer',
            goal='Expand the outline into a detailed, coherent draft with sections totaling 2500 to 4000 words.',
            backstory='You are an experienced writer, skilled in transforming outlines into fully-developed drafts that are clear, detailed, and engaging.',
            llm=MODEL_NAME,
            max_retry_limit=3
        )