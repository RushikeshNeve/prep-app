import streamlit as st

from utils.data import ALL_TOPICS_ORDER, TOPIC_DATA

st.title("📚 Consolidated Resources")
st.caption("Topic-wise curated links for fast and deep preparation.")

options = ["All"] + [TOPIC_DATA[k].title for k in ALL_TOPICS_ORDER]
selected = st.selectbox("Filter by topic", options=options)

def show_tier(tier_key: str, heading: str) -> None:
    st.subheader(heading)
    for key in ALL_TOPICS_ORDER:
        topic = TOPIC_DATA[key]
        if selected != "All" and topic.title != selected:
            continue
        links = [r for r in topic.resources if r.tier == tier_key]
        if not links:
            continue
        with st.container(border=True):
            st.markdown(f"**{topic.icon} {topic.title}**")
            for r in links:
                st.markdown(f"- [{r.title}]({r.url}) · `{r.kind}`")

show_tier("must_watch", "Must watch first")
show_tier("must_read", "Must read first")
show_tier("deep_dive", "Optional deep dive")
