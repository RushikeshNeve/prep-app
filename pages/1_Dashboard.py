import streamlit as st

from utils.components import completion_percent, filtered_topic_keys, placement_countdown_message
from utils.data import ALL_TOPICS_ORDER, ROLE_SUMMARY, TOPIC_DATA

st.title("🎓 Movate AI Engineer Prep App")
st.caption("A structured, interview-focused companion for campus placement preparation.")

with st.container(border=True):
    c1, c2, c3 = st.columns(3)
    c1.metric("Role", ROLE_SUMMARY["role"])
    c2.metric("Location", ROLE_SUMMARY["location"])
    c3.metric("CTC", ROLE_SUMMARY["ctc"])
    st.write("**Focus areas:** " + ", ".join(ROLE_SUMMARY["focus_areas"]))

pct = completion_percent()
st.progress(pct / 100)
st.write(f"Overall completion: **{pct}%**")

col_a, col_b = st.columns([1.6, 1])
with col_a:
    st.subheader("Topic tracker")
    for key in filtered_topic_keys():
        topic = TOPIC_DATA[key]
        done = "✅ Completed" if key in st.session_state["completed_topics"] else "🕒 Pending"
        score = st.session_state["quiz_scores"].get(key, "-")
        st.markdown(
            f"<div class='topic-card'><strong>{topic.icon} {topic.title}</strong><br/>"
            f"<span class='muted'>{done} | Best Quiz: {score}% | Time: {topic.estimated_time}</span></div>",
            unsafe_allow_html=True,
        )

with col_b:
    st.subheader("Today’s Focus")
    pending = [k for k in ALL_TOPICS_ORDER if k not in st.session_state["completed_topics"]]
    focus = pending[:3] if pending else ALL_TOPICS_ORDER[:3]
    for k in focus:
        st.write(f"- {TOPIC_DATA[k].title}")

    st.subheader("Recommended order")
    for idx, k in enumerate(ALL_TOPICS_ORDER, 1):
        st.write(f"{idx}. {TOPIC_DATA[k].title}")

    st.subheader("Weak areas")
    weak = sorted(st.session_state["quiz_scores"].items(), key=lambda x: x[1])[:3]
    if weak:
        for k, s in weak:
            st.write(f"- {TOPIC_DATA[k].title}: {s}%")
    else:
        st.write("Take a few quizzes to detect weak areas.")

st.info(placement_countdown_message())

st.subheader("Quick navigation")
nav_map = {
    "python": "pages/2_Python.py",
    "dsa": "pages/3_DSA.py",
    "generative_ai": "pages/4_Generative_AI.py",
    "prompt_engineering": "pages/5_Prompt_Engineering.py",
    "agentic_ai": "pages/6_Agentic_AI.py",
    "apis_backend": "pages/7_APIs_Backend.py",
    "pandas_data_handling": "pages/8_Pandas_Data_Handling.py",
    "databases": "pages/9_Databases.py",
    "ai_workflows": "pages/10_AI_Workflows.py",
    "interview_prep": "pages/11_Interview_Prep.py",
}
nav_cols = st.columns(5)
for i, key in enumerate(ALL_TOPICS_ORDER):
    with nav_cols[i % 5]:
        st.page_link(nav_map[key], label=TOPIC_DATA[key].title)
