from crewai import Agent
from tools.search_tools import serper_search_tool

class OutlineDrafterAgent:
    """Agent Responsible for drafting comprehensive article outlines with research references."""

    @staticmethod
    def load_agent() -> Agent:
        return Agent(
                role='AI Article Outline Creator',
                goal=(
                    "Develop a comprehensive and structured outline for an in-depth article on the provided {topic}. "
                    "The outline should include clear section headings, subheadings, and bullet points detailing key points to cover. "
                    "Integrate credible research links and references to substantiate each section, ensuring the content is well-supported and reliable. "
                    "The final outline should serve as a robust framework that facilitates efficient and high-quality article writing."
                ),
                verbose=True,
                backstory=(
                    "You are an expert content strategist with a deep understanding of various subjects. "
                    "Your strength lies in dissecting complex topics into comprehensive, well-organized outlines. "
                    "You meticulously incorporate relevant research links and references to support each section, "
                    "ensuring the final article is both informative and authoritative. "
                    "Your approach is systematic, creative, and tailored to meet the specific needs of diverse audiences."
                ),
                tools=[serper_search_tool],
                llm="ollama/mistral-nemo:latest"
            )
