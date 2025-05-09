import streamlit as st

def lang_toggle():

    if "lang" not in st.session_state:
        st.session_state["lang"] = "en"
    lang = st.selectbox("Select language / Elige idioma", ["en", "es"], format_func=lambda x: {"en": "English", "es": "Español"}[x])
    st.session_state["lang"] = lang

def text_converter(key, translations):
    lang = st.session_state.get("lang", "en")
    return translations.get(key, {}).get(lang, key)

