from crewai import Agent, Task
class AgentExtractorTask:
    """Task for  ."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
      return Task(

         description=(
                  "Given an {article}, your job is to do the following:\n"
                  "1. Identify and extract the *Hero Section* from the article. In this context, the hero section is the part of the article where "
                  "you can include a *Mermaid diagram* to explain the workflow architecture. Look for content that discusses system design, project "
                  "workflow, or architectural details. It is often the most important explanatory section that describes how the system works.\n"
                  "2. Extract the *Introduction* of the article, which typically precedes the hero section and provides a high-level overview of the article's focus.\n\n"
                  "Both the hero section and the introduction MUST be returned exactly as they appear in the article, without any summarization or rephrasing."
         ),
         expected_output=(
                  "The output should include:\n"
                  "1. Hero section content (as it is in the article), which will be suitable for including a *Mermaid diagram*.\n"
                  "2. Introduction content (as it is in the article).\n"
                  "Ensure that both sections are clearly labeled and returned as a dictionary."
         ),
         agent=agent,
         output_file="data/herosection.txt"

      )
