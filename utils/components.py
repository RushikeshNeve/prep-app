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
    "completed_days": set(),
    "checked_tasks": set(),
    "daily_notes": {},
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
            "Global search",
            value=st.session_state.get("search_text", ""),
            placeholder="Search topics or questions",
        )
        st.session_state["revision_mode"] = st.toggle("Revision mode", value=st.session_state["revision_mode"])
        st.session_state["interview_mode"] = st.toggle("Interview mode", value=st.session_state["interview_mode"])

        col1, col2 = st.columns(2)
        if col1.button("Reset progress", use_container_width=True):
            st.session_state["completed_topics"] = set()
            st.session_state["bookmarks"] = set()
            st.session_state["quiz_scores"] = {}
            st.toast("Progress reset.")

        export_notes = "\n\n".join(
            [f"# {TOPIC_DATA[k].title}\n{v}" for k, v in st.session_state["notes"].items() if v.strip()]
        )
        col2.download_button(
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
    if topic.key == "python":
        _render_python_header(topic)
        return
    if topic.key == "generative_ai":
        _render_generative_ai_header(topic)
        return
    if topic.key == "prompt_engineering":
        _render_prompt_engineering_header(topic)
        return
    if topic.key == "agentic_ai":
        _render_agentic_ai_header(topic)
        return
    if topic.key == "apis_backend":
        _render_apis_backend_header(topic)
        return
    if topic.key == "pandas_data_handling":
        _render_pandas_data_header(topic)
        return
    if topic.key == "databases":
        _render_databases_header(topic)
        return
    if topic.key == "ai_workflows":
        _render_ai_workflows_header(topic)
        return

    st.title(f"{topic.icon} {topic.title}")
    st.markdown(
        f"<span class='badge pill-success'>Difficulty: {topic.difficulty}</span>"
        f"<span class='badge pill-warning'>Priority: {topic.priority}</span>",
        unsafe_allow_html=True,
    )
    st.caption(f"Estimated study time: **{topic.estimated_time}**")
    _render_topic_actions(topic)


def _render_python_header(topic: TopicContent) -> None:
    st.title("Python Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why Python matters for this role: Python powers AI experimentation, prompt workflows, Pandas/NumPy data handling, "
        "backend automation, and API integrations for the Movate AI Engineer role."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    _render_topic_actions(topic)


def _render_generative_ai_header(topic: TopicContent) -> None:
    st.title("Generative AI Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why Generative AI matters for this role: enterprise AI products, prompt-based apps, copilots, agentic workflows, "
        "automation, and knowledge work all depend on strong GenAI fundamentals."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    _render_topic_actions(topic)


def _render_prompt_engineering_header(topic: TopicContent) -> None:
    st.title("Prompt Engineering Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: prompt design directly affects accuracy, hallucination control, "
        "workflow automation, knowledge assistants, enterprise copilots, and output standardization."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    _render_topic_actions(topic)


def _render_agentic_ai_header(topic: TopicContent) -> None:
    st.title("Agentic AI Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: agentic workflows, tool-based systems, enterprise automation, "
        "task orchestration, copilots, and AI productivity tools all depend on understanding how agents plan and act."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    render_flow_diagram(
        "Intro flow",
        "User Goal -> AI decides steps -> uses tools -> collects results -> returns final response",
    )

    _render_topic_actions(topic)


def _render_apis_backend_header(topic: TopicContent) -> None:
    st.title("APIs and Backend Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: AI apps call APIs, tool and agent workflows depend on APIs, "
        "backend services connect models and databases, and enterprise automation needs reliable backend systems."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    render_flow_diagram(
        "Intro flow",
        "User/App -> Backend/API -> Business Logic -> Database/Model/External Service -> Response",
    )

    _render_topic_actions(topic)


def _render_pandas_data_header(topic: TopicContent) -> None:
    st.title("Pandas and Data Handling Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: AI workflows need clean and structured data, enterprise CSV and Excel data often needs "
        "cleanup, prompt workflows depend on organized inputs, and experimentation or evaluation is only useful when the data is usable."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    render_flow_diagram(
        "Intro flow",
        "Raw Data -> Load -> Clean -> Transform -> Analyze -> Use in App / AI Workflow",
    )

    _render_topic_actions(topic)


def _render_databases_header(topic: TopicContent) -> None:
    st.title("Databases and Vector Databases Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: enterprise systems depend on databases for reliable storage and retrieval, backend services use "
        "SQL and NoSQL stores, and modern AI applications use vector databases for semantic search, retrieval, and RAG."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    render_flow_diagram(
        "Intro flow",
        "User -> Backend -> Database -> Backend -> User",
    )

    _render_topic_actions(topic)


def _render_ai_workflows_header(topic: TopicContent) -> None:
    st.title("AI Workflows Interview Study Module")
    meta_cols = st.columns(4)
    meta_cols[0].metric("Difficulty", topic.difficulty)
    meta_cols[1].metric("Priority", topic.priority)
    meta_cols[2].metric("Movate importance", topic.importance_for_movate or topic.priority)
    meta_cols[3].metric("Study time", topic.estimated_time)

    st.info(
        "Why this matters for Movate AI Engineer: real AI products combine prompts, data, APIs, retrieval, tools, validation, logging, and evaluation. "
        "AI Engineers build these workflows end to end and keep improving them."
    )

    with st.container(border=True):
        st.markdown("### Role fit")
        for item in topic.role_relevance:
            st.write(f"- {item}")

    render_flow_diagram(
        "Intro flow",
        "User Need -> Data/Input -> AI Processing -> Output -> Evaluation -> Improvement",
    )

    _render_topic_actions(topic)


def _render_topic_actions(topic: TopicContent) -> None:
    col1, col2 = st.columns([1, 1])
    done = topic.key in st.session_state["completed_topics"]
    if col1.checkbox("Mark topic as completed", value=done, key=f"complete_{topic.key}"):
        st.session_state["completed_topics"].add(topic.key)
    else:
        st.session_state["completed_topics"].discard(topic.key)

    if col2.button("Bookmark this topic", key=f"bookmark_{topic.key}", use_container_width=True):
        st.session_state["bookmarks"].add(topic.key)
        st.toast(f"Bookmarked: {topic.title}")


def render_topic_tabs(topic: TopicContent) -> None:
    if st.session_state["revision_mode"]:
        render_revision_points(topic)
        return
    if st.session_state["interview_mode"]:
        render_interview_mode(topic)
        return

    if topic.key == "python":
        tabs = st.tabs(["Learn", "Patterns", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_python_learn_tab(topic)
        with tabs[1]:
            render_pattern_cards(topic)
        with tabs[2]:
            render_interview_questions(topic)
        with tabs[3]:
            render_quiz(topic)
        with tabs[4]:
            render_resources(topic)
        with tabs[5]:
            render_notes_box(topic)
        return

    if topic.key == "generative_ai":
        tabs = st.tabs(["Learn", "Use Cases", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_generative_ai_learn_tab(topic)
        with tabs[1]:
            render_use_case_cards(topic)
        with tabs[2]:
            render_topic_interview_questions(topic, heading="Most likely Generative AI interview questions")
        with tabs[3]:
            render_quiz(topic)
        with tabs[4]:
            render_resources(topic)
        with tabs[5]:
            render_notes_box(topic)
        return

    if topic.key == "prompt_engineering":
        tabs = st.tabs(["Learn", "Techniques", "Examples", "Debugging", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_prompt_engineering_learn_tab(topic)
        with tabs[1]:
            render_technique_cards(topic)
        with tabs[2]:
            render_worked_examples(topic)
        with tabs[3]:
            render_debugging_sections(topic)
        with tabs[4]:
            render_topic_interview_questions(topic, heading="Most likely Prompt Engineering interview questions")
        with tabs[5]:
            render_quiz(topic)
        with tabs[6]:
            render_resources(topic)
        with tabs[7]:
            render_notes_box(topic)
        return

    if topic.key == "agentic_ai":
        tabs = st.tabs(["Learn", "Architectures", "Workflows", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_agentic_ai_learn_tab(topic)
        with tabs[1]:
            render_architecture_cards(topic)
        with tabs[2]:
            render_workflow_cards(topic)
        with tabs[3]:
            render_topic_interview_questions(topic, heading="Most likely Agentic AI interview questions")
        with tabs[4]:
            render_quiz(topic)
        with tabs[5]:
            render_resources(topic)
        with tabs[6]:
            render_notes_box(topic)
        return

    if topic.key == "apis_backend":
        tabs = st.tabs(["Learn", "REST & CRUD", "AI App Integration", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_apis_backend_learn_tab(topic)
        with tabs[1]:
            render_rest_examples(topic)
        with tabs[2]:
            render_ai_integration_cards(topic)
        with tabs[3]:
            render_topic_interview_questions(topic, heading="Most likely APIs and Backend interview questions")
        with tabs[4]:
            render_quiz(topic)
        with tabs[5]:
            render_resources(topic)
        with tabs[6]:
            render_notes_box(topic)
        return

    if topic.key == "pandas_data_handling":
        tabs = st.tabs(["Learn", "Pandas Operations", "Data Cleaning", "AI Workflow Context", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_pandas_data_learn_tab(topic)
        with tabs[1]:
            render_operations_cards(topic)
        with tabs[2]:
            render_cleaning_cards(topic)
        with tabs[3]:
            render_ai_workflow_cards(topic)
        with tabs[4]:
            render_topic_interview_questions(topic, heading="Most likely Pandas and Data Handling interview questions")
        with tabs[5]:
            render_quiz(topic)
        with tabs[6]:
            render_resources(topic)
        with tabs[7]:
            render_notes_box(topic)
        return

    if topic.key == "databases":
        tabs = st.tabs(["Learn (SQL + NoSQL)", "SQL Concepts", "NoSQL Concepts", "Vector Databases", "AI Use Cases", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_databases_learn_tab(topic)
        with tabs[1]:
            render_sql_concepts(topic)
        with tabs[2]:
            render_nosql_concepts(topic)
        with tabs[3]:
            render_vector_db_concepts(topic)
        with tabs[4]:
            render_database_ai_use_cases(topic)
        with tabs[5]:
            render_topic_interview_questions(topic, heading="Most likely Databases and Vector DB interview questions")
        with tabs[6]:
            render_quiz(topic)
        with tabs[7]:
            render_resources(topic)
        with tabs[8]:
            render_notes_box(topic)
        return

    if topic.key == "ai_workflows":
        tabs = st.tabs(["Learn", "Workflow Types", "System Design View", "Evaluation & Iteration", "Interview", "Quiz", "Resources", "Notes"])
        with tabs[0]:
            render_ai_workflows_learn_tab(topic)
        with tabs[1]:
            render_workflow_type_cards(topic)
        with tabs[2]:
            render_system_design_cards(topic)
        with tabs[3]:
            render_evaluation_cards(topic)
        with tabs[4]:
            render_topic_interview_questions(topic, heading="Most likely AI Workflows interview questions")
        with tabs[5]:
            render_quiz(topic)
        with tabs[6]:
            render_resources(topic)
        with tabs[7]:
            render_notes_box(topic)
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
        render_revision_points(topic)
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
        render_notes_box(topic)


def render_python_learn_tab(topic: TopicContent) -> None:
    st.markdown("### Why Python matters")
    st.write(topic.why_it_matters)
    st.success("Study this page like a mini module: learn concepts, revise patterns, then switch to interview mode for quick speaking practice.")

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)


def render_generative_ai_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What Generative AI means")
    st.write(topic.why_it_matters)
    st.success("Study flow: understand the foundations, connect them to real enterprise use cases, then switch to interview mode for short speaking-ready answers.")

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_prompt_engineering_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What Prompt Engineering means")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: learn prompt anatomy, understand techniques, practice with examples, debug bad prompts, then switch to interview mode for short answers."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_agentic_ai_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What Agentic AI means")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: learn what makes a system agentic, understand tools, memory, planning, and orchestration, then use the architecture and workflow tabs to build intuition."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_apis_backend_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What backend and APIs mean")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: learn backend basics, understand request-response and REST, connect the ideas to AI systems, then revise through interview mode and the dedicated tabs."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_pandas_data_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What data handling means")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: learn what data handling means, understand common Pandas operations, practice cleaning messy data, then connect it to AI workflows and interviews."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_databases_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What databases mean")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: understand what databases do, separate SQL from NoSQL, spend extra time on vector databases, then connect everything to RAG and AI application design."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_ai_workflows_learn_tab(topic: TopicContent) -> None:
    st.markdown("### What AI workflows mean")
    st.write(topic.why_it_matters)
    st.success(
        "Study flow: learn the core workflow blocks, understand common workflow types, see how systems are designed, then focus on evaluation and iteration because real AI products improve over time."
    )

    if topic.learning_objectives:
        st.markdown("### What you should get from this page")
        for item in topic.learning_objectives:
            st.write(f"- {item}")

    render_section_expanders(topic)

    st.markdown("### Quick revision")
    render_revision_points(topic, use_expander=False)

    st.markdown("### Common mistakes candidates make")
    for item in topic.common_mistakes:
        st.warning(item)


def render_section_expanders(topic: TopicContent) -> None:
    for section in topic.learn_sections:
        with st.expander(section["title"], expanded=False):
            if section.get("summary"):
                st.markdown(section["summary"])

            for callout in section.get("callouts", []):
                _render_callout(callout["type"], callout["text"])

            for point in section.get("points", []):
                st.write(f"- {point}")

            for subtopic in section.get("subtopics", []):
                st.markdown(f"#### {subtopic['title']}")
                for line in subtopic.get("content", []):
                    st.write(f"- {line}")
                if subtopic.get("code"):
                    st.code(subtopic["code"], language="python")

            for table in section.get("tables", []):
                st.markdown(f"#### {table['title']}")
                st.markdown(table["markdown"])

            if section.get("diagram"):
                render_flow_diagram("Flow diagram", section["diagram"])

            for example in section.get("examples", []):
                st.markdown(f"#### {example['label']}")
                st.code(example["code"], language=example.get("language", "python"))

            if section.get("interview_questions"):
                st.markdown("#### Simple interview prompts")
                for question in section["interview_questions"]:
                    st.write(f"- {question}")

            if section.get("notes"):
                st.markdown("#### Key notes")
                for note in section["notes"]:
                    st.write(f"- {note}")

            if section.get("mistakes"):
                st.markdown("#### Common mistakes")
                for mistake in section["mistakes"]:
                    st.write(f"- {mistake}")


def render_pattern_cards(topic: TopicContent) -> None:
    st.markdown("### Python coding patterns")
    st.caption("These are high-frequency campus interview patterns. Learn the intuition before memorizing the code.")
    for pattern in topic.patterns:
        with st.expander(pattern["title"], expanded=False):
            st.markdown(f"**Problem statement:** {pattern['problem']}")
            st.markdown(f"**Intuition:** {pattern['intuition']}")
            st.markdown("**Clean Python solution**")
            st.code(pattern["solution"], language="python")
            if pattern.get("alternative"):
                st.markdown("**Alternative solution**")
                st.code(pattern["alternative"], language="python")
            st.markdown(f"**Time complexity:** {pattern['time_complexity']}")
            st.markdown(f"**Likely interview variation:** {pattern['variation']}")
            if pattern.get("mistakes"):
                st.markdown("**Common mistakes**")
                for item in pattern["mistakes"]:
                    st.write(f"- {item}")


def render_use_case_cards(topic: TopicContent) -> None:
    st.markdown("### Practical Generative AI use cases")
    st.caption("These examples help connect concepts with real AI Engineer work in enterprise settings.")
    for use_case in topic.use_cases:
        with st.expander(use_case["title"], expanded=False):
            st.markdown(f"**What it does:** {use_case['what_it_does']}")
            st.markdown(f"**Why businesses use it:** {use_case['why_businesses_use_it']}")
            st.markdown("**Simple architecture idea**")
            st.code(use_case["architecture"], language="text")
            st.markdown(f"**Possible risks or challenges:** {use_case['risks']}")

    if topic.key == "generative_ai":
        st.markdown("### Where Generative AI is not enough by itself")
        st.warning(
            "Many production systems still need databases, rule engines, search layers, human approvals, and deterministic workflows. "
            "A language model is often one part of the system, not the whole system."
        )
        st.write("- Databases are needed for trusted structured data and transactions.")
        st.write("- Rule engines are needed when policy or compliance must be exact.")
        st.write("- Search systems are needed when the answer should come from known documents.")
        st.write("- Human approvals are needed for sensitive business actions.")
        st.write("- Deterministic workflows are needed when outcomes must be repeatable.")


def render_technique_cards(topic: TopicContent) -> None:
    st.markdown("### Prompt engineering techniques")
    st.caption("These are the practical levers AI Engineers use to improve output quality systematically.")
    for technique in topic.techniques:
        with st.expander(technique["title"], expanded=False):
            st.markdown(f"**What it is:** {technique['what_it_is']}")
            st.markdown(f"**Why it helps:** {technique['why_it_helps']}")
            if technique.get("when_to_use"):
                st.markdown(f"**When to use it:** {technique['when_to_use']}")
            if technique.get("prompt"):
                st.markdown("**Example prompt**")
                st.code(technique["prompt"], language="text")
            if technique.get("mistakes"):
                st.markdown("**Common mistakes**")
                for item in technique["mistakes"]:
                    st.write(f"- {item}")


def render_worked_examples(topic: TopicContent) -> None:
    st.markdown("### Practical prompt examples")
    st.caption("These examples show how prompts improve when you make them more specific, structured, and workflow-aware.")
    for example in topic.worked_examples:
        with st.expander(example["title"], expanded=False):
            st.markdown(f"**Problem:** {example['problem']}")
            if example.get("bad_prompt"):
                st.markdown("**Weak prompt**")
                st.code(example["bad_prompt"], language="text")
            if example.get("better_prompt"):
                st.markdown("**Better prompt**")
                st.code(example["better_prompt"], language="text")
            if example.get("why_better"):
                st.markdown(f"**Why this is better:** {example['why_better']}")
            if example.get("workflow"):
                st.markdown("**Workflow view**")
                st.code(example["workflow"], language="text")


def render_debugging_sections(topic: TopicContent) -> None:
    st.markdown("### Prompt debugging and optimization")
    st.caption("Treat prompts like something you test and improve, not magic text you write once.")
    for section in topic.debugging_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(f"**Problem pattern:** {section['problem']}")
            st.markdown(f"**Why it happens:** {section['why_it_happens']}")
            st.markdown(f"**How to fix it:** {section['fix']}")
            if section.get("example"):
                st.code(section["example"], language="text")
            if section.get("checklist"):
                st.markdown("**Quick checklist**")
                for item in section["checklist"]:
                    st.write(f"- {item}")


def render_architecture_cards(topic: TopicContent) -> None:
    st.markdown("### Common agent architectures")
    st.caption("These patterns help you explain how agents are structured in real systems.")
    for architecture in topic.architectures:
        with st.expander(architecture["title"], expanded=False):
            st.markdown(f"**What it is:** {architecture['what_it_is']}")
            st.markdown(f"**When to use it:** {architecture['when_to_use']}")
            render_flow_diagram("Flow", architecture["diagram"])
            st.markdown(f"**Pros:** {architecture['pros']}")
            st.markdown(f"**Limitations:** {architecture['limitations']}")
            st.markdown(f"**Interview-ready explanation:** {architecture['interview_note']}")


def render_workflow_cards(topic: TopicContent) -> None:
    st.markdown("### Practical agentic workflows")
    st.caption("These examples connect agent ideas with enterprise AI Engineer tasks.")
    for workflow in topic.workflows:
        with st.expander(workflow["title"], expanded=False):
            st.markdown(f"**Business purpose:** {workflow['business_purpose']}")
            st.markdown("**Flow diagram**")
            render_flow_diagram(workflow["title"], workflow["diagram"])
            st.markdown("**Step-by-step explanation**")
            for step in workflow["steps"]:
                st.write(f"- {step}")
            st.markdown(f"**Tools involved:** {workflow['tools_involved']}")
            st.markdown(f"**Risks / challenges:** {workflow['risks']}")
            st.markdown(f"**Why agentic AI helps:** {workflow['why_agentic_ai_helps']}")

    if topic.key == "agentic_ai":
        st.markdown("### When not to use an agent")
        st.warning("Not every workflow needs an agent. In some cases, simple automation or deterministic rules are better.")
        st.write("- Use rule-based automation when steps are simple, fixed, and fully predictable.")
        st.write("- Prefer deterministic workflows when compliance or exact reproducibility is critical.")
        st.write("- Avoid agents when latency or cost is too high for the business need.")
        st.write("- Add human approvals when the workflow has high compliance or business risk.")


def render_rest_examples(topic: TopicContent) -> None:
    st.markdown("### REST and CRUD fundamentals")
    st.caption("This section focuses on resource-based API design, method mapping, and practical request-response examples.")
    for section in topic.rest_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(section["summary"])
            for point in section.get("points", []):
                st.write(f"- {point}")
            if section.get("table"):
                st.markdown(section["table"])
            if section.get("diagram"):
                render_flow_diagram("Flow", section["diagram"])
            for example in section.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language="text")


def render_ai_integration_cards(topic: TopicContent) -> None:
    st.markdown("### AI app integration examples")
    st.caption("These examples connect backend and API concepts directly to AI Engineer workflows.")
    for item in topic.ai_integration_examples:
        with st.expander(item["title"], expanded=False):
            st.markdown(f"**Business purpose:** {item['business_purpose']}")
            render_flow_diagram(item["title"], item["diagram"])
            st.markdown("**Backend responsibilities**")
            for point in item["backend_responsibilities"]:
                st.write(f"- {point}")
            st.markdown(f"**APIs involved:** {item['apis_involved']}")
            st.markdown(f"**Risks / challenges:** {item['risks']}")
            st.markdown(f"**Why backend matters:** {item['why_backend_matters']}")

    if topic.key == "apis_backend":
        st.markdown("### When simple API integration is enough vs when full backend orchestration is needed")
        st.info("Simple API integration is enough when the workflow is short and deterministic. Full backend orchestration is needed when validation, retries, auth, retrieval, logging, or multi-step business logic are involved.")
        st.write("- Simple integration: one frontend request calls one known service and returns one response.")
        st.write("- Full backend orchestration: multiple services, model calls, DB reads, validation, retries, and workflow control are needed.")


def render_operations_cards(topic: TopicContent) -> None:
    st.markdown("### Most-used Pandas operations")
    st.caption("These are the operations interviewers expect you to recognize quickly and explain with simple examples.")
    for operation in topic.operations:
        with st.expander(operation["title"], expanded=False):
            st.markdown(f"**What it does:** {operation['what_it_does']}")
            st.markdown("**Syntax**")
            st.code(operation["syntax"], language="python")
            st.markdown("**Example**")
            st.code(operation["example"], language="python")
            st.markdown(f"**Common mistake:** {operation['common_mistake']}")
            st.markdown(f"**Interview tip:** {operation['interview_tip']}")

    if topic.key == "pandas_data_handling":
        st.markdown("### Mini cheat sheet")
        st.code(
            "\n".join(
                [
                    "pd.read_csv('file.csv')",
                    "df.head()",
                    "df.info()",
                    "df.describe()",
                    "df['col']",
                    "df[['a', 'b']]",
                    "df[df['score'] > 50]",
                    "df.loc[rows, cols]",
                    "df.iloc[row_positions, col_positions]",
                    "df['total'] = df['price'] * df['qty']",
                    "df.rename(columns={'old': 'new'})",
                    "df.drop(columns=['unused'])",
                    "df.sort_values('score', ascending=False)",
                    "df.groupby('category')['sales'].sum()",
                    "df.isnull().sum()",
                    "df.fillna(0)",
                    "df.drop_duplicates()",
                    "df.to_csv('cleaned.csv', index=False)",
                ]
            ),
            language="python",
        )


def render_cleaning_cards(topic: TopicContent) -> None:
    st.markdown("### Real-world data cleaning")
    st.caption("Good AI and analytics work starts with checking what is broken or inconsistent in the data before modeling or reporting.")
    for section in topic.cleaning_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(f"**What the problem looks like:** {section['problem']}")
            st.markdown(f"**How to detect it:** {section['detect']}")
            st.markdown(f"**How to fix it:** {section['fix']}")
            st.markdown(f"**Why it matters:** {section['why_it_matters']}")
            if section.get("example"):
                st.code(section["example"], language=section.get("language", "python"))
            if section.get("diagram"):
                render_flow_diagram("Flow", section["diagram"])

    if topic.key == "pandas_data_handling":
        st.markdown("### Cleaning strategy depends on business context")
        st.info(
            "There is no one correct cleaning strategy. Sometimes you drop rows, sometimes you fill values, and sometimes you go back to the data source because the issue indicates a business or collection problem."
        )
        st.write("- Dropping missing rows may be fine when only a tiny fraction is affected.")
        st.write("- Filling values may be better when the field is important and a reasonable default exists.")
        st.write("- Data issues can signal upstream collection problems, so sometimes the right step is to fix the source process.")


def render_ai_workflow_cards(topic: TopicContent) -> None:
    st.markdown("### Data handling in AI workflows")
    st.caption("These examples connect Pandas and data cleaning directly to AI Engineer tasks and backend pipelines.")
    for item in topic.ai_workflow_examples:
        with st.expander(item["title"], expanded=False):
            st.markdown(f"**Business purpose:** {item['business_purpose']}")
            render_flow_diagram(item["title"], item["diagram"])
            st.markdown("**Data handling responsibilities**")
            for point in item["data_handling_responsibilities"]:
                st.write(f"- {point}")
            st.markdown(f"**Why Pandas helps:** {item['why_pandas_helps']}")
            st.markdown(f"**Risks / challenges:** {item['risks']}")

    if topic.key == "pandas_data_handling":
        st.markdown("### When Pandas is enough vs when a full data pipeline is needed")
        st.info("Pandas is great for local analysis, quick cleaning, prototyping, and moderate-size structured data. A larger production workflow may need scheduled pipelines, databases, validation services, or distributed processing.")
        st.write("- Pandas is enough when the dataset is manageable and the workflow is exploratory or moderately sized.")
        st.write("- A fuller pipeline is needed when data is very large, highly frequent, shared across systems, or needs strong automation and monitoring.")


def render_sql_concepts(topic: TopicContent) -> None:
    st.markdown("### SQL concepts")
    st.caption("These are the highest-value relational database basics for interviews and backend work.")
    for section in topic.sql_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(section["summary"])
            for point in section.get("points", []):
                st.write(f"- {point}")
            if section.get("table"):
                st.markdown(section["table"])
            if section.get("diagram"):
                render_flow_diagram("Flow", section["diagram"])
            for example in section.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "sql"))


def render_nosql_concepts(topic: TopicContent) -> None:
    st.markdown("### NoSQL concepts")
    st.caption("Focus on flexible schema, common use cases, and how NoSQL differs from relational systems.")
    for section in topic.nosql_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(section["summary"])
            for point in section.get("points", []):
                st.write(f"- {point}")
            if section.get("table"):
                st.markdown(section["table"])
            if section.get("diagram"):
                render_flow_diagram("Flow", section["diagram"])
            for example in section.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "text"))


def render_vector_db_concepts(topic: TopicContent) -> None:
    st.markdown("### Vector databases")
    st.caption("This is the most important part for modern AI roles because retrieval, semantic search, and RAG depend on it.")
    for section in topic.vector_db_sections:
        with st.expander(section["title"], expanded=False):
            st.markdown(section["summary"])
            for callout in section.get("callouts", []):
                _render_callout(callout["type"], callout["text"])
            for point in section.get("points", []):
                st.write(f"- {point}")
            if section.get("table"):
                st.markdown(section["table"])
            if section.get("diagram"):
                render_flow_diagram("Flow", section["diagram"])
            for example in section.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "text"))


def render_database_ai_use_cases(topic: TopicContent) -> None:
    st.markdown("### AI and database use cases")
    st.caption("These examples connect backend databases and vector retrieval directly to AI Engineer work.")
    for item in topic.ai_use_cases:
        with st.expander(item["title"], expanded=False):
            st.markdown(f"**Business purpose:** {item['business_purpose']}")
            render_flow_diagram(item["title"], item["diagram"])
            st.markdown("**System responsibilities**")
            for point in item["responsibilities"]:
                st.write(f"- {point}")
            st.markdown(f"**Why this architecture helps:** {item['why_it_helps']}")
            st.markdown(f"**Risks / challenges:** {item['risks']}")


def render_workflow_type_cards(topic: TopicContent) -> None:
    st.markdown("### Common workflow types")
    st.caption("These patterns help you explain how AI systems differ depending on complexity, grounding, and tool use.")
    for item in topic.workflow_types:
        with st.expander(item["title"], expanded=False):
            st.markdown(item["summary"])
            for point in item.get("points", []):
                st.write(f"- {point}")
            if item.get("table"):
                st.markdown(item["table"])
            if item.get("diagram"):
                render_flow_diagram("Flow", item["diagram"])
            for example in item.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "text"))


def render_system_design_cards(topic: TopicContent) -> None:
    st.markdown("### System design view")
    st.caption("These sections help you explain AI systems as connected components, not just model calls.")
    for item in topic.system_design_sections:
        with st.expander(item["title"], expanded=False):
            st.markdown(item["summary"])
            for point in item.get("points", []):
                st.write(f"- {point}")
            if item.get("diagram"):
                render_flow_diagram("Architecture", item["diagram"])
            for example in item.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "text"))


def render_evaluation_cards(topic: TopicContent) -> None:
    st.markdown("### Evaluation and iteration")
    st.caption("A strong AI Engineer answer includes how the system is measured, improved, and monitored after the first version works.")
    for item in topic.evaluation_sections:
        with st.expander(item["title"], expanded=False):
            st.markdown(item["summary"])
            for point in item.get("points", []):
                st.write(f"- {point}")
            if item.get("diagram"):
                render_flow_diagram("Flow", item["diagram"])
            for example in item.get("examples", []):
                st.markdown(f"**{example['label']}**")
                st.code(example["code"], language=example.get("language", "text"))


def render_interview(topic: TopicContent) -> None:
    st.subheader("Most likely interview questions")
    for qa in topic.interview_questions:
        with st.expander(qa["q"]):
            st.write(qa["a"])


def render_interview_questions(topic: TopicContent) -> None:
    st.markdown("### Most likely Python interview questions")
    for qa in topic.interview_questions_detailed:
        with st.expander(qa["question"], expanded=False):
            st.markdown("**Short answer**")
            st.write(qa["short_answer"])
            st.markdown("**Expanded answer for speaking**")
            st.write(qa["spoken_answer"])

    st.markdown("### Rapid fire revision")
    for item in topic.interview_rapid_fire:
        st.write(f"- **{item['question']}** {item['answer']}")

    st.markdown("### Common mistakes candidates make")
    for item in topic.interview_common_mistakes:
        st.warning(item)


def render_topic_interview_questions(topic: TopicContent, heading: str | None = None) -> None:
    st.markdown(f"### {heading or 'Most likely interview questions'}")
    for qa in topic.interview_questions_detailed:
        with st.expander(qa["question"], expanded=False):
            st.markdown("**Short answer**")
            st.write(qa["short_answer"])
            st.markdown("**Expanded answer for speaking**")
            st.write(qa["spoken_answer"])

    if topic.interview_scenarios:
        st.markdown("### Real interview scenario answers")
        for scenario in topic.interview_scenarios:
            with st.expander(scenario["question"], expanded=False):
                if scenario.get("approach"):
                    st.markdown(f"**How to structure your answer:** {scenario['approach']}")
                for point in scenario.get("answer_points", []):
                    st.write(f"- {point}")
                if scenario.get("diagram"):
                    render_flow_diagram("Suggested flow", scenario["diagram"])

    if topic.interview_rapid_fire:
        st.markdown("### Rapid revision")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")

    if topic.interview_common_mistakes:
        st.markdown("### Common mistakes candidates make")
        for item in topic.interview_common_mistakes:
            st.warning(item)


def render_flow_diagram(title: str, diagram_text: str) -> None:
    st.markdown(f"**{title}**")
    st.code(diagram_text, language="text")


def render_interview_mode(topic: TopicContent) -> None:
    st.subheader("Interview mode")
    st.info("This view hides the long learning content and focuses on likely questions with short speaking-ready answers.")

    if topic.key == "python":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "generative_ai":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "prompt_engineering":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "agentic_ai":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "apis_backend":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "pandas_data_handling":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "databases":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    if topic.key == "ai_workflows":
        for qa in topic.interview_questions_detailed:
            with st.expander(qa["question"], expanded=False):
                st.write(qa["short_answer"])
        st.markdown("### Rapid fire")
        for item in topic.interview_rapid_fire:
            st.write(f"- **{item['question']}** {item['answer']}")
        return

    render_interview(topic)


def render_revision_points(topic: TopicContent, use_expander: bool = True) -> None:
    if use_expander:
        with st.expander("Revision mode summary", expanded=True):
            for idx, point in enumerate(topic.quick_revision_points, start=1):
                st.write(f"{idx}. {point}")
        return

    for idx, point in enumerate(topic.quick_revision_points, start=1):
        st.write(f"{idx}. {point}")


def render_quiz(topic: TopicContent) -> None:
    question_count = len(topic.quiz_questions)
    st.caption(f"Quiz: {question_count} MCQs. Best score is saved.")
    choices = []
    for i, q in enumerate(topic.quiz_questions):
        answer = st.radio(q.question, q.options, index=None, key=f"quiz_{topic.key}_{i}")
        choices.append(q.options.index(answer) if answer is not None else -1)

    if st.button("Submit quiz", key=f"submit_{topic.key}"):
        score, total, flags = evaluate_quiz(topic, choices)
        update_best_score(st.session_state, topic.key, score, total)
        st.success(f"Score: {score}/{total}. Best: {st.session_state['quiz_scores'][topic.key]}%")
        for index, ok in enumerate(flags):
            question = topic.quiz_questions[index]
            status = "Correct" if ok else "Incorrect"
            correct_answer = question.options[question.answer_index]
            st.write(f"**Q{index + 1} - {status}**")
            st.write(f"Correct answer: {correct_answer}")
            st.write(question.explanation)


def render_resources(topic: TopicContent) -> None:
    if topic.resource_sections:
        for section_name, items in topic.resource_sections.items():
            st.markdown(f"### {section_name}")
            for item in items:
                with st.container(border=True):
                    st.markdown(f"**[{item.title}]({item.url})**")
                    st.caption(f"{item.kind.title()} | {item.tier.replace('_', ' ')}")
                    if item.description:
                        st.write(item.description)
        return

    st.subheader("Useful resources")
    for item in topic.resources:
        with st.container(border=True):
            st.markdown(f"**[{item.title}]({item.url})**")
            if item.description:
                st.write(item.description)


def render_notes_box(topic: TopicContent) -> None:
    st.markdown("### Personal notes")
    note_key = f"notes_{topic.key}"
    existing = st.session_state["notes"].get(topic.key, "")
    text = st.text_area(
        "Write your own summary, doubts, or interview answers here.",
        value=existing,
        key=note_key,
        height=260,
    )
    st.session_state["notes"][topic.key] = text

    export_text = text if text.strip() else f"No notes saved for {topic.title}."
    col1, col2 = st.columns(2)
    if col1.button("Save notes", key=f"save_notes_{topic.key}", use_container_width=True):
        st.success("Notes saved in session state.")
    col2.download_button(
        "Export notes",
        data=export_text,
        file_name=f"{topic.key}_notes.md",
        mime="text/markdown",
        use_container_width=True,
        key=f"export_notes_{topic.key}",
    )


def render_timetable_header(timetable: dict) -> None:
    st.title("5-Day Timetable")
    st.caption("Movate AI Engineer Preparation Plan")
    st.info(
        "This is a focused 5-day preparation dashboard for the Movate AI Engineer role. It is designed to help you cover the highest-value topics in a realistic order and keep execution visible every day."
    )

    days = timetable["days"]
    completed_days = st.session_state.get("completed_days", set())
    checked_tasks = st.session_state.get("checked_tasks", set())
    total_tasks = sum(len(day["checklist"]) for day in days)
    completed_tasks = sum(1 for day in days for item in day["checklist"] if f"{day['day']}::{item}" in checked_tasks)
    high_priority_topics = timetable["overview"]["high_priority_topics"]
    covered_high_priority = sum(
        1
        for topic_name in high_priority_topics
        if any(day["day"] in completed_days and topic_name in day["covered_topics"] for day in days)
    )
    progress = completed_tasks / total_tasks if total_tasks else 0

    metric_cols = st.columns(4)
    metric_cols[0].metric("Days Completed", f"{len(completed_days)}/5")
    metric_cols[1].metric("Tasks Completed", f"{completed_tasks}/{total_tasks}")
    metric_cols[2].metric("High Priority Covered", f"{covered_high_priority}/{len(high_priority_topics)}")
    metric_cols[3].metric("Execution Progress", f"{round(progress * 100)}%")
    st.progress(progress)


def render_study_block(label: str, time_range: str, items: list[str], compact: bool = False) -> None:
    with st.container(border=True):
        st.markdown(f"### {label}")
        st.caption(time_range)
        if compact:
            st.write(", ".join(items))
        else:
            for item in items:
                st.write(f"- {item}")


def render_checklist(day: dict) -> None:
    st.markdown("### Daily checklist")
    for task in day["checklist"]:
        task_key = f"{day['day']}::{task}"
        checked = task_key in st.session_state["checked_tasks"]
        value = st.checkbox(task, value=checked, key=f"task_{task_key}")
        if value:
            st.session_state["checked_tasks"].add(task_key)
        else:
            st.session_state["checked_tasks"].discard(task_key)


def render_day_notes(day: dict) -> None:
    st.markdown("### Day notes")
    existing = st.session_state["daily_notes"].get(day["day"], "")
    text = st.text_area(
        f"Notes for {day['day']}",
        value=existing,
        key=f"day_notes_{day['day']}",
        height=180,
    )
    st.session_state["daily_notes"][day["day"]] = text
    export_text = text if text.strip() else f"No notes saved for {day['day']}."
    st.download_button(
        "Export day notes",
        data=export_text,
        file_name=f"{day['day'].lower().replace(' ', '_')}_notes.md",
        mime="text/markdown",
        use_container_width=True,
        key=f"export_day_notes_{day['day']}",
    )


def render_day_completion(day: dict) -> None:
    completed = day["day"] in st.session_state["completed_days"]
    label = "Mark day complete" if not completed else "Mark day incomplete"
    if st.button(label, key=f"complete_day_{day['day']}", use_container_width=True):
        if completed:
            st.session_state["completed_days"].discard(day["day"])
        else:
            st.session_state["completed_days"].add(day["day"])
        st.rerun()


def render_day_plan_card(day: dict, compact: bool = False) -> None:
    with st.container(border=True):
        st.markdown(f"## {day['title']}")
        badges = [f"`Priority: {day['priority']}`"]
        if day.get("badge"):
            badges.append(f"`{day['badge']}`")
        st.markdown(" ".join(badges))
        st.write(day["goal"])
        if day.get("diagram"):
            render_flow_diagram("Day flow", day["diagram"])

    if compact:
        st.markdown("### What to study")
        for block_name, items in day["blocks"].items():
            st.write(f"- **{block_name.title()}**: {', '.join(items)}")
    else:
        render_study_block("Morning Block", "9:30 AM – 12:00 PM", day["blocks"]["morning"])
        render_study_block("Afternoon Block", "2:00 PM – 4:30 PM", day["blocks"]["afternoon"])
        render_study_block("Night Block", "8:00 PM – 10:30 PM", day["blocks"]["night"])

    with st.expander("Expected outcome", expanded=False):
        for item in day["expected_outcome"]:
            st.write(f"- {item}")

    with st.expander("Interview focus", expanded=False):
        for item in day["interview_focus"]:
            st.write(f"- {item}")

    render_checklist(day)
    render_day_notes(day)
    render_day_completion(day)


def render_final_revision_section(final_revision: dict, compact: bool = False) -> None:
    st.markdown("## Final Revision")
    st.info(final_revision["summary"])
    if final_revision.get("diagram"):
        render_flow_diagram("Final revision flow", final_revision["diagram"])

    sections = [
        ("1-Hour Final Revision Plan", final_revision["one_hour_plan"]),
        ("Most Important Concepts to Revise", final_revision["important_concepts"]),
        ("Most Likely Interview Questions", final_revision["top_questions"]),
        ("Final Night Strategy", final_revision["final_night_strategy"]),
        ("Confidence Reminders", final_revision["confidence_reminders"]),
    ]
    for title, items in sections:
        with st.expander(title, expanded=title == "1-Hour Final Revision Plan"):
            if compact:
                st.write(", ".join(items))
            else:
                for item in items:
                    st.write(f"- {item}")


def _render_callout(kind: str, text: str) -> None:
    if kind == "info":
        st.info(text)
    elif kind == "warning":
        st.warning(text)
    elif kind == "success":
        st.success(text)
    else:
        st.write(text)


def placement_countdown_message() -> str:
    today = date.today()
    return f"Placement prep for next week starts now - keep momentum on {today.strftime('%d %b %Y')}"
