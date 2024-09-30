from crewai import Agent, Task


class StoryDraftingTask:
    """Task responsible for assigning story drafting task to StoryDrafterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description="Refine the {draft_article} to enhance its narrative and engagement.",
                expected_output="A refined article with engaging storytelling within 1200-1300 words.",
                agent=agent
            )