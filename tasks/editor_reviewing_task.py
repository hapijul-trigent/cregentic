from crewai import Agent, Task
class EditorReviewingTask:
    """Task for reviewing the article draft and providing feedback."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Review the draft {enhanced_draft} against the outline {outline}. Ensure each section adheres to the structure and key points in the outline, '
                'verify the word count is between 1500 to 2000 words per section, and provide detailed feedback on any missing sections or errors.'
            ),
            expected_output=(
                'Detailed feedback addressing:\n'
                '- Missing or misaligned sections\n'
                '- Word count validation\n'
                '- Suggestions for improvement\n'
                '- Corrections for clarity and structure'
            ),
            agent=agent,
            output_file="data/feedback.txt"
        )