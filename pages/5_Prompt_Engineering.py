import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.prompt_topic import PROMPT_ENGINEERING_TOPIC

TOPIC_DATA["prompt_engineering"] = PROMPT_ENGINEERING_TOPIC
topic = PROMPT_ENGINEERING_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
