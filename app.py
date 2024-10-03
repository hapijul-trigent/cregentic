import streamlit as st
st.set_page_config(
    page_title="Crigentic | Trigent AXLR8 Labs",
    layout="wide",
    initial_sidebar_state="collapsed",
)
import json
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
    with st.spinner("Drafting Outline"):
        outline = outline_drafter_crew.kickoff(inputs=topic)
    st.success('Outline Drafting Successful!')

    draft_writer_crew = Crew(
        agents=[draft_writer_agent],
        tasks=[draft_writing_task],
        process=Process.sequential,
        verbose=False
    )
    with st.spinner("Drafting Article"):
        draft_writer_crew_inputs = {'outline': outline.raw}
        draft_article = draft_writer_crew.kickoff(inputs=draft_writer_crew_inputs)
    st.success('Article Drafting Successful!')
    # Feedback loop
    story_drafter_crew = Crew(
        agents=[story_drafter_agent],
        tasks=[story_drafting_task],
        process=Process.sequential,
        verbose=False
    )

    editor_reviewing_crew = Crew(
        agents=[editor_agent],
        tasks=[editor_reviewing_task],
        process=Process.sequential,
        verbose=False
    )

    refiner_crew = Crew(
        agents=[reviser_agent],
        tasks=[refining_task],
        process=Process.sequential,
        verbose=False
    )
    with st.spinner("Refining the Article"):
        for revision in ['1', '2']:

            # story_drafter_crew_inputs = {'draft_article': draft_article.raw}
            # enhanced_draft = story_drafter_crew.kickoff(inputs=story_drafter_crew_inputs)
            with st.spinner("Editor Reviewing the Article Draft"):
                editor_reviewing_crew_inputs = {'enhanced_draft': draft_article.raw}
                feedback = editor_reviewing_crew.kickoff(inputs=editor_reviewing_crew_inputs)
            with st.spinner("Working on the Editor's Feedback"):
                refiner_crew_inputs = {'draft_article': draft_article.raw, 'feedbacks': feedback.raw}
                draft_article = refiner_crew.kickoff(inputs=refiner_crew_inputs)
    st.success('Refined Article!')
    # story_drafter_crew_inputs = {'draft_article': draft_article.raw}
    # enhanced_draft = story_drafter_crew.kickoff(inputs=story_drafter_crew_inputs)
    return {
        'outline': outline.raw,
        'draft_article': draft_article.raw,
        # 'enhanced_draft': enhanced_draft.raw,
        'feedback': feedback.raw,
    }

def run_publisher_crews(drafting_crews_output: Dict): 
    """Run all Article Generator crews for given topic."""
    with st.spinner("Publishing Article"):
        publisher_crew = Crew(
            agents=[publisher_agent],
            tasks=[publishing_task],
            process=Process.sequential,
            verbose=False
        )
        publisher_crew_inputs = {'enhanced_draft': drafting_crews_output['draft_article']}
        final_markdown_article = publisher_crew.kickoff(inputs=publisher_crew_inputs)
    st.success('Article is Ready to Publish!')
    return final_markdown_article.raw




# if __name__ == '__main__':
#     run_researcher()

#     df = pd.read_json('data/trending_topics.json')
#     first_row = df.iloc[0]
#     trending_topic = first_row['Topic']

#     topic = {'topic': str(trending_topic)}
#     drafting_crews_output = run_drafting_crews(topic)
#     run_publisher_crews(drafting_crews_output=drafting_crews_output)

if 'trending_topic' in st.session_state.keys():
    json_file = 'data/trending_topics.json'
else:
  run_researcher()
  json_file = 'data/trending_topics.json'
  st.session_state['trending_topic'] = json_file


try:
    with open(json_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("The trending topics file could not be found.")
    data = []

num_topics = len(data)

if 'selected_topic' not in st.session_state:
    st.session_state['selected_topic'] = None



st.markdown("""
<style>
[data-testid="column"] {
    border-right: 2px solid black;
    padding-right: 20px;
}
[data-testid="column"]:last-child {
    border-right: none;
}
.stApp > header {
    background-color: transparent;
}
.stApp {
    margin-top: -80px;
}
</style>
""", unsafe_allow_html=True)

logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{logo_path}" alt="Trigent Logo" style="height:170px;width:70%">
    </div>
    """,
    unsafe_allow_html=True
)
st.header('Crigentic', divider="rainbow")

col1, col2 = st.columns([1.2, 2])

with col1:
    st.header("Trending Topics :fire:")
    st.subheader("Select a Topic")
    subcol1, subcol2 = st.columns(2)

    def select_topic(topic):
        st.session_state['selected_topic'] = topic

    with subcol1:
        for i in range(min(5, num_topics)):
            topic = data[i]['Topic']
            st.button(topic, key=f"button_{i}", on_click=select_topic, args=(topic,))

    with subcol2:
        for i in range(5, min(10, num_topics)):
            topic = data[i]['Topic']
            st.button(topic, key=f"button_{i}", on_click=select_topic, args=(topic,))

    if st.session_state['selected_topic']:
        selected_topic = next((item for item in data if item['Topic'] == st.session_state['selected_topic']), None)
        if selected_topic:
            st.write(f"**Selected Topic:** {selected_topic['Topic']}")
            st.write(f"**Description:** {selected_topic['Description']}")

        if st.button("Generate Article"):
            
            topic = {'topic': str(selected_topic['Topic'])}
            drafting_crews_output = run_drafting_crews(topic)
            published_article = run_publisher_crews(drafting_crews_output=drafting_crews_output)

            st.session_state['published_article'] = published_article
            st.success("Article generated successfully!")

    # if 'published_article' in st.session_state:
    #     st.subheader("Article Components")
    #     st.write("**Outline:**", st.session_state['results']['outline'])
    #     st.write("**Draft Article:**", st.session_state['results']['draft_article'])
    #     st.write("**Enhanced Draft:**", st.session_state['results']['enhanced_draft'])
    #     st.write("**Editor's Feedback:**", st.session_state['results']['feedback'])

with col2:
  if 'published_article' in st.session_state.keys():
      st.header("Published Article")
      if 'published_article' in st.session_state:
          st.markdown(st.session_state['published_article'])
      else:
          st.write("Select a topic and generate an article to see the final result here.")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<div style="text-align: center;">
    <p>
        Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank" aria-label="Trigent Website">Trigent Software Inc.</a> All rights reserved. |
        <a href="https://www.linkedin.com/company/trigent-software/" target="_blank" aria-label="Trigent LinkedIn"><i class="fab fa-linkedin"></i></a> |
        <a href="https://www.twitter.com/trigentsoftware/" target="_blank" aria-label="Trigent Twitter"><i class="fab fa-twitter"></i></a> |
        <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank" aria-label="Trigent Youtube"><i class="fab fa-youtube"></i></a>
    </p>
</div>
""", unsafe_allow_html=True)
