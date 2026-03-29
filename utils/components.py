"""Reusable UI and state helpers."""

from __future__ import annotations

from datetime import date
import streamlit as st

from utils.data import ALL_TOPICS_ORDER, TOPIC_DATA, TopicContent
from utils.quiz_engine import evaluate_quiz, update_best_score


SESSION_DEFAULTS = {
    "completed_topics": set(),
    "bookmarks": set(),
    "notes": {},
    "quiz_scores": {},
    "revision_mode": False,
    "interview_mode": False,
    "search_text": "",
}


def init_session_state() -> None:
    for key, default in SESSION_DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default.copy() if isinstance(default, (set, dict)) else default


def render_sidebar_controls() -> None:
    with st.sidebar:
        st.subheader("Study Controls")
        st.session_state["search_text"] = st.text_input(
            "Global search", value=st.session_state.get("search_text", ""), placeholder="Search topics/questions"
        )
        st.session_state["revision_mode"] = st.toggle("Revision mode", value=st.session_state["revision_mode"])
        st.session_state["interview_mode"] = st.toggle("Interview mode", value=st.session_state["interview_mode"])

        c1, c2 = st.columns(2)
        if c1.button("Reset progress", use_container_width=True):
            st.session_state["completed_topics"] = set()
            st.session_state["bookmarks"] = set()
            st.session_state["quiz_scores"] = {}
            st.toast("Progress reset.")

        export_notes = "\n\n".join(
            [f"# {TOPIC_DATA[k].title}\n{v}" for k, v in st.session_state["notes"].items() if v.strip()]
        )
        c2.download_button(
            "Export notes",
            data=export_notes or "No notes yet.",
            file_name="movate_prep_notes.md",
            mime="text/markdown",
            use_container_width=True,
        )


def filtered_topic_keys() -> list[str]:
    query = st.session_state.get("search_text", "").strip().lower()
    if not query:
        return ALL_TOPICS_ORDER

    matched = []
    for key in ALL_TOPICS_ORDER:
        topic = TOPIC_DATA[key]
        haystack = " ".join(
            [topic.title, topic.why_it_matters]
            + list(topic.detailed_sections.keys())
            + list(topic.detailed_sections.values())
            + [q["q"] for q in topic.interview_questions]
        ).lower()
        if query in haystack:
            matched.append(key)
    return matched


def completion_percent() -> int:
    return round((len(st.session_state["completed_topics"]) / len(ALL_TOPICS_ORDER)) * 100)


def render_topic_header(topic: TopicContent) -> None:
    st.title(f"{topic.icon} {topic.title}")
    st.markdown(
        f"<span class='badge pill-success'>Difficulty: {topic.difficulty}</span>"
        f"<span class='badge pill-warning'>Priority: {topic.priority}</span>",
        unsafe_allow_html=True,
    )
    st.caption(f"Estimated study time: **{topic.estimated_time}**")

    col1, col2 = st.columns([1, 1])
    done = topic.key in st.session_state["completed_topics"]
    if col1.checkbox("Mark topic as completed", value=done, key=f"complete_{topic.key}"):
        st.session_state["completed_topics"].add(topic.key)
    else:
        st.session_state["completed_topics"].discard(topic.key)

    if col2.button("🔖 Bookmark this topic", key=f"bookmark_{topic.key}", use_container_width=True):
        st.session_state["bookmarks"].add(topic.key)
        st.toast(f"Bookmarked: {topic.title}")


def render_topic_tabs(topic: TopicContent) -> None:
    revision_mode = st.session_state["revision_mode"]
    interview_mode = st.session_state["interview_mode"]

    if revision_mode:
        render_quick_revision(topic)
        return
    if interview_mode:
        render_interview(topic)
        return

    tabs = st.tabs(["Learn", "Code", "Interview", "Quiz", "Resources", "Notes"])
    with tabs[0]:
        st.info(topic.why_it_matters)
        for section_title, section_body in topic.detailed_sections.items():
            with st.expander(section_title, expanded=False):
                st.write(section_body)
        st.subheader("Common mistakes to avoid")
        for item in topic.common_mistakes:
            st.write(f"- {item}")
        render_quick_revision(topic)

    with tabs[1]:
        for name, code in topic.code_examples.items():
            st.markdown(f"**{name}**")
            st.code(code, language="python")

    with tabs[2]:
        render_interview(topic)

    with tabs[3]:
        render_quiz(topic)

    with tabs[4]:
        render_resources(topic)

    with tabs[5]:
        notes_key = f"notes_{topic.key}"
        existing = st.session_state["notes"].get(topic.key, "")
        text = st.text_area("Personal notes", value=existing, key=notes_key, height=220)
        st.session_state["notes"][topic.key] = text


def render_interview(topic: TopicContent) -> None:
    st.subheader("Most likely interview questions")
    for qa in topic.interview_questions:
        with st.expander(qa["q"]):
            st.write(qa["a"])


def render_quick_revision(topic: TopicContent) -> None:
    with st.expander("⚡ Quick revision", expanded=True):
        for idx, point in enumerate(topic.quick_revision_points, start=1):
            st.write(f"{idx}. {point}")


def render_quiz(topic: TopicContent) -> None:
    st.caption("Mini quiz (5 MCQs). Best score is saved.")
    choices = []
    for i, q in enumerate(topic.quiz_questions):
        answer = st.radio(q.question, q.options, index=None, key=f"quiz_{topic.key}_{i}")
        choices.append(q.options.index(answer) if answer is not None else -1)

    if st.button("Submit quiz", key=f"submit_{topic.key}"):
        score, total, flags = evaluate_quiz(topic, choices)
        update_best_score(st.session_state, topic.key, score, total)
        st.success(f"You scored {score}/{total}. Best: {st.session_state['quiz_scores'][topic.key]}%")
        for i, ok in enumerate(flags):
            exp = topic.quiz_questions[i].explanation
            st.write(("✅" if ok else "❌") + f" Q{i+1}: {exp}")


def render_resources(topic: TopicContent) -> None:
    st.subheader("Useful resources")
    for res in topic.resources:
        st.markdown(f"- **{res.title}** ({res.kind}, {res.tier.replace('_', ' ')}): {res.url}")


def placement_countdown_message() -> str:
    today = date.today()
    return f"Placement prep for next week starts now — keep momentum on {today.strftime('%d %b %Y')} 🚀"
