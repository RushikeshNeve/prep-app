import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.databases_topic import DATABASES_TOPIC

TOPIC_DATA["databases"] = DATABASES_TOPIC
topic = DATABASES_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
