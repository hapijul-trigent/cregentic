import streamlit as st
import json
import os
import pandas as pd
from crewai import Crew, Process, agent
from typing import Dict
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

# Set page config
st.set_page_config(
    page_title="Crigentic | Trigent AXLR8 Labs",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def display_how_it_works():
    st.markdown("### How it works:")
    st.markdown("""
    1. **Generate Trending Topics**: Click the button to fetch the latest trending AI research topics.
    2. **Choose a Topic**: After generating the topics, users can select a topic from the displayed options.
    3. **Draft Article Creation**: The system initiates the drafting process, including outline creation, drafting, and refinement.
    4. **Publish and Download**: Users can download the final article in Markdown format.
    """)

display_how_it_works()

# Load agents and assign tasks (original logic)
research_agent = TrendResearcherAgent.load_agent()
outline_drafter_agent = OutlineDrafterAgent.load_agent()
draft_writer_agent = DraftWriterAgent.load_agent()
story_drafter_agent = StoryDrafterAgent.load_agent()
editor_agent = EditorAgent.load_agent()
publisher_agent = PublisherAgent.load_agent()
reviser_agent = TrendingTopicsAIContentReviser().load_agent()

trend_researcher_task = TrendResearcherTask.assign_task(agent=research_agent)
outline_drafting_task = OutlineDraftingTask.assign_task(agent=outline_drafter_agent)
draft_writing_task = DraftWritingTask.assign_task(agent=draft_writer_agent)
story_drafting_task = StoryDraftingTask.assign_task(agent=story_drafter_agent)
editor_reviewing_task = EditorReviewingTask.assign_task(agent=editor_agent)
publishing_task = PublishingTask.assign_task(agent=publisher_agent)
refining_task = TrendingTopicsRevisionTask.assign_task(agent=reviser_agent)

def run_researcher():
    """Run Researcher Crew to fetch trending topics"""
    researcher_crew = Crew(
        agents=[research_agent],
        tasks=[trend_researcher_task],
        verbose=False,
        process=Process.sequential
    )
    trend_topics = researcher_crew.kickoff()
    
    # Save topics to json
    with open('data/trending_topics.json', mode='w') as f:
        cleaned_string = str(trend_topics.raw).replace('**', '')
        cleaned_string = cleaned_string.replace('```json', '').replace('```', '').strip()
        f.write(cleaned_string)

# UI styling for cards
st.markdown("""
    <style>
    .card {
        background-color: #f7f7f7;
        padding: 20px;
        margin: 10px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 18px;
        font-family: 'Arial', sans-serif;
        color: #333;
    }
    h1 {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 30px;
        text-align: left;
    }
    .section {
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# Generate Trending Topics button
if st.button("Generate Trending Topics"):
    run_researcher()
    st.session_state['trending_topics'] = 'data/trending_topics.json'

if 'trending_topics' in st.session_state:
    try:
        with open(st.session_state['trending_topics'], 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        st.error("The trending topics file could not be found.")
        data = []

    # Display trending topics in a matrix (grid) format
    if data:
        st.markdown('<div class="section"><h1>Trending AI Research Topics</h1></div>', unsafe_allow_html=True)

        # Define the number of columns per row
        cols_per_row = 3

        # Split the topics into chunks of 3 and display them in a grid
        for i in range(0, len(data), cols_per_row):
            cols = st.columns(cols_per_row)
            for idx, topic in enumerate(data[i:i + cols_per_row]):
                with cols[idx]:
                    st.markdown(f'<div class="card">{topic["Topic Name"]}</div>', unsafe_allow_html=True)
    
    st.header("Select a topic to generate an article in the next section.")
    # Dropdown for topic selection
    topic_names = [item['Topic Name'] for item in data]
    selected_topic = st.selectbox("Choose a Topic", topic_names, key='selected_topic')

    if selected_topic:
        topic = {'topic': selected_topic}

        if st.button("Generate Article"):
            drafting_crews_output = run_drafting_crews(topic)
            published_article = run_publisher_crews(drafting_crews_output=drafting_crews_output)

            col1, col2 = st.columns([1, 2])

            with col1:
                st.subheader("Outline")
                st.write(drafting_crews_output['outline'])
                st.subheader("Draft Article")
                st.write(drafting_crews_output['draft_article'])

            with col2:
                st.subheader("Published Article")
                st.markdown(published_article)
                st.download_button(
                    label="Download Article",
                    data=published_article,
                    file_name="published_article.md",
                    mime="text/markdown"
                )

# Footer with social links
footer_html = """
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
   <div class='footer'>
       <p>
           Copyright © 2024 | <a href="https://trigent.com/ai/" target="_blank">Trigent Software Inc.</a> All rights reserved. |
           <a href="https://www.linkedin.com/company/trigent-software/" target="_blank"><i class="fab fa-linkedin"></i></a> |
           <a href="https://www.twitter.com/trigentsoftware/" target="_blank"><i class="fab fa-twitter"></i></a> |
           <a href="https://www.youtube.com/channel/UCNhAbLhnkeVvV6MBFUZ8hOw" target="_blank"><i class="fab fa-youtube"></i></a>
       </p>
   </div>
   """
st.markdown(footer_html, unsafe_allow_html=True)
