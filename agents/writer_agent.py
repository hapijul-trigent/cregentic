from crewai import Agent

class DraftWriterAgent:
    """Agent responsible for drafting article for StoryDrafterAgent for given ouline by OutlineDrafterAgent."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='expert_article_writer',
                goal='Transform the provided into a detailed, engaging, and well-researched article that meets high editorial standards: {outline}                
                verbose=True,
                memory=True,
                backstory=""" 'As an expert article writer, your job is to take the provided  and craft a coherent, comprehensive, and informative article.'
                            'You will need to ensure that each section of the  is elaborated with rich insights, examples, and well-supported arguments. '
                            'You must produce articles that are not only factually accurate but also engaging for the reader. '
                            'The writing process is iterative, with feedback captured in feedback.txt, allowing revisions to be made until the article is polished and no further feedback is required.'""",
                llm="ollama/mistral-nemo:latest"
            )