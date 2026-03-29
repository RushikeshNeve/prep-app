import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.apis_topic import APIS_BACKEND_TOPIC

TOPIC_DATA["apis_backend"] = APIS_BACKEND_TOPIC
topic = APIS_BACKEND_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
