import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Add New Q&A",
    layout="centered"
)

CSV_PATH = Path("data/general_knowledge_qa.csv")

# --------------------------------------------------
# Helper function to append Q&A
# --------------------------------------------------
def append_qa(csv_path, question, answer):
    if csv_path.exists():
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame(columns=["question", "answer", "question_type"])

    new_row = {
        "question": question.strip(),
        "answer": answer.strip(),
        "question_type": "user_added"
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(csv_path, index=False)


# --------------------------------------------------
# UI Design
# --------------------------------------------------

st.markdown(
    "<h1 style='color: gray;'>Add new question and answer</h1>",
    unsafe_allow_html=True
)
st.write("Use this to expand the ChatGTP knowledge base.")

question = st.text_input("❓ Enter Question")
answer = st.text_area("📝 Enter Answer", height=120)

if st.button("💾 Save"):
    if not question.strip() or not answer.strip():
        st.warning("⚠️ Question and Answer cannot be empty.")
    else:
        append_qa(CSV_PATH, question, answer)
        st.success("✅ Question & Answer added successfully!")

        