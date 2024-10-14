from crewai import Agent, Task


class EditorReviewingTask:
    """Task responsible for assigning reviewing task to EditorAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=(
                    "Review the draft article: {enhanced_draft} against the provided outline: {outline}. "
                    "Ensure the following criteria are met:\n\n"
                    "1. *Strict Adherence to Outline:* Verify that each section and key point from the outline is fully developed in the draft. "
                    "Any missing sections, deviations, or alterations from the outline must be identified.\n\n"
                    "2. *Word Count Validation:* Confirm that the draft article reaches the required length of 1500-2000 words, ensuring that all points are "
                    "thoroughly explored.\n\n"
                    "3. *Consistency and Flow:* Check that the draft maintains logical transitions and coherence between sections, as outlined.\n\n"
                    "4. *Feedback for Revision:* Provide detailed feedback in feedback.txt, highlighting areas where the draft diverges from the outline "
                    "or lacks sufficient detail, and recommend revisions accordingly.\n\n"
                    "The final output should be of 1500-2000 words article that strictly follows the outline and is ready for further refinement."
                ),
                expected_output=(
                    "The feedback should include:\n"
                    "- Identification of any missing or misaligned sections.\n"
                    "- Suggestions for improvement in areas that do not meet the outline's requirements.\n"
                    "- Confirmation that the word count meets the 3000-word requirement."
                ),
                agent=agent,
                output_file='data/feedback.txt'
            )    
