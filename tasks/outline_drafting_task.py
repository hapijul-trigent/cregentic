from crewai import Agent, Task

class OutlineDraftingTask:
    """Task responsible for assigning the detailed outline drafting to OutlineDrafterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Expand on the high-level outline by creating a detailed and structured draft for the article on {topic}. "
                "Develop clear section headings, subheadings, and bullet points for each main idea. "
                "Incorporate specific research links and references, as well as evidence to support each section, ensuring that each point is well-founded. "
                "Ensure a logical progression of ideas, so that each section builds naturally upon the previous one to guide the writing process."
            ),
            expected_output=(
                "A comprehensive and detailed outline containing:\n"
                "- Main section headings and subheadings with supporting details\n"
                "- Bullet points elaborating key ideas and arguments for each section\n"
                "- Credible research links and references integrated into each relevant section\n"
                "- A logical flow to support coherent writing from introduction to conclusion"
            ),
            agent=agent,
            output_file="data/outline.txt"
        )