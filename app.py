import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faqs import FAQS

# ---------------------------
# 1. Page setup
# ---------------------------
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖")
st.title("🤖 Python FAQ Chatbot")
st.write("Ask me anything about Python programming!")

# ---------------------------
# 2. Prepare data (do this once)
# ---------------------------
@st.cache_resource
def prepare_data():
    # Download NLTK data (first run only)
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)
    nltk.download("stopwords", quiet=True)

    stop_words = set(stopwords.words("english"))

    def clean(text):
        # lowercase + tokenize + remove stopwords + remove non-alphanumeric
        tokens = word_tokenize(text.lower())
        tokens = [t for t in tokens if t.isalnum() and t not in stop_words]
        return " ".join(tokens)

    questions = [f["question"] for f in FAQS]
    cleaned_questions = [clean(q) for q in questions]

    vectorizer = TfidfVectorizer()
    question_vectors = vectorizer.fit_transform(cleaned_questions)

    return vectorizer, question_vectors, clean

vectorizer, question_vectors, clean_text = prepare_data()

# ---------------------------
# 3. Chat history
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me a question about Python."}
    ]

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------------------
# 4. Handle user input
# ---------------------------
user_input = st.chat_input("Type your question here...")

if user_input:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Find best matching FAQ
    cleaned_input = clean_text(user_input)
    input_vector = vectorizer.transform([cleaned_input])
    similarities = cosine_similarity(input_vector, question_vectors)[0]

    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    if best_score < 0.15:
        answer = "Sorry, I couldn't find a matching FAQ. Try rephrasing or asking a different Python question."
    else:
        answer = FAQS[best_idx]["answer"]

    # Show bot's reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
        if best_score >= 0.15:
            st.caption(f"Matched: *{FAQS[best_idx]['question']}* (similarity: {best_score:.2f})")