from crewai import Agent

class DraftWriterAgent:
    """Agent responsible for drafting article for StoryDrafterAgent for given ouline by OutlineDrafterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Writer',
                goal='Draft a compelling article within 800-1000 words based on the outline : {outline}',
                verbose=True,
                memory=True,
                backstory="With a flair for simplifying complex topics, you craft engaging content.",
                llm="ollama/mistral-nemo:latest"
            )