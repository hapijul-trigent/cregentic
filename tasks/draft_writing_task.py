from crewai import Agent, Task

class DraftWritingTask:
    """Task responsible for assigning the detailed draft writing to the DraftWriterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Write a detailed draft of the article based on the following outline: {outline}. "
                "The draft should cover the following elements:\n\n"
                "1. **Introduction:** Write a captivating opening that introduces the topic and highlights the article's purpose.\n\n"
                "2. **Section Development:** Expand each section and subheading from the outline into well-developed paragraphs. "
                "Ensure each key point is explored thoroughly and supported by relevant information.\n\n"
                "3. **Examples and Explanations:** Integrate specific examples, case studies, or explanations to illustrate each point effectively.\n\n"
                "4. **Conclusion:** Summarize the main points covered in the article and provide a thoughtful closing or call to action.\n\n"
                "5. **Consistency and Flow:** Maintain logical progression from one section to the next, ensuring readability and coherence.\n\n"
                "6. **Proofreading and Editing:** Utilize integrated tools to identify and correct grammatical errors, punctuation issues, and enhance sentence structure.\n\n"
                "The draft should be between 1500 to 2000 words, well-structured, informative, and polished, preparing it for further review by the Editor Agent."
            ),
            expected_output=(
                "A comprehensive draft article including:\n\n"
                "- **Introduction:** An engaging introduction that sets up the article.\n"
                "- **Section Development:** Expanded sections with in-depth coverage of each key point.\n"
                "- **Examples and Explanations:** Relevant examples, case studies, or explanations that illustrate each concept.\n"
                "- **Conclusion:** A concise summary and closing thought or call to action.\n"
                "- **Consistency and Flow:** Seamless transitions and a logical flow between sections.\n"
                "- **Proofreading and Editing:** Polished text with corrected grammar, punctuation, and improved readability."
            ),
            agent=agent,
            output_file="data/draft_article.txt"
        )
