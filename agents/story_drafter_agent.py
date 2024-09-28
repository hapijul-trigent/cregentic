from crewai import Agent


class StoryDrafterAgent:
    """Agent responsible for enhancing the narrative and engagement on draft article given by DraftWriterAgent"""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Storyteller',
                goal='Refine the {draft_article} by enhancing the narrative and engagement in 1300-1500 words.',
                verbose=True,
                memory=True,
                backstory="You have a unique ability to turn basic stories into captivating narratives.",
                llm="ollama/mistral-nemo:latest"
            )