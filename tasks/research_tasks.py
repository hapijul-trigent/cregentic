from crewai import Task, Agent
class TrendResearcherTask:
    """Task for finding and summarizing trending AI topics."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                'Use the search tools to find 10 trending AI topics. For each topic:\n'
                '- Ensure relevance by referencing at least two credible sources (peer-reviewed journals, industry reports, or news outlets).\n'
                '- Write a 200 to 250-word summary with verified facts, avoiding speculative information.\n'
                '- Format the output in a structured JSON format with topic name, description, and sources.'
            ),
            expected_output=(
                'A structured JSON file containing:\n'
                '- Topic name\n'
                '- 200 to 250-word summary for each topic\n'
                '- Two or more credible sources for each trend'
            ),
            agent=agent,
            output_file='data/trending_topics.json'
        )