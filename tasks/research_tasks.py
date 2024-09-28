from crewai import Agent, Task

class ResearchTrendTask:
    """Task responsible for finding trending topics in AI."""

    @staticmethod
    def research_trends(agent: Agent) -> Task:
        return Task(
                description="Search the internet for the latest trending topics in AI",
                expected_output="A list of 20 current trending AI topics with brief descriptions"
                agent=agent
            )
