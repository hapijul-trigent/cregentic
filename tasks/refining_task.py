from crewai import Agent, Task

class TrendingTopicsRevisionTask:
    """Task responsible for assigning article revision to TrendingTopicsAIContentReviser."""

    @staticmethod
    def assign_task(agent: Agent) -> Task:
        return Task(
            description=(
                "Revise the AI-generated draft article on a trending internet topic located at {draft_article} based on the editor's feedback provided in {feedbacks}. "
                "Your revision should include the following steps:\n\n"
                "1. *Incorporating Feedback:* Carefully read and understand the editor's feedback. Address each point meticulously, ensuring that all suggested changes are implemented effectively.\n\n"
                "2. *Enhancing Accuracy and Relevance:* Verify the accuracy of all factual information and ensure that the content remains relevant to current internet trends. Update any outdated information as necessary.\n\n"
                "3. *Improving Clarity and Coherence:* Refine the language to enhance clarity and coherence. Ensure that ideas flow logically and that transitions between sections are seamless.\n\n"
                "4. *Boosting Engagement:* Utilize engagement strategies such as varied sentence structures, rhetorical questions, and compelling examples to make the article more captivating for readers.\n\n"
                "5. *Maintaining Style and Tone:* Ensure that the article maintains a consistent style and tone appropriate for the target audience and publication standards.\n\n"
                "6. *Proofreading and Editing:* Conduct thorough proofreading to eliminate grammatical errors, punctuation mistakes, and improve overall readability.\n\n"
                "7. *Plagiarism Check:* Ensure that the revised article is free from plagiarism by properly citing all sources and rephrasing any borrowed content.\n\n"
                "8. *Final Review:* Perform a final review to ensure that all revisions meet the highest quality standards and that the article is polished and publication-ready.\n\n"
                "Save the refined article to {output_file}."
            ),
            expected_output=(
                "- *Incorporating Feedback:* All editor feedback points have been addressed and implemented effectively.\n"
                "- *Enhancing Accuracy and Relevance:* The article contains accurate and up-to-date information relevant to current internet trends.\n"
                "- *Improving Clarity and Coherence:* Enhanced clarity of ideas and logical flow with seamless transitions between sections.\n"
                "- *Boosting Engagement:* Implementation of engagement strategies such as varied sentence structures and compelling examples.\n"
                "- *Maintaining Style and Tone:* Consistent and appropriate style and tone aligned with target audience and publication standards.\n"
                "- *Proofreading and Editing:* Corrected grammatical errors and improved overall readability.\n"
                "- *Plagiarism Check:* The article is free from plagiarism, with all sources properly cited and content appropriately rephrased.\n"
                "- *Final Review:* A polished, error-free article that is publication-ready."
            ),
            agent=agent,
            # input_files=['{ai_draft_file}', '{feedback_file}'],
            output_file='data/revised_article.txt'
        )
