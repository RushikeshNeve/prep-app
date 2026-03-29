import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.agentic_topic import AGENTIC_AI_TOPIC

TOPIC_DATA["agentic_ai"] = AGENTIC_AI_TOPIC
topic = AGENTIC_AI_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
