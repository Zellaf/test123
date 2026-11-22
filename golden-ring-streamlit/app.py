from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Золотое кольцо", layout="wide")
show_demo = components.declare_component(
    "golden_ring", path=str(Path(__file__).parent / "site")
)
show_demo(key="golden_ring_demo", default=None)
