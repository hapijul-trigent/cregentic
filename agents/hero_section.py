from crewai import Agent
from tools.search_tools import serper_search_tool, duck_search_tool
from utils.constants import MODEL_NAME, RESEARCH_LLM

class ArticleExtractorAgent:
    """Agent responsible for."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Article Section Extractor',
                goal='Extract the section which and introduction from the article.',
                verbose=True,
                memory=False,
                backstory=(
                  "You are an expert at analyzing articles and identifying the most critical sections. "
                  "Your primary function is to accurately extract the hero section and introduction without altering the original content."
              ),
                llm=MODEL_NAME,
                tools=[]
            )
