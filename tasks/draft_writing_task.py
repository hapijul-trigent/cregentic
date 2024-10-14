from crewai import Agent, Task

class DraftWritingTask:
    """Task responsible for assigning draft writing to WriterAgent."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
                description=(
                    "Write a comprehensive draft article based on the following outline: {outline}. "
                    "Your draft should include the following elements:\n\n"
                    "1. **Introduction:** Craft an engaging opening that introduces the topic and outlines the article's purpose.\n\n"
                    "2. **Section Development:** Expand each section and subheading from the outline into detailed paragraphs. Ensure that each key point is thoroughly explored and supported with relevant information.\n\n"
                    "3. **Examples and Explanations:** Incorporate relevant examples, case studies, or explanations to illustrate and support each point.\n\n"
                    "4. **Conclusion:** Summarize the main points discussed in the article and provide a closing thought or call to action.\n\n"
                    "5. **Consistency and Flow:** Ensure that the article flows logically from one section to the next, maintaining coherence and readability throughout.\n\n"
                    "6. **Proofreading and Editing:** Utilize integrated tools to check for grammatical errors, punctuation mistakes, and improve sentence structures for better readability.\n\n"
                    "The final draft should be between 1500-2000 words, well-structured, informative, and ready for further refinement by the EditorAgent."
                ),
                expected_output=(
                    "A detailed draft article containing:\n\n"
                    "- **Introduction:** An engaging opening that sets the stage for the article.\n"
                    "- **Section Development:** Expanded sections with thorough exploration of each key point.\n"
                    "- **Examples and Explanations:** Relevant examples and explanations that support and illustrate each point.\n"
                    "- **Conclusion:** A concise summary and closing thought or call to action.\n"
                    "- **Consistency and Flow:** Logical progression and seamless transitions between sections.\n"
                    "- **Proofreading and Editing:** Corrected grammatical errors, punctuation mistakes, and improved sentence structures, ensuring a polished and readable draft."
                ),
                agent=agent,
                output_file="data/draft_article.txt"
            )
