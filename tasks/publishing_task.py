from crewai import Agent, Task

class PublishingTask:
    """Task for converting the article into markdown format for publication."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Convert the final draft {enhanced_draft} into a well-structured markdown format. '
                'Ensure correct markdown syntax for headings, lists, links, and images, making the article publication-ready.'
            ),
            expected_output=(
                'A markdown file with correct formatting for headings, lists, links, and images, ready for publication.'
            ),
            agent=agent,
            output_file="data/published_article.md"
        )