from crewai import Agent, Task

class StoryDraftingTask:
    """Task responsible for assigning the story enhancement task to StoryDrafterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Your task is to take the {draft_article} and enhance its narrative. '
                'Use storytelling techniques like metaphors, anecdotes, and quotes to make the content more engaging and coherent. '
                'Ensure the article is reader-friendly, while maintaining the integrity of the original information.'
            ),
            expected_output=(
                'The output should be a refined article with enhanced storytelling, between 2500 to 4500 words. '
                'Ensure the article is engaging, well-structured, and maintains technical accuracy, while using storytelling techniques.'
            ),
            agent=agent
        )