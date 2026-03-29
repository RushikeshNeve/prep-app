"""Lightweight style injection for a premium Streamlit look."""

import streamlit as st


def inject_styles() -> None:
    st.markdown(
        """
        <style>
        .block-container {padding-top: 1.2rem; padding-bottom: 2rem;}
        .topic-card {
            border: 1px solid rgba(151, 166, 195, 0.25);
            border-radius: 14px;
            padding: 14px;
            background: linear-gradient(180deg, rgba(37,99,235,.07), rgba(16,185,129,.05));
            margin-bottom: .8rem;
        }
        .muted {color: #64748B; font-size: 0.95rem;}
        .badge {
            display: inline-block; border-radius: 999px; padding: 0.15rem 0.6rem;
            border: 1px solid rgba(100,116,139,.35); margin-right: .35rem; font-size: .8rem;
        }
        .pill-success {background-color: rgba(16,185,129,.14);} 
        .pill-warning {background-color: rgba(245,158,11,.16);} 
        </style>
        """,
        unsafe_allow_html=True,
    )
