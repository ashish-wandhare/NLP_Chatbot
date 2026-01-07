import pandas as pd
import os



def load_dataset(csv_path):
    """
    Loads and validates the general knowledge QA dataset.
    """

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset not found at: {csv_path}")

    df = pd.read_csv(csv_path)

    required_columns = {"question", "answer", "question_type"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Dataset must contain columns: {required_columns}")

    df = df.dropna(subset=["question", "answer", "question_type"])

    df["question"] = df["question"].astype(str).str.strip()
    df["answer"] = df["answer"].astype(str).str.strip()
    df["question_type"] = df["question_type"].astype(str).str.strip()

    return df
