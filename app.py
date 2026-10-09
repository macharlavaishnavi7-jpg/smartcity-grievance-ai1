
import streamlit as st
from src.response_service import get_response

st.set_page_config(
    page_title="Smart City Grievance Guide",
    page_icon="🏙️",
    layout="centered"
)

st.title("🏙️ Smart City Grievance Guide")

st.write(
    "Understand civic grievance categories, general procedures, "
    "and official channels for roads, water, electricity, and sanitation."
)

st.info(
    "This assistant provides general information only. "
    "It does not register complaints, track complaint status, "
    "or guarantee resolutions or timelines."
)

category = st.selectbox(
    "Choose a civic issue (optional)",
    [
        "General question",
        "Roads and potholes",
        "Water supply",
        "Electricity",
        "Sanitation and waste"
    ]
)

question = st.text_area(
    "What would you like to understand?",
    placeholder="Example: What should I know before reporting a pothole?",
    height=120
)

if st.button("Get Guidance", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")
    else:
        if category == "General question":
            full_question = question
        else:
            full_question = f"My issue is related to {category}. {question}"

        with st.spinner("Preparing guidance..."):
            answer = get_response(full_question)

        st.subheader("Guidance")
        st.write(answer)

st.divider()

st.caption(
    "Always verify current procedures with the relevant official "
    "municipal authority or utility provider."
)
