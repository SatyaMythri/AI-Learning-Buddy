import os
import streamlit as st
from google import genai

# Replace with your Gemini API Key
#api_key = os.getenv("GEMINI_API_KEY")

#st.write("Key loaded:", api_key is not None)
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)
st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy")
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple choice questions on {topic} with answers."

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            st.subheader("Result")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
