from crewai import Agent
from tools.search_tools import duck_search_tool
from utils.constants import MODEL_NAME

class DraftWriterAgent:
    """Agent responsible for writing the initial draft of the article based on the outline provided by OutlineDrafterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Article Draft Writer',
            goal='Write a comprehensive article by expanding each section of the provided outline, ensuring each section has sufficient depth and supporting details to achieve a total word count between 2500 and 4000 words.',
            backstory='You are a highly skilled writer with a deep understanding of how to turn structured outlines into detailed, engaging drafts. Your expertise lies in developing each section with sufficient depth, using examples, explanations, and references to maintain clarity and engagement, while ensuring the article meets the word count target of 2500 to 4000 words. Your ability to craft well-rounded, comprehensive articles is critical for providing readers with valuable insights.',
            tools=[duck_search_tool],
            llm=MODEL_NAME,
            max_retry_limit=3
        )