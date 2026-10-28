# NLP Chatbot — Semantic Similarity-Based Question Answering

An end-to-end Natural Language Processing (NLP) chatbot that answers general knowledge questions using **sentence embeddings and semantic similarity**.

🔗 **GitHub Repository:** [NLP_Chatbot](https://github.com/ashish-wandhare/NLP_Chatbot)

---

## 📌 Project Overview

This project implements an intelligent conversational chatbot that retrieves factual answers from a structured question-answer dataset using semantic similarity rather than traditional keyword matching.

The chatbot processes natural language queries, converts questions into sentence embeddings, and identifies the most relevant question in the dataset using cosine similarity.

Once a suitable match is found, the chatbot retrieves and returns its corresponding answer.

The system follows a retrieval-based NLP approach, making it suitable for answering questions from a predefined knowledge base without generating new answers using an LLM.

## 🎯 Project Objectives

- Build an end-to-end NLP chatbot using Python.
- Understand semantic similarity using sentence embeddings.
- Retrieve relevant factual answers from a structured dataset.
- Implement confidence-based answer retrieval.
- Reduce incorrect responses through retrieval-based NLP.
- Develop a clean and modular NLP pipeline.

## ✨ Key Features

- **Semantic Understanding:** Matches questions based on meaning rather than exact keywords.
- **Sentence Embeddings:** Converts natural language questions into numerical representations.
- **Similarity Matching:** Uses cosine similarity to identify the most relevant question.
- **Fact-Based Retrieval:** Returns answers from the existing dataset.
- **Confidence Threshold:** Provides a fallback response when similarity is below the predefined threshold.
- **Modular Architecture:** Separates data loading, preprocessing, semantic matching, and chatbot logic.
- **Paraphrase Handling:** Supports differently worded questions with similar meanings.

## 📂 Dataset Description

The chatbot uses a General Knowledge Question–Answer dataset stored in CSV format.

| Property | Description |
|---|---|
| Dataset | General Knowledge Q&A |
| File Format | CSV |
| Total Records | 930 |
| Columns | `question`, `answer`, `question_type` |

### Dataset Columns

- `question` — Natural language general knowledge questions.
- `answer` — Corresponding factual answers.
- `question_type` — Difficulty labels such as `kid`, `class_1`, through `class_7`.

In the current implementation, all questions are used together to maximize semantic coverage. Difficulty-level filtering is not enabled.

## 🔄 NLP Pipeline

The chatbot follows an end-to-end NLP pipeline:

```text
Raw CSV Dataset
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
Confidence Threshold Validation
      ↓
Conversational Response
```

## ⚙️ How the Chatbot Works

1. **Data Loading**  
   Loads general knowledge questions and answers from the CSV dataset.

2. **Text Preprocessing**  
   Cleans the input text while preserving its meaning.

3. **Sentence Embedding Generation**  
   Converts dataset questions into semantic vector representations using Sentence Transformers.

4. **User Query Processing**  
   Converts the user's question into a sentence embedding.

5. **Semantic Similarity Matching**  
   Computes cosine similarity between the user query and dataset questions.

6. **Answer Retrieval**  
   Identifies the best-matching question and retrieves its corresponding factual answer.

7. **Confidence Validation**  
   Checks the similarity score against a predefined confidence threshold.

8. **Response Generation**  
   Returns the retrieved answer or a fallback response when confidence is insufficient.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3.12 | Core programming language |
| Pandas | Dataset loading and data handling |
| Regular Expressions (`re`) | Text preprocessing |
| Sentence Transformers | Sentence embeddings |
| Scikit-learn | Cosine similarity |
| VS Code | Development environment |

## 📁 Project Structure

```text
NLP_Chatbot/
│
├── data/
│   └── general_knowledge_qa.csv
│
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── semantic_matching.py
│   └── chatbot_engine.py
│
├── app.py
├── requirements.txt
├── README.md
└── venv/
```

## 💬 Sample Interaction

```text
You: How many letters are there in the English alphabet?
Bot: 26

You: Which bird has the largest egg?
Bot: Ostrich

You: Where is Eden Gardens located?
Bot: Calcutta
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12
- Git
- VS Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/ashish-wandhare/NLP_Chatbot.git
```

### 2. Navigate to the Project Directory

```bash
cd NLP_Chatbot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Chatbot

```bash
python app.py
```

## 🧠 Design Decisions

### Retrieval-Based NLP Approach

The chatbot uses semantic similarity to retrieve answers from a predefined dataset rather than generating new answers.

This approach was selected to:

- Keep responses aligned with the dataset's factual answers.
- Avoid relying on generative AI for answer creation.
- Provide a simple and interpretable NLP architecture.

### Difficulty-Level Filtering

Although the dataset contains question difficulty labels, level-based filtering is intentionally disabled in the current implementation.

All questions are used together to:

- Maximize semantic coverage.
- Improve the availability of relevant matches.
- Simplify user interaction.

## ✅ Answer Validation

The chatbot uses cosine similarity scores computed from sentence embeddings to determine the relevance of a user query to dataset questions.

A predefined confidence threshold determines whether an answer should be returned.

- If the similarity score exceeds the threshold, the corresponding answer is retrieved.
- If the similarity score is below the threshold, a fallback response is returned.

This helps reduce irrelevant answers when the user's query does not sufficiently match the dataset.

## 🔮 Future Improvements

- Automatic difficulty-level detection.
- Streamlit-based web interface.
- Top-k answer suggestions.
- Improved answer formatting.
- Expanded knowledge base.
- Enhanced query preprocessing and matching.

## 🏁 Conclusion

This project demonstrates the development of an end-to-end NLP chatbot using sentence embeddings and semantic similarity.

It covers the complete pipeline from raw question-answer data to semantic matching and factual answer retrieval, providing a practical foundation for understanding NLP and building more advanced conversational systems.

---
- GitHub: [Repository](https://github.com/ashish-wandhare/NLP_Chatbot)
- Streamlit Cloud: [Live Demo](https://nlpchatbot-bzbocjsas2my6v7zfnsxkv.streamlit.app/)
- AWS EC2: [Live Demo](http://13.239.147.87:8501/)
