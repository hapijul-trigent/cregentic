from crewai import Agent


class StoryDrafterAgent:
    """Agent responsible for enhancing the narrative and engagement on draft article given by DraftWriterAgent"""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Expert Technology Article Writer',
                goal='Refine the given by enhancing the narrative and engagement in 1300-1500 words keeping all article information. Here is the article: {draft_article}',
                verbose=True,
                memory=True,
                backstory="You have a unique ability to turn basic stories into captivating narratives.",
                llm="ollama/mistral-nemo:latest"
            )
