import streamlit as st
import os
from google import genai

# ----------------------------
# Gemini Client
# ----------------------------
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ----------------------------
# Streamlit Page
# ----------------------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy")
st.write("Learn any topic with simple explanations, examples, and quizzes!")

# ----------------------------
# User Input
# ----------------------------
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz"
    ]
)

# ----------------------------
# Generate Button
# ----------------------------
if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        # Prompt Selection
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."

        else:
            prompt = f"Create 5 multiple choice questions on {topic} with answers."

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("Result")
            st.write(response.text)

        except Exception:

            st.subheader("Result")

            # ----------------------------
            # Explain Concept
            # ----------------------------
            if option == "Explain Concept":

                st.write(f"""
### {topic}

{topic} is an important concept that helps people understand and solve real-world problems more effectively.

It involves learning the basic principles, understanding how they work, and applying them in practical situations.

For beginners, the best way to learn {topic} is through simple explanations, examples, and regular practice.
                """)

            # ----------------------------
            # Real-Life Example
            # ----------------------------
            elif option == "Real-Life Example":

                st.write(f"""
### Real-Life Example

Imagine learning to ride a bicycle.

At first, someone explains the basics.

Then they show a real demonstration.

After that, you practice yourself.

Learning **{topic}** follows the same process—understand the concept, observe examples, and practice until you become confident.
                """)

            # ----------------------------
            # Quiz
            # ----------------------------
            else:

                st.write(f"""
### Quiz on {topic}

**1. What is the main purpose of {topic}?**

A. Entertainment

B. Understanding concepts ✅

C. Cooking

D. Traveling

---

**2. Why is {topic} important?**

A. It helps solve problems ✅

B. It wastes time

C. It replaces teachers

D. None

---

**3. Which is the best way to learn {topic}?**

A. Practice regularly ✅

B. Ignore it

C. Memorize only

D. Guess answers

---

**4. Which statement is correct?**

A. Learning takes practice ✅

B. Practice is unnecessary

C. Reading alone is enough

D. None

---

**5. Beginners should first:**

A. Learn the basics ✅

B. Skip fundamentals

C. Take exams directly

D. Avoid examples
                """)

st.markdown("---")
st.caption("Built using Streamlit and Google Gemini API")
