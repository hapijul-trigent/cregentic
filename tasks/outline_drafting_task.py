from crewai import Agent, Task

class OutlineDraftingTask:
    """Task responsible for assigning outline drafting to OutlineDrafterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=(
                    "Develop a comprehensive and structured outline for an in-depth article on the topic: {topic}. "
                    "The outline should include clear section headings, subheadings, and detailed bullet points for each section. "
                    "Additionally, incorporate relevant and credible research links to support each section, "
                    "ensuring the content is well-founded and authoritative."
                ),
                expected_output=(
                    "A meticulously organized outline containing:\n"
                    "- Main section headings and subheadings\n"
                    "- Detailed bullet points outlining key points and arguments for each section\n"
                    "- Integrated credible research links and references for each section\n"
                    "- Logical flow and coherence between sections to facilitate seamless article writing."
                ),
                agent=agent,
                output_file="data/outline.txt"
            )
