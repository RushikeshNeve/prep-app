import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.ai_workflows_topic import AI_WORKFLOWS_TOPIC

TOPIC_DATA["ai_workflows"] = AI_WORKFLOWS_TOPIC
topic = AI_WORKFLOWS_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
