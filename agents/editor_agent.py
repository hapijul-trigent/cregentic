from crewai import Agent
from utils.constants import MODEL_NAME

class EditorAgent:
    """Agent responsible for reviewing and validating the article created by StoryDrafterAgent, ensuring alignment with the original outline."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Article Editor',
            goal='Review the draft for structure, clarity, and adherence to the outline, ensuring it meets the desired word count.',
            backstory='You are an expert editor known for your keen eye for structure and consistency, ensuring that articles are aligned with the outline and free from errors.',
            llm=MODEL_NAME,
            max_retry_limit=3
        )
