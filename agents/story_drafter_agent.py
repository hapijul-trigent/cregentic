from crewai import Agent
from utils.constants import MODEL_NAME

class StoryDrafterAgent:
    """Agent responsible for enhancing the narrative and engagement of a draft article created by the DraftWriterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Storytelling Expert',
            goal='Add storytelling elements like anecdotes and metaphors to make the article more engaging.',
            backstory='You are a master storyteller, focused on turning technical content into narratives that captivate readers while maintaining factual accuracy.',
            
            llm=MODEL_NAME,
            max_retry_limit=3
        )