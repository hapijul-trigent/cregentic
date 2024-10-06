from crewai import Agent


class EditorAgent:
    """Agent responsible for reviewing article and giving feedback to improve article  by StoryDrafterAgent"""

    @staticmethod
    def load_agent() -> Agent:
        return  Agent(
                  role='Editor',
                  goal='Review and provide feedback for improvements for the given draft article: {enhanced_draft}',
                  verbose=True,
                  memory=True,
                  backstory="You are responsible for finalizing and publishing articles, ensuring they are properly formatted and stored.",
                  llm="ollama/mistral-nemo:latest"
              )