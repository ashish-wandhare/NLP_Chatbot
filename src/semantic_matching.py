from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
import pickle

# --------------------------------------------------
# Model loader (unchanged)
# --------------------------------------------------
def load_embedding_model():
    """
    Loads a pre-trained sentence embedding model.
    """
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model


# --------------------------------------------------
# Full encoding (unchanged)
# --------------------------------------------------
def encode_questions(model, questions):
    """
    Converts a list of questions into embeddings.
    """
    embeddings = model.encode(questions, show_progress_bar=True)
    return embeddings


# --------------------------------------------------
# NEW: Incremental encoding (ONLY NEW QUESTIONS)
# --------------------------------------------------
EMBED_PATH = Path("data/question_embeddings.pkl")

def incremental_encode_questions(model, questions):
    """
    Encodes ONLY new questions and reuses stored embeddings.
    """
    # Load existing embeddings
    if EMBED_PATH.exists():
        with open(EMBED_PATH, "rb") as f:
            embedding_store = pickle.load(f)
    else:
        embedding_store = {}

    # Find questions that need embeddings
    new_questions = [q for q in questions if q not in embedding_store]

    # Encode only new questions
    if new_questions:
        new_embeddings = model.encode(new_questions, show_progress_bar=True)

        for q, emb in zip(new_questions, new_embeddings):
            embedding_store[q] = emb

        # Save updated embeddings
        with open(EMBED_PATH, "wb") as f:
            pickle.dump(embedding_store, f)

    # Return embeddings in same order as questions
    return [embedding_store[q] for q in questions]


# --------------------------------------------------
# Similarity computation (unchanged)
# --------------------------------------------------
def compute_similarity(user_embedding, question_embeddings):
    """
    Computes cosine similarity between user input and all questions.
    """
    similarities = cosine_similarity(user_embedding, question_embeddings)
    return similarities
