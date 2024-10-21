from crewai import Agent, Task
class TrendingTopicsRevisionTask:
    """Task for revising the draft based on editor feedback."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Revise the draft article {draft_article} using the editor feedback {feedbacks}. '
                'Ensure that all feedback points are incorporated, and the article is accurate, clear, and engaging. '
                'Make necessary adjustments to improve coherence and factual accuracy without reducing content.'
            ),
            expected_output=(
                'A revised article that addresses all feedback, ensuring accuracy and engagement. '
                'The article should maintain or improve the word count and readability.'
            ),
            agent=agent,
            output_file="data/revised_article.txt"
        )