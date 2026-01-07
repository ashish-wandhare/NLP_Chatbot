import streamlit as st
from pathlib import Path

from src.data_loading import load_dataset
from src.preprocessing import clean_text
from src.semantic_matching import load_embedding_model, encode_questions
from src.chatbot_engine import get_best_answer

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="General Knowledge NLP Chatbot",
    layout="centered"
)

CSV_PATH = Path("data/general_knowledge_qa.csv")

# --------------------------------------------------
# FIXED HEADER
# --------------------------------------------------
st.markdown(
    """
    <style>
    .app-header {
        position: fixed;
        top: 3.5rem;
        left: 0;
        width: 100%;
        background-color: white;
        z-index: 1000;
    }

    .header-inner {
        max-width: 800px;
        margin: 0 auto;
        padding: 14px 20px;
    }

    .block-container {
        padding-top: 200px !important;
    }
    </style>

    <div class="app-header">
        <div class="header-inner">
            <h1 style="margin:0; color:gray;">🤖 ChatGTP</h1>
            <h4 style="margin-top:2px; color:gray;">General Text Processing</h4>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# Load model (cached ONCE)
# --------------------------------------------------
@st.cache_resource
def load_model():
    return load_embedding_model()

# --------------------------------------------------
# Load dataset (auto-refresh when CSV changes)
# --------------------------------------------------
@st.cache_data
def load_qa_data(csv_path: str, last_modified: float):
    df = load_dataset(csv_path)
    questions = df["question"].apply(clean_text).tolist()
    return df, questions

# --------------------------------------------------
# Compute embeddings (cached, FAST)
# --------------------------------------------------
@st.cache_data
def compute_embeddings(questions, last_modified: float):
    model = load_model()   # safe: cache_resource
    return encode_questions(model, questions)

# --------------------------------------------------
# Load everything
# --------------------------------------------------
model = load_model()

last_modified = CSV_PATH.stat().st_mtime

df, questions = load_qa_data(str(CSV_PATH), last_modified)
from src.semantic_matching import incremental_encode_questions

question_embeddings = incremental_encode_questions(model, questions)

# --------------------------------------------------
# Initialize chat history
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 Ask me a general knowledge question."
        }
    ]

# --------------------------------------------------
# Display chat history
# --------------------------------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Chat input
# --------------------------------------------------
user_question = st.chat_input("Type your question here...")

if user_question:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )
    with st.chat_message("user"):
        st.markdown(user_question)

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_best_answer(
                user_question,
                df,
                model,
                question_embeddings
            )
        st.markdown(f"✅ **Answer:** {answer}")

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown(
    """
    <style>
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 5px;
        width: 100%;
        text-align: center;
        font-size: 14px;
        color: #9e9e9e;
        opacity: 0.8;
        z-index: 100;
        pointer-events: none;
    }
    </style>

    <div class="custom-footer">
        <div>Developed by Ashish. ChatGTP can make mistakes.</div>
    </div>
    """,
    unsafe_allow_html=True
)
