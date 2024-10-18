from crewai import Agent
from utils.constants import MODEL_NAME


class TrendingTopicsAIContentReviser:
    """Agent responsible for refining AI-generated articles on trending internet topics based on editorial feedback."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Content Reviser',
            goal='Refine drafts by incorporating editor feedback, ensuring accuracy and engagement.',
            backstory='You specialize in revising content to improve clarity, coherence, and engagement based on feedback, ensuring the article meets high editorial standards.',
            tools=[],
            llm=MODEL_NAME,
            max_retry_limit=3
        )