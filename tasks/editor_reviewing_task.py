from crewai import Agent, Task


class EditorReviewingTask:
    """Task responsible for assigning reviewing task to EditorAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=(
                    "Review the article draft and provide feedback on its structure, clarity, grammar, and storytelling elements of given article: {enhanced_draft}"
                    "Store the feedback in feedback.txt and highlight any areas that need to be revised for Writer agent."
                ),
                expected_output='Feedback on the article saved to feedback.txt',
                agent=agent,
                output_file='feedback.txt'
            )