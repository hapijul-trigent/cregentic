import sys
import os

for root, dirs, files in os.walk("."):
  for dir in dirs:
    sys.path.append(os.path.abspath(os.path.join(root, dir)))

from typing import Dict
from crewai import Crew, Process, agent
from agents.outline_agent import OutlineDrafterAgent
from agents.writer_agent import DraftWriterAgent
from agents.story_drafter_agent import StoryDrafterAgent
from agents.editor_agent import EditorAgent
from agents.publisher_agent import PublisherAgent
from agents.research_agent import TrendResearcherAgent
from agents.reviser_agent import TrendingTopicsAIContentReviser
from tasks.research_tasks import TrendResearcherTask
from tasks.outline_drafting_task import OutlineDraftingTask
from tasks.draft_writing_task import DraftWritingTask
from tasks.story_drafting_task import StoryDraftingTask
from tasks.editor_reviewing_task import EditorReviewingTask
from tasks.publishing_task import PublishingTask
from tasks.refining_task import TrendingTopicsRevisionTask
import agentops
import pandas as pd
# agentops.init("KEY")

# TODO : Venkatesh will add Researcher Agent -> worked on this -> Should connect with Happy and update it.
# load all agents
research_agent = TrendResearcherAgent.load_agent()
outline_drafter_agent = OutlineDrafterAgent.load_agent()
draft_writer_agent =  DraftWriterAgent.load_agent()
story_drafter_agent = StoryDrafterAgent.load_agent()
editor_agent = EditorAgent.load_agent()
publisher_agent = PublisherAgent.load_agent()
reviser_agent = TrendingTopicsAIContentReviser().load_agent()


# Assign Task
trend_researcher_task = TrendResearcherTask.assign_task(agent=research_agent)
outline_drafting_task = OutlineDraftingTask.assign_task(agent=outline_drafter_agent)
draft_writing_task = DraftWritingTask.assign_task(agent=draft_writer_agent)
story_drafting_task = StoryDraftingTask.assign_task(agent=story_drafter_agent)
editor_reviewing_task = EditorReviewingTask.assign_task(agent=editor_agent)
publishing_task = PublishingTask.assign_task(agent=publisher_agent)
refining_task = TrendingTopicsRevisionTask.assign_task(agent=reviser_agent)

def run_researcher():
    """Run Researcher Crew to fetch trending topics"""
    global research_agent, trend_researcher_task
    researcher_crew = Crew(
        agents=[research_agent],
        tasks=[trend_researcher_task],
        verbose=False,
        process=Process.sequential
    )
    trend_topics = researcher_crew.kickoff()

    
    with open('data/trending_topics.json', mode='w') as f:
        cleaned_string = str(trend_topics.raw).replace('**', '')
        cleaned_string = cleaned_string.replace('```json', '').replace('```', '').strip()
        f.write(cleaned_string)

def run_drafting_crews(topic: Dict): 
    """Run all Article Generator crews for given topic."""
    outline_drafter_crew = Crew(
        agents=[outline_drafter_agent],
        tasks=[outline_drafting_task],
        process=Process.sequential,
        verbose=False
    )
    outline = outline_drafter_crew.kickoff(inputs=topic)


    draft_writer_crew = Crew(
        agents=[draft_writer_agent],
        tasks=[draft_writing_task],
        process=Process.sequential,
        verbose=False
    )
    draft_writer_crew_inputs = {'outline': outline.raw}
    draft_article = draft_writer_crew.kickoff(inputs=draft_writer_crew_inputs)


    for revision in ['1', '2']:
        story_drafter_crew = Crew(
            agents=[story_drafter_agent],
            tasks=[story_drafting_task],
            process=Process.sequential,
            verbose=False
        )
        story_drafter_crew_inputs = {'draft_article': draft_article.raw}
        enhanced_draft = story_drafter_crew.kickoff(inputs=story_drafter_crew_inputs)


        editor_reviewing_crew = Crew(
            agents=[editor_agent],
            tasks=[editor_reviewing_task],
            process=Process.sequential,
            verbose=False
        )
        editor_reviewing_crew_inputs = {'enhanced_draft': enhanced_draft.raw}
        feedback = editor_reviewing_crew.kickoff(inputs=editor_reviewing_crew_inputs)

        refiner_crew = Crew(
            agents=[reviser_agent],
            tasks=[refining_task],
            process=Process.sequential,
            verbose=False
        )
        refiner_crew_inputs = {'draft_article': enhanced_draft.raw, 'feedbacks': feedback.raw}
        draft_article = refiner_crew.kickoff(inputs=refiner_crew_inputs)

    return {
        'outline': outline.raw,
        'draft_article': draft_article.raw,
        'enhanced_draft': enhanced_draft.raw,
        'feedback': feedback.raw,
    }

def run_publisher_crews(drafting_crews_output: Dict): 
    """Run all Article Generator crews for given topic."""
    publisher_crew = Crew(
        agents=[publisher_agent],
        tasks=[publishing_task],
        process=Process.sequential,
        verbose=False
    )
    publisher_crew_inputs = {'enhanced_draft': drafting_crews_output['draft_article']}
    final_markdown_article = publisher_crew.kickoff(inputs=publisher_crew_inputs)




if __name__ == '__main__':
    run_researcher()

    df = pd.read_json('data/trending_topics.json')
    first_row = df.iloc[0]
    trending_topic = first_row['Topic']

    topic = {'topic': str(trending_topic)}
    drafting_crews_output = run_drafting_crews(topic)
    run_publisher_crews(drafting_crews_output=drafting_crews_output)
