import streamlit as st
from googletrans import Translator

translator = Translator()

lang = st.selectbox("Select language", ["en", "es"], format_func=lambda x: {"en": "English", "es": "Español"}[x])
st.session_state["lang"] = lang

def t(text):
    if lang == "en":
        return text
    try:
        return translator.translate(text, dest=lang).text
    except:
        return "[translation error]"

st.title(t("Welcome to RISEsc"))
st.write(t("This app displays data on air quality and health."))
