import streamlit as st

from utils.components import (
    render_day_plan_card,
    render_final_revision_section,
    render_flow_diagram,
    render_timetable_header,
)
from utils.data import FIVE_DAY_TIMETABLE

timetable = FIVE_DAY_TIMETABLE
compact_view = st.toggle("Compact Revision View", value=False)

render_timetable_header(timetable)

tabs = st.tabs(["Overview", "Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Final Revision"])

with tabs[0]:
    overview = timetable["overview"]
    col1, col2 = st.columns([3, 1])
    with col1:
        with st.container(border=True):
            st.markdown("## Goal Summary")
            for item in overview["goal_summary"]:
                st.write(f"- {item}")

        with st.container(border=True):
            st.markdown("## Daily Structure")
            for item in overview["daily_structure"]:
                st.write(f"- {item}")

        with st.container(border=True):
            st.markdown("## Priority Order")
            for item in overview["priority_order"]:
                st.write(f"- {item}")

        with st.container(border=True):
            st.markdown("## Outcome Goals")
            for item in overview["outcome_goals"]:
                st.write(f"- {item}")

        render_flow_diagram("5-Day Flow", overview["flow_diagram"])

    with col2:
        st.markdown("## Focus Badges")
        st.markdown("`Very High` `GenAI`")
        st.markdown("`Very High` `Prompt Engineering`")
        st.markdown("`Very High` `Agentic AI`")
        st.markdown("`High` `Python`")
        st.markdown("`High` `APIs & Backend`")
        st.markdown("`High` `Databases / Vector DB`")
        st.markdown("`High` `Pandas / Data`")
        st.markdown("`High` `AI Workflows`")
        st.markdown("`Medium` `DSA`")

        st.warning("GenAI + Prompt Engineering + Agentic AI are strong differentiators in this drive.")
        st.info("Use the checklist in each day tab. Aim to finish the night block every day because that is where retention and interview confidence build.")
        if st.button("Reset timetable progress", use_container_width=True):
            st.session_state["completed_days"] = set()
            st.session_state["checked_tasks"] = set()
            st.session_state["daily_notes"] = {}
            st.rerun()

for index, day in enumerate(timetable["days"], start=1):
    with tabs[index]:
        render_day_plan_card(day, compact=compact_view)

with tabs[6]:
    render_final_revision_section(timetable["final_revision"], compact=compact_view)
    st.success("Final mock interview reminder: spend at least 20 to 30 minutes speaking answers aloud, not just reading notes.")
