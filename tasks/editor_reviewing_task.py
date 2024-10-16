from crewai import Agent, Task

class EditorReviewingTask:
    """Task responsible for assigning the article reviewing task to EditorAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Your task is to review the draft article: {enhanced_draft} against the provided outline: {outline}. "
                "Ensure that the following key criteria are met:\n\n"
                "1. **Adherence to Outline**: Verify that each section and key point from the outline is thoroughly covered in the draft. "
                "Identify any missing sections or deviations from the outline and provide detailed notes.\n\n"
                "2. **Word Count Validation**: Confirm that the draft article is between 1500 to 2000 words, ensuring all key points are sufficiently explored.\n\n"
                "3. **Consistency and Flow**: Ensure that the draft maintains logical transitions between sections and follows the flow outlined in the structure.\n\n"
                "4. **Feedback for Revisions**: Provide detailed, actionable feedback in feedback.txt. Highlight areas where the draft diverges from the outline, lacks depth, or needs improvement."
            ),
            expected_output=(
                "The feedback should include:\n"
                "- Identification of missing or misaligned sections.\n"
                "- Suggestions for improving sections that do not meet the outline's requirements.\n"
                "- Confirmation that the word count falls within the range of 1500 to 2000 words.\n"
                "- Detailed notes to improve the article's consistency, structure, and flow."
            ),
            agent=agent,
            output_file='data/feedback.txt'
        )