from crewai import Task

class TrendResearcherTask:
    """Task for Finding Trending AI Topics."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Find 10 current AI trends using online research. For each trend:\n'
                '- Validate the trend using at least two credible sources (peer-reviewed journals, news, or industry reports).\n'
                '- Write a 200-word summary backed by these sources.\n'
                '- Avoid speculative information or unverified claims.\n'
                '- Ensure summaries are concise, precise, and fact-checked.'
            ),
            expected_output=(
                'The output should be a JSON file with 10 AI trends. Each entry must include:\n'
                '1. **Topic Name**: The name of the AI trend.\n'
                '2. **Description**: A 200-word summary based on verified data.\n'
                '3. **Sources**: Two valid source links for each trend.\n'
                'Ensure accuracy and trustworthiness by cross-verifying the sources.'
            ),
            agent=agent,
            output_file='data/trending_ai_topics.json'
        )
