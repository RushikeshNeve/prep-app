import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import GENERATIVE_AI_TOPIC, TOPIC_DATA

TOPIC_DATA["generative_ai"] = GENERATIVE_AI_TOPIC
topic = GENERATIVE_AI_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
