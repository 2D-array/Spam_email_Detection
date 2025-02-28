import streamlit as st
import pickle

# Load the trained model
with open("spam_classifier.pkl", "rb") as model_file:
    clf = pickle.load(model_file)

# Custom CSS for dark mode and modern UI
st.markdown("""
    <style>
    /* Main container */
    .main {
        background-color: #1e1e1e;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    }
    /* Title */
    .title {
        color: #00d4ff;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 36px;
        text-align: center;
        margin-bottom: 10px;
    }
    /* Subtitle */
    .subtitle {
        color: #b0b0b0;
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    /* Text area */
    .stTextArea textarea {
        background-color: #2d2d2d;
        color: #e0e0e0;
        border: 1px solid #404040;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    /* Selectbox */
    .stSelectbox > div > div {
        background-color: #2d2d2d;
        color: #e0e0e0;
        border: 1px solid #404040;
        border-radius: 8px;
    }
    /* Button */
    .stButton > button {
        background-color: #00d4ff;
        color: #1e1e1e;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #00b0cc;
    }
    /* Result box */
    .result-box {
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .spam {
        background-color: #ff5555;
        color: #ffffff;
    }
    .not-spam {
        background-color: #55ff55;
        color: #1e1e1e;
    }
    /* Warning */
    .stWarning {
        background-color: #ffaa00;
        color: #1e1e1e;
        border-radius: 8px;
    }
    /* Footer */
    .footer {
        text-align: center;
        color: #707070;
        margin-top: 30px;
        font-size: 14px;
    }
    /* General text color */
    body, .stMarkdown, .stText {
        color: #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI with dark mode
# st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<h1 class="title">📩 Spam Detection Hub</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Classify your messages with cutting-edge AI</p>', unsafe_allow_html=True)

# Define dummy text options
dummy_texts = {
    "None": "",
    "Sample Not Spam": "Hi there, just checking in to see how you're doing this week!",
    "Sample Spam": "Congratulations! You've won $1,000,000! Click here to claim your prize now!"
}

# Layout with columns
col1, col2 = st.columns([3, 1], gap="medium")

with col2:
    # Dummy text selector
    dummy_option = st.selectbox("Generate Example", list(dummy_texts.keys()), help="Pick a sample message")

# Set initial text area value based on dummy option
initial_text = dummy_texts[dummy_option]

with col1:
    # User input with dynamic initial value
    user_input = st.text_area("Your Message:", value=initial_text, height=200, key="input_text", placeholder="Type or select a message...")

# Predict button centered
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Analyze Now", key="predict_btn"):
    if user_input.strip():  # Ensure input is not empty
        prediction = clf.predict([user_input])[0]
        result = "🚨 Spam Detected" if prediction == 1 else "✅ Safe Message"
        result_class = "spam" if prediction == 1 else "not-spam"
        st.markdown(f'<div class="result-box {result_class}">{result}</div>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a message to analyze.")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown('<p class="footer">Powered by Streamlit & Naïve Bayes • Built with ❤️</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)