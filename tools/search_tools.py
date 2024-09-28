from crewai_tools import SerperDevTool
from langchain_community.tools import DuckDuckGoSearchRun

duck_search = DuckDuckGoSearchRun()
serper_search_tool = SerperDevTool()
duck_search_tool = Tool(
    name="Web Search for trending AI Topics ",
    func=duck_search.run,
    description="Useful for searching the internet for current information and trends.",
    )

# TODO : Venkatesh will be adding DuckDuckGoSearch Tool