from crewai_tools import SerperDevTool
from langchain_community.tools import DuckDuckGoSearchRun

duck_search = DuckDuckGoSearchRun()
serper_search_tool = SerperDevTool()
duck_search_tool = Tool(
    name="Accurate AI Trend Web Research Tool",
    func=search.run,
    description=(
        "A real-time web search tool designed to conduct reliable, up-to-date research on the latest trends in artificial intelligence. "
        "The tool retrieves exactly 10 distinct AI topics, each backed by verified and trusted sources such as academic papers, industry reports, or reputable tech publications. "
        "It specializes in providing factual, trustworthy information on topics like machine learning, natural language processing, AI ethics, and more, ensuring no speculative or hallucinated data is included in the results."
    )
)

# TODO : Venkatesh will be adding DuckDuckGoSearch Tool -> Done