from crewai import Agent, Task


class PublishingTask:
    """Task responsible for assigning publishing article to markdown task to PublisherAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description="Convert the final draft arttcle into markdown format. Here is the final draft: {enhanced_draft}",
                expected_output="A markdown formatted article.",
                agent=agent,
                output_file="final_article.md"
            )