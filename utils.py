import streamlit as st
from googletrans import Translator

translator = Translator()

def select_lang():
    if "lang" not in st.session_state:
        st.session_state["lang"] = "en"

    lang = st.sidebar.selectbox("Select language", ["en", "es", "zh-cn"],
                                format_func=lambda x: {"en": "English", "es": "Español", "zh-cn": "中文"}[x], key='lang')
    return lang

def t(text):
    lang = st.session_state.get("lang", "en")
    if lang == "en":
        return text
    try:
        return translator.translate(text, dest=lang).text
    except:
        return "[translation error]"

# st.title(t("Welcome to RISEsc"))
# st.write(t("This app displays data on air quality and health."))


# import streamlit as st
#
# def lang_toggle():
#
#     if "lang" not in st.session_state:
#         st.session_state["lang"] = "en"
#     lang = st.selectbox("Select language / Elige idioma", ["en", "es"], format_func=lambda x: {"en": "English", "es": "Español"}[x])
#     st.session_state["lang"] = lang
#
# def text_converter(key, translations):
#     lang = st.session_state.get("lang", "en")
#     return translations.get(key, {}).get(lang, key)

