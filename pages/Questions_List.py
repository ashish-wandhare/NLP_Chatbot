import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Question List",
    layout="wide"
)

st.title("📋 Question List")

# --------------------------------------------------
# CSV path
# --------------------------------------------------
CSV_PATH = Path("data/general_knowledge_qa.csv")

# --------------------------------------------------
# Load dataset (auto-refresh using file timestamp)
# --------------------------------------------------
@st.cache_data
def load_data(csv_path: str, last_modified: float):
    return pd.read_csv(csv_path)

# Get file modification time
last_modified = CSV_PATH.stat().st_mtime

# Load fresh data automatically when CSV changes
df = load_data(str(CSV_PATH), last_modified)

# --------------------------------------------------
# Display dataset
# --------------------------------------------------
st.dataframe(df, use_container_width=True)

# --------------------------------------------------
# Footer / Info
# --------------------------------------------------
st.caption(f"📚 Total questions: {len(df)}")
