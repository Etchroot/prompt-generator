from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="나만의 프롬프트 생성기", page_icon="🛠", layout="wide")

# Streamlit 기본 여백과 메뉴를 줄여서 생성기가 화면을 꽉 채우게
st.markdown(
    """
    <style>
      .block-container {padding: 0 0.5rem; max-width: 100%;}
      header[data-testid="stHeader"] {display: none;}
      iframe {border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "prompt-generator.html").read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
