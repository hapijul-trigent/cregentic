from crewai import Agent


class PublisherAgent:
    """Agent responsible for publishing the final article given by StoryDrafterAgent"""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='Publisher',
                goal='Convert the final draft article into markdown format. Here is the draft article : {enhanced_draft}',
                verbose=True,
                memory=True,
                backstory="You ensure articles are well-formatted and ready for publication in markdown.",
                llm="ollama/mistral-nemo:latest"
            )