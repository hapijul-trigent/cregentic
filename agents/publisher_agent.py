from crewai import Agent
from utils.constants import MODEL_NAME

class PublisherAgent:
    """Agent responsible for publishing the final article given by StoryDrafterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Markdown Publisher',
            goal='Convert the final article into a clean, structured markdown format, ensuring publication readiness.',
            backstory='You specialize in formatting articles for web publication, ensuring that markdown syntax is applied correctly for optimal readability.',
            
            llm=MODEL_NAME,
            max_retry_limit=3
        )