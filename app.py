
import streamlit as st

st.set_page_config(
    page_title="Smart City Grievance Guide",
    page_icon="🏙️",
    layout="centered",
)

st.title("🏙️ Smart City Grievance Guide")

st.write(
    "Understand civic grievance categories, general procedures, "
    "and where to find official guidance."
)

st.info(
    "This assistant provides information only. It does not register "
    "complaints, track complaint status, or guarantee resolution."
)

st.subheader("How can I help you?")

category = st.selectbox(
    "Choose a topic (optional)",
    [
        "All topics",
        "Roads and potholes",
        "Water supply",
        "Electricity",
        "Sanitation and waste",
    ],
)

question = st.text_area(
    "Enter your question",
    placeholder="Example: What should I do if there is a pothole on my road?",
    height=120,
)

if st.button("Get Guidance", type="primary"):
    if not question.strip():
        st.error("Please enter a question first.")
    else:
        st.session_state["last_question"] = question.strip()
        st.session_state["last_category"] = category

        st.warning(
            "The frontend is ready. AI guidance will appear here "
            "after the backend integration is completed."
        )

        st.write("**Your question:**", question.strip())
        st.write("**Selected topic:**", category)

st.divider()

st.caption(
    "For current procedures and timelines, consult the relevant "
    "official authority."
)