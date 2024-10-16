from crewai import Agent, Task

class PublishingTask:
    """Task responsible for assigning the article-to-markdown transformation task to PublisherAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Your task is to transform the final draft article into a clean, well-structured markdown format. "
                "Ensure all headings, lists, links, images, and code snippets (if any) are formatted correctly using markdown syntax. "
                "The article should be visually organized, readable, and optimized for publication. Ensure the markdown adheres to best practices for "
                "web content formatting. Here is the final draft you will work with: {enhanced_draft}."
            ),
            expected_output=(
                "A fully formatted markdown version of the article. The markdown output should follow best practices, including the use of proper hierarchy "
                "(headings, subheadings), clean lists (ordered/unordered), and ensure any links, images, or embeds are correctly placed. "
                "The final output should be ready for immediate publication, saved in a markdown (.md) file."
            ),
            agent=agent,
            output_file="data/published_article.md"
        )