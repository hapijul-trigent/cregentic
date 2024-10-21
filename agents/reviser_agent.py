from crewai import Agent
from utils.constants import MODEL_NAME


class TrendingTopicsAIContentReviser:
    """Agent responsible for refining AI-generated articles on trending internet topics based on editorial feedback."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='Content Reviser',
            goal='Incorporate editorial feedback to refine the article, improving clarity, coherence, and accuracy while ensuring the content remains engaging and aligned with the original intent.',
            backstory='You are an expert content reviser, skilled at refining drafts to meet high editorial standards. Your expertise lies in improving the clarity, coherence, and flow of articles, while ensuring that feedback is incorporated seamlessly and the content retains its original intent. You are meticulous in your revisions, making sure every article is accurate, engaging, and polished to perfection before it moves forward in the publishing process.',
            tools=[],
            llm=MODEL_NAME,
            max_retry_limit=3
    )