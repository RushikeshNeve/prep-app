import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA

topic = TOPIC_DATA["databases"]
render_topic_header(topic)
render_topic_tabs(topic)
