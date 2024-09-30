from crewai import Agent, Task


class OutlineDraftingTask:
    """Task responsible for assigning outline drafting to OutlineDrafterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description="Create a detailed outline for {topic} with relevant research links.",
                expected_output="Must be a structured outline with headings and research links.",
                agent=agent,
                output_file="data/outline.txt"
            )
