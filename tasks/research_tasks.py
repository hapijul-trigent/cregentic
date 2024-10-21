from crewai import Agent, Task

class TrendResearcherTask:
    """Task responsible for finding trending topics in AI."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=(
                    'Conduct a thorough and comprehensive research on the latest trends in the AI industry. '
                    'The goal is to identify and analyze 10 distinct topics that are actively discussed in the AI field. '
                    'Each topic should be backed by verified, reputable sources (e.g., peer-reviewed journals, trusted news outlets, or industry-leading reports). '
                    'For each topic, provide a brief summary and relevant source information. Make sure the information gathered is accurate, fact-checked, and not based on speculation. '
                    'Under no circumstances should any part of the research be hallucinated or fabricated. Use only trusted sources for compiling the results.'
                ),
                expected_output=(
                    'A Json file containing 10 trending AI topics. Each entry should have: \n'
                    '1. The topic: topic \n'
                    '2. A 150 to 200 summary derived from the source material: Description \n'
                    '3. A valid, verifiable source link: Source \n'
                    'The file must be structured with the following column names: "topic", "Description", "Sources". \n'
                    'Ensure that each row adheres to this format, and that the content is free of errors or hallucinations. \n'
                    'The research should be based on factual data and legitimate sources, ensuring clarity and precision.'
                ),
                agent=agent,
                output_file='data/trending_topics.json'
            )
