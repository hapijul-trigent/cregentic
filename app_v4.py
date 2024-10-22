import streamlit as st
import json
import os
import sys
from typing import Dict
from crewai import Crew, Process
from utils.constants import STABILITY_API_KEY
from agents.outline_agent import OutlineDrafterAgent
from agents.writer_agent import DraftWriterAgent
from agents.story_drafter_agent import StoryDrafterAgent
from agents.editor_agent import EditorAgent
from agents.publisher_agent import PublisherAgent
from agents.hero_section import ArticleExtractorAgent
from agents.research_agent import TrendResearcherAgent
from agents.reviser_agent import TrendingTopicsAIContentReviser
from tasks.research_tasks import TrendResearcherTask
from tasks.outline_drafting_task import OutlineDraftingTask
from tasks.draft_writing_task import DraftWritingTask
from tasks.story_drafting_task import StoryDraftingTask
from tasks.editor_reviewing_task import EditorReviewingTask
from tasks.hero_section_task import AgentExtractorTask
from tasks.publishing_task import PublishingTask
from tasks.revision_task import TrendingTopicsRevisionTask
import agentops
from dotenv import load_dotenv
load_dotenv()
agentops.init(os.environ['AGENTOPS_API_KEY'])



# Set up Streamlit page configuration
st.set_page_config(
    page_title="Cregentic | Trigent AXLR8 Labs",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Initialize agents
research_agent = TrendResearcherAgent.load_agent()
outline_drafter_agent = OutlineDrafterAgent.load_agent()
draft_writer_agent = DraftWriterAgent.load_agent()
story_drafter_agent = StoryDrafterAgent.load_agent()
editor_agent = EditorAgent.load_agent()
publisher_agent = PublisherAgent.load_agent()
reviser_agent = TrendingTopicsAIContentReviser().load_agent()
hero_section = ArticleExtractorAgent().load_agent()
# Assign tasks
trend_researcher_task = TrendResearcherTask.assign_task(agent=research_agent)
outline_drafting_task = OutlineDraftingTask.assign_task(agent=outline_drafter_agent)
draft_writing_task = DraftWritingTask.assign_task(agent=draft_writer_agent)
story_drafting_task = StoryDraftingTask.assign_task(agent=story_drafter_agent)
editor_reviewing_task = EditorReviewingTask.assign_task(agent=editor_agent)
publishing_task = PublishingTask.assign_task(agent=publisher_agent)
refining_task = TrendingTopicsRevisionTask.assign_task(agent=reviser_agent)
hero_section_task = AgentExtractorTask.assign_task(agent=hero_section)

# Function to run researcher crew
def run_researcher():
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
        topics = json.loads(cleaned_string)
        for topic in topics:
            if "name" in topic:
                topic["topic"] = topic.pop("name")
        f.write(json.dumps(topics, indent=4))

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
        for revision in ['1']:

            with st.spinner("Editor Reviewing the Article Draft"):
                editor_reviewing_crew_inputs = {'enhanced_draft': draft_article.raw, 'outline' : outline.raw}
                feedback = editor_reviewing_crew.kickoff(inputs=editor_reviewing_crew_inputs)
            with st.spinner("Working on the Editor's Feedback"):
                refiner_crew_inputs = {'draft_article': draft_article.raw, 'feedbacks': feedback.raw}
                draft_article = refiner_crew.kickoff(inputs=refiner_crew_inputs)
    st.success('Refined Article!')
    story_drafter_crew_inputs = {'draft_article': draft_article.raw}
    enhanced_draft = story_drafter_crew.kickoff(inputs=story_drafter_crew_inputs)
    return {
        'outline': outline.raw,
        'draft_article': draft_article.raw,
        'enhanced_draft': enhanced_draft.raw,
        'feedback': feedback.raw,
    }

import requests

def generate_image(api_key, prompt, output_file='data/generated_image.jpeg'):
    
    try:
        response = requests.post(
            "https://api.stability.ai/v2beta/stable-image/generate/sd3",
            headers={
                "authorization": f"Bearer {api_key}",
                "accept": "image/*"  
            },
            files={"none": ''}, 
            data={
                "prompt": prompt, 
                "output_format": "jpeg" 
            },
        )

        if response.status_code == 200:
            with open(output_file, 'wb') as file:
                file.write(response.content)  
            print(f"Image successfully generated and saved as {output_file}")
            return "generated_image.jpeg"
        else:
            raise Exception(f"Failed to generate image: {response.json()}")

    except Exception as e:
        print(f"Error: {e}")

def extract_text_from_file(file_path):
    
    try:
        with open(file_path, 'r') as file:
            text = file.read()  
        return text
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generateImageAgent(article):
  hero_section_crew = Crew(
        agents=[hero_section],
        tasks=[hero_section_task],
        process=Process.sequential,
        verbose=False
    )
  hero_section_crew_inputs= {'article':article}
  hero_section_crew.kickoff(inputs=hero_section_crew_inputs)
  prompt = extract_text_from_file(file_path= "data/herosection.txt") 
  image_path= generate_image(api_key=STABILITY_API_KEY, prompt= prompt)
  return image_path

def run_publisher_crews(drafting_crews_output: Dict, image_path): 
    """Run all Article Generator crews for given topic."""
    with st.spinner("Publishing Article"):
        publisher_crew = Crew(
            agents=[publisher_agent],
            tasks=[publishing_task],
            process=Process.sequential,
            verbose=False
        )
        publisher_crew_inputs = {'enhanced_draft': drafting_crews_output['enhanced_draft'],'image_link':image_path}
        final_markdown_article = publisher_crew.kickoff(inputs=publisher_crew_inputs)
    st.success('Article is Ready to Publish!')
    return final_markdown_article.raw

if 'trending_topic' in st.session_state.keys():
    json_file = 'data/trending_topics.json'
else:
    run_researcher()
    json_file = 'data/trending_topics.json'
    st.session_state['trending_topic'] = json_file

# Load data from JSON file
try:
    with open(json_file, 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    st.error("The trending topics file could not be found.")
    data = []

num_topics = len(data)

if 'selected_topic' not in st.session_state:
    st.session_state['selected_topic'] = None

logo_path = "https://trigent.com/wp-content/uploads/Trigent_Axlr8_Labs.png"
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{logo_path}" alt="Trigent Logo" style="height:170px;width:70%">
    </div>
    """,
    unsafe_allow_html=True
)
st.header('Cregentic', divider="rainbow")

col1, col2 = st.columns([1.2, 2])

with col1:
    st.header("Trending Topics :fire:")
    st.subheader("Select a Topic")
    subcol1, subcol2 = st.columns(2)

    def select_topic(topic):
        st.session_state['selected_topic'] = topic

    with subcol1:
        for i in range(min(5, num_topics)):
            topic = data[i]["topic"]
            st.button(topic, key=f"button_{i}", on_click=select_topic, args=(topic,))

    with subcol2:
        for i in range(5, min(10, num_topics)):
            topic = data[i]["topic"]
            st.button(topic, key=f"button_{i}", on_click=select_topic, args=(topic,))

    if st.session_state['selected_topic']:
        selected_topic = next((item for item in data if item["topic"] == st.session_state['selected_topic']), None)
        if selected_topic:
            st.write(f"**Selected Topic:** {selected_topic['topic']}")
            st.write(f"**Description:** {selected_topic['description']}")

        if st.button("Generate Article"):
            topic = {'topic': str(selected_topic["topic"]), 'description': str(selected_topic["description"])}
            drafting_crews_output = run_drafting_crews(topic)
            image_generator = generateImageAgent(article=drafting_crews_output["enhanced_draft"])
            published_article = run_publisher_crews(drafting_crews_output=drafting_crews_output, image_path=image_generator)

            st.session_state['published_article'] = published_article
            st.success("Article generated successfully!")

with col2:
    if 'published_article' in st.session_state.keys():
        st.header("Published Article")
        if 'published_article' in st.session_state:
            st.markdown(st.session_state['published_article'])
            st.download_button(
                label="Download Article",
                data=st.session_state['published_article'],
                file_name="published_article.md",
                mime="text/markdown"
            )
        else:
            st.write("Select a topic and generate an article to see the final result here.")