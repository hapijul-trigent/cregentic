from crewai import Agent, Task
class StoryDraftingTask:
    """Task for enhancing the article's narrative through storytelling techniques."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Enhance the draft {draft_article} by adding storytelling elements such as anecdotes, metaphors, and quotes. '
                'Ensure the narrative flow is coherent and engaging while maintaining technical accuracy.'
            ),
            expected_output=(
                'A 2500 to 4000-word article with a well-crafted narrative, using storytelling techniques to enhance reader engagement.'
            ),
            agent=agent
        )