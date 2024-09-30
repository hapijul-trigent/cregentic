from crewai import Agent, Task


class DraftWritingTask:
    """Task responsible for assigning draft writing task to DraftWriterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description="Draft a compelling article based on the provided {outline}.",
                expected_output="A full detailed article in 1000-1200",
                agent=agent,
                output_file="data/draft.txt"
            )