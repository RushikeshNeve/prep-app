import streamlit as st
from utils.components import render_topic_header, render_topic_tabs
from utils.data import TOPIC_DATA
from utils.pandas_topic import PANDAS_DATA_HANDLING_TOPIC

TOPIC_DATA["pandas_data_handling"] = PANDAS_DATA_HANDLING_TOPIC
topic = PANDAS_DATA_HANDLING_TOPIC
render_topic_header(topic)
render_topic_tabs(topic)
