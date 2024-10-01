from crewai import Agent, Task


class DraftWritingTask:
    """Task responsible for assigning draft writing task to DraftWriterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=("Use the provided {outline} to draft a detailed and well-researched article. "
        "Incorporate relevant information, examples, and research to expand upon the {outline}. "
        "After the article is written, it will be critiqued, and revisions should be made based on feedback."),
                expected_output="The final article should be saved in article.txt, and feedback should be saved in feedback.txt.",
                agent=agent,
                output_file="data/draft.txt"
            )