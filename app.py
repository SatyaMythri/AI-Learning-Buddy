import streamlit as st
import os
from groq import Groq

# Initialize Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy")
st.write("Learn any topic with AI!")

# User Input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz"
    ]
)

# Generate Button
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        else:
            prompt = f"Create 5 multiple choice questions on {topic} with answers."

        try:

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1024
            )

            answer = response.choices[0].message.content

            st.subheader("Result")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")
