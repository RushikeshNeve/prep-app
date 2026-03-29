# Movate AI Engineer Prep App

A production-style Streamlit study application focused on **Movate AI Engineer campus placement prep**.

## Highlights
- Multipage app using **`st.Page` + `st.navigation`**.
- Structured content loaded from `utils/data.py`.
- Dashboard with progress metrics, weak areas, and study order.
- Topic pages with:
  - Learn, Code, Interview, Quiz, Resources, Notes tabs
  - quick revision section
  - completion tracker and bookmarks
  - mini MCQ quiz with best score tracking
- Session-state powered progress, notes, bookmarks, and quiz history.
- Global search, revision mode, interview mode, reset progress, export notes.

## Project Structure

```text
streamlit_app.py
pages/
  1_Dashboard.py
  2_Python.py
  3_DSA.py
  4_Generative_AI.py
  5_Prompt_Engineering.py
  6_Agentic_AI.py
  7_APIs_Backend.py
  8_Pandas_Data_Handling.py
  9_Databases.py
  10_AI_Workflows.py
  11_Interview_Prep.py
  12_Resources.py
utils/
  data.py
  components.py
  quiz_engine.py
  styles.py
requirements.txt
README.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

## Run

```bash
streamlit run streamlit_app.py
```

## Notes
- No authentication and no database are required.
- App state is session-based via `st.session_state`.
- Optional notes export is provided as Markdown.
