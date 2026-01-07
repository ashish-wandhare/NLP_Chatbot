import numpy as np
from src.preprocessing import clean_text
from src.semantic_matching import compute_similarity


def get_best_answer(
    user_question,
    df,
    model,
    question_embeddings,
    threshold=0.45
):
    """
    Finds the best matching answer for a user question.
    """

    # Clean user input
    cleaned_question = clean_text(user_question)

    # Encode user question
    user_embedding = model.encode([cleaned_question])

    # Compute similarity
    similarities = compute_similarity(user_embedding, question_embeddings)[0]

    # Find best match
    best_index = np.argmax(similarities)
    best_score = similarities[best_index]

    # Confidence check
    if best_score < threshold:
        return "Sorry, I don’t know the answer to that."

    return df.iloc[best_index]["answer"]
