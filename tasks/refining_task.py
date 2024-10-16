from crewai import Agent, Task

class TrendingTopicsRevisionTask:
    """Task responsible for assigning the article revision task to TrendingTopicsAIContentReviser."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Your task is to revise the AI-generated draft article: {draft_article}, using the editor's feedback provided in: {feedbacks}. "
                "The revision process must include the following steps:\n\n"
                "1. **Incorporate Feedback:** Thoroughly review the editor's feedback and apply all suggested changes to improve the article.\n\n"
                "2. **Enhance Accuracy and Relevance:** Verify and update any factual information, ensuring the article is aligned with current internet trends.\n\n"
                "3. **Improve Clarity and Coherence:** Refine the text to make the language clearer and ensure the article flows logically between sections.\n\n"
                "4. **Boost Engagement:** Enhance the article's appeal by varying sentence structures, adding compelling examples, and making it more engaging overall.\n\n"
                "5. **Maintain Style and Tone:** Ensure the article maintains a consistent style and tone, suitable for the target audience and publication standards.\n\n"
                "6. **Proofread for Errors:** Conduct a final check to correct grammatical and punctuation errors, and ensure overall readability.\n\n"
                "7. **Check for Plagiarism:** Ensure the article is free from plagiarism by properly citing all sources and rephrasing any content where necessary.\n\n"
                "8. **Final Review:** Perform a final review of the article to ensure it is polished and publication-ready."
            ),
            expected_output=(
                "- **Incorporating Feedback:** All editor feedback has been addressed, and changes have been applied.\n"
                "- **Enhancing Accuracy and Relevance:** The article contains accurate, up-to-date information aligned with current trends.\n"
                "- **Improving Clarity and Coherence:** The article has been refined to ensure clear ideas and logical flow between sections.\n"
                "- **Boosting Engagement:** Engagement strategies like varied sentence structures and compelling examples have been implemented.\n"
                "- **Maintaining Style and Tone:** The article maintains a consistent style and tone suitable for the audience and publication standards.\n"
                "- **Proofreading and Editing:** All grammatical and punctuation errors have been corrected, and readability is improved.\n"
                "- **Plagiarism Check:** The article is free from plagiarism, with properly cited sources.\n"
                "- **Final Review:** The article is polished, error-free, and publication-ready."
            ),
            agent=agent,
            output_file='data/revised_article.txt'
        )