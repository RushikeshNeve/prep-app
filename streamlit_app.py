"""Entry point using Streamlit's st.Page / st.navigation."""

import streamlit as st

from utils.components import init_session_state, render_sidebar_controls
from utils.styles import inject_styles

st.set_page_config(
    page_title="Movate AI Engineer Prep App",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_styles()
init_session_state()
render_sidebar_controls()

pages = [
    st.Page("pages/1_Dashboard.py", title="Dashboard", icon="🏠", default=True),
    st.Page("pages/2_Python.py", title="Python", icon="🐍"),
    st.Page("pages/3_DSA.py", title="DSA", icon="🧠"),
    st.Page("pages/4_Generative_AI.py", title="Generative AI", icon="✨"),
    st.Page("pages/5_Prompt_Engineering.py", title="Prompt Engineering", icon="📝"),
    st.Page("pages/6_Agentic_AI.py", title="Agentic AI", icon="🤖"),
    st.Page("pages/7_APIs_Backend.py", title="APIs & Backend", icon="🌐"),
    st.Page("pages/8_Pandas_Data_Handling.py", title="Pandas & Data", icon="📊"),
    st.Page("pages/9_Databases.py", title="Databases", icon="🗃️"),
    st.Page("pages/10_AI_Workflows.py", title="AI Workflows", icon="🔁"),
    st.Page("pages/11_Interview_Prep.py", title="Interview Prep", icon="🎯"),
    st.Page("pages/12_Resources.py", title="Resources", icon="📚"),
]

pg = st.navigation(pages, position="sidebar")
pg.run()
