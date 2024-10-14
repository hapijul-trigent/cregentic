from crewai import Agent, Task


class PublishingTask:
    """Task responsible for assigning publishing article to markdown task to PublisherAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Your task is to transform the final draft article into a clean, well-structured markdown format. "
                "Ensure all headings, lists, links, images, and code snippets (if any) are formatted correctly using markdown "
                "syntax. The article should be readable, visually organized, and ready for immediate publication. Here is the final draft you will work with: {enhanced_draft}."
            ),
            expected_output=(
                "A fully formatted markdown version of the article. The markdown output should follow best practices with proper "
                "hierarchy (headings, subheadings), clean lists (ordered/unordered), and ensure any links, images, or other "
                "embeds are correctly placed. The final output should be publication-ready and saved in a markdown (.md) file."
            ),
            agent=agent,
            output_file="data/published_article.md"
        )
