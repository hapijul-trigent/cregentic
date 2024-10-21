from crewai import Agent, Task

class DraftWritingTask:
    """Task for writing a detailed draft of the article based on the outline."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Write a comprehensive draft of the article based on the provided outline {outline}. '
                'Each section must contain 500 to 800 words to ensure in-depth exploration.\n'
                '- Start with a strong introduction.\n'
                '- For each section, expand on the outline with detailed explanations, examples, and references.\n'
                '- Maintain consistency and flow between sections, ensuring a total word count of 2500 to 4000 words.\n'
                '- Conclude with a well-rounded conclusion.'
            ),
            expected_output=(
                'A draft article with the following:\n'
                '- Introduction\n'
                '- Well-expanded sections (500 to 800 words each)\n'
                '- Examples and references to support the content\n'
                '- Conclusion\n'
                '- Total word count between 2500 to 4000 words'
            ),
            agent=agent,
            output_file="data/draft_article.txt"
        )
