import streamlit as st
from decision import decide_action
from weather import fetch_weather
from rag import answer_pdf_query

import re

def extract_city(query: str) -> str:
    # Try extracting the city name after "in" or at the end of the question
    match = re.search(r"\bin\s+([a-zA-Z\s]+)", query.lower())
    if match:
        city = match.group(1).strip()
    else:
        # Use fallback: remove common phrases
        city = re.sub(r"(what's|is|the|weather|temperature|like|forecast|in|of|for)", "", query.lower())
        city = re.sub(r"[^a-zA-Z\s]", "", city).strip()

    # Capitalize each word (e.g., new york -> New York)
    return " ".join(word.capitalize() for word in city.split())


st.set_page_config(page_title="Weather & PDF Assistant", layout="centered")
st.title("🌤️ Weather & 📄 PDF Assistant")

query = st.text_input("Ask something:")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        task = decide_action(query)
        if task == "weather":
            city = extract_city(query)
            response = fetch_weather(city)
        else:
            response = answer_pdf_query(query)
        st.success(response)
