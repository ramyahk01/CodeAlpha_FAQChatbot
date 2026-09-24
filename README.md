# 🤖 FAQ Chatbot — Python Programming

An intelligent FAQ chatbot that answers Python programming questions using **Natural Language Processing** and **Cosine Similarity**. Built as part of the CodeAlpha internship program.

## ✨ Features

- 20+ Python programming FAQs
- NLP preprocessing with NLTK (tokenization + stopword removal)
- TF-IDF vectorization for text representation
- Cosine similarity matching for finding best answer
- Interactive chat UI with Streamlit
- Shows matched question + similarity score for transparency
- Gracefully handles out-of-scope questions

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.13 |
| UI Framework | Streamlit |
| NLP Library | NLTK |
| ML / Vectors | scikit-learn (TF-IDF, cosine similarity) |
| Environment | Virtual Environment (venv) |

## 🧠 How It Works

1. User types a question in the chat
2. NLTK preprocesses text (lowercase, tokenize, remove stopwords)
3. Text is converted to a TF-IDF vector
4. Cosine similarity is computed against all FAQ questions
5. Best matching question (highest score) is found
6. If similarity ≥ 0.15 → return its answer
   If similarity < 0.15 → return "Sorry, I don't know"
7. Answer is displayed in the chat UI

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ramyahk01/CodeAlpha_FAQChatbot.git
   cd CodeAlpha_FAQChatbot

   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows

   pip install -r requirements.txt

   python -m nltk.downloader punkt stopwords

   streamlit run app.py

   
6. Open your browser at `http://localhost:8501`

## 📁 Project Structure
CodeAlpha_FAQChatbot/
├── app.py # Main chatbot + Streamlit UI
├── faqs.py # FAQ data (20 Q&A pairs)
├── requirements.txt # Dependencies
└── README.md # Project documentation


## 💬 Example Questions to Try

- What is Python?
- Tell me about lists
- How to install python?
- Difference between list and tuple
- What is pip?

## 👤 Author

Ramya H K — B.Tech AI & ML Student

## 📜 License

This project is part of the CodeAlpha internship program.
