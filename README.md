End-to-End NLP Development: Intelligent Conversational Chatbot
ChatGTP (General Text Processing)
--------------------------------------------------------------------
Project Overview

This project implements an end-to-end Natural Language Processing (NLP) based conversational chatbot that answers general knowledge questions using semantic similarity instead of keyword matching.

The chatbot processes raw text data, understands the meaning of user queries, and retrieves the most relevant factual answer from a structured dataset.

This project is designed as a first NLP project to understand the complete NLP pipeline, from raw text to an intelligent conversational system.

Objectives

Build an NLP chatbot from raw text data

Understand semantic similarity using sentence embeddings

Retrieve accurate answers from a fact-based dataset

Avoid hallucination by using retrieval-based NLP

Design a clean and modular NLP pipeline


📂 Dataset Description

Dataset type: General Knowledge Question–Answer Dataset

Format: CSV

Total records: 930

Columns:3 question,answer,question_type

question – natural language General Knowledge questions

answer – factual answers

question_type – difficulty labels (kid,class_1..to..class_7)

In the current implementation, all questions are used together to maximize semantic coverage.
In this I am not using difficulty labels.


NLP Pipeline (End-to-End)
Raw CSV Data
   ↓
Data Loading
   ↓
Text Preprocessing
   ↓
Sentence Embeddings
   ↓
Semantic Similarity Matching
   ↓
Best Answer Retrieval
   ↓
Conversational Response

🛠️ Technologies Used

Python 3.12

Pandas – data handling

Regular Expressions (re) – text cleaning

Sentence Transformers – semantic embeddings

Scikit-learn – cosine similarity

VS Code – development environment

📁 Project Structure
NLP_Chatbot/
│── data/
│   └── general_knowledge_qa.csv
│
│── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── semantic_matching.py
│   ├── chatbot_engine.py
│
│── app.py
│── requirements.txt
│── README.md
│── venv/

⚙️ How the Chatbot Works

Loads the dataset from CSV

Cleans raw text while preserving meaning

Converts questions into semantic embeddings

Converts user input into an embedding

Computes similarity using cosine similarity

Retrieves the most relevant factual answer

Returns a fallback response if confidence is low

💬 Sample Interaction
You: how many letters in english
Bot: 26

You: which bird has largest egg
Bot: Ostrich

You: location of Eden Gardens
Bot: Calcutta


The chatbot successfully handles:

Paraphrased questions

Minor spelling mistakes

Semantic understanding

✅ Key Features

Semantic understanding (not keyword-based)

Fact-based answer retrieval

No hallucination or answer generation

Robust to spelling variations

Clean modular NLP design

🚀 How to Run the Project

Create and activate a virtual environment

Install dependencies:

pip install -r requirements.txt


Run the chatbot:

python app.py

📌 Design Decision

Although the dataset includes difficulty levels, level-based filtering was intentionally disabled in the current version to improve answer accuracy due to limited data per category.

This design choice ensures:

Better semantic coverage

Improved chatbot performance

Simpler user interaction

🔮 Future Improvements

Automatic difficulty-level detection

Web interface using Streamlit

Top-k answer suggestions

Improved answer formatting

Larger knowledge base

Answer Validation Criteria:
The correctness of chatbot responses is determined using semantic similarity scores computed via cosine similarity on sentence embeddings. Answers are returned only when similarity exceeds a predefined confidence threshold, ensuring alignment with ground truth responses from the dataset.

🏁 Conclusion

This project demonstrates a complete end-to-end NLP system that converts raw text data into an intelligent conversational chatbot using semantic similarity. It serves as a strong foundation for learning practical NLP concepts and building more advanced conversational AI systems in the future.

👤 Author

Ashish Wandhare
NLP Project