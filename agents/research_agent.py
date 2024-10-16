from crewai import Agent
from tools.search_tools import serper_search_tool, duck_search_tool

class TrendResearcherAgent:
    """Agent Responsible for Finding Trending Topics in AI."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
            role='AI Trend Researcher',
            goal=(
                'Identify the latest AI trends using thorough online research. '
                'For each trend, validate its relevance by referencing at least two trusted and credible sources such as peer-reviewed journals, industry whitepapers, or reputable news outlets. '
                'Summarize the findings with accurate, fact-checked data while avoiding speculative or unverified content.'
            ),
            verbose=True,
            memory=True,
            backstory=(
                'The AI Trend Researcher Agent is highly regarded for its precision in identifying relevant and impactful developments in artificial intelligence. '
                'This agent is known for its ability to extract trends from vast online data while ensuring that only well-supported facts make it into reports. '
                'With a commitment to providing accurate, actionable insights, this agent references trustworthy sources like industry reports or top-tier academic publications. '
                'In fact, a quote often associated with the Researcher is, "Data speaks, but only the most credible voices should be heard."'
            ),
            tools=[duck_search_tool],
            llm='ollama/mistral-nemo',
            max_retry_limit=3
        )
