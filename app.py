import sys

# Step 1: Monkey patch for Python 3.14 compatibility
try:
    import cgi
except ImportError:
    import legacy_cgi as cgi
    sys.modules['cgi'] = cgi

import streamlit as st
from googletrans import Translator, LANGUAGES

# Step 2: Initialize the translation engine 
translator = Translator()

# Step 3: UI Configuration and Header 
st.set_page_config(page_title="CodeAlpha | AI Translator", page_icon="🌍")

st.title("🌍 AI Language Translation Tool")
st.markdown("""
    Welcome to the CodeAlpha Internship. 
    This tool uses the Google Translate API to process your text.
""")

# Step 4: User Input Section 
st.subheader("1. Enter Text")
text_to_translate = st.text_area("Input text to translate:", placeholder="Hello, how are you?", height=150)

# Step 5: Language Selection 
st.subheader("2. Select Languages")
col1, col2 = st.columns(2)

with col1:
    # Mapping full language names from the library
    source_lang = st.selectbox("Source Language", options=list(LANGUAGES.values()), index=list(LANGUAGES.values()).index('english'))

with col2:
    # Defaulting target to Urdu based on your preference
    target_lang = st.selectbox("Target Language", options=list(LANGUAGES.values()), index=list(LANGUAGES.values()).index('urdu'))

# Map full names back to language codes (e.g., 'english' -> 'en')
lang_codes = {v: k for k, v in LANGUAGES.items()}

# Step 6: Translation Logic and Output 
if st.button("Translate Now"):
    if text_to_translate.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Processing translation..."):
            try:
                # Call the API
                result = translator.translate(
                    text_to_translate, 
                    src=lang_codes[source_lang], 
                    dest=lang_codes[target_lang]
                )
                
                # Display the response 
                st.success("Translation Complete!")
                st.subheader("Translated Text:")
                st.code(result.text, language='')
                
                # Optional: Extra Feature for better usability 
                st.button("Clear Output", on_click=lambda: st.rerun())

            except Exception as e:
                st.error(f"API Error: {e}. Please check your internet connection or try a different language.")

# Footer for internship 
st.divider()
st.caption("CodeAlpha Artificial Intelligence Internship | Task 1")
