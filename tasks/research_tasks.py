from crewai import Task, Agent

class TrendResearcherTask:
    """Task for Finding Trending AI Topics."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Find 10 trending AI topics using online research. For each trend:\n'
                '- Validate its relevance using at least two credible sources such as peer-reviewed journals, industry whitepapers, or reputable news outlets.\n'
                '- Write a 200 to 250-word summary that is fact-checked and supported by verified data from the sources.\n'
                '- Avoid any speculative information or unverified claims to ensure accuracy.\n'
                '- Ensure all summaries are clear, concise, and precise.'
            ),
            expected_output=(
                'The output should be a structured JSON file with 10 AI trends. Each entry must include:\n'
                '1. **Topic Name**: The specific name of the AI trend.\n'
                '2. **Description**: A 200 to 250-word fact-based summary supported by reliable sources.\n'
                '3. **Sources**: Links to at least two credible and trustworthy sources for each trend.\n'
                'Accuracy is key, and all information must be cross-verified with trustworthy sources to avoid errors.'
            ),
            agent=agent,
            output_file='data/trending_ai_topics.json'
        )
