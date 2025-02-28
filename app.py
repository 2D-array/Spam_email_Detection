import streamlit as st
import pickle

# Load the trained model
with open("spam_classifier.pkl", "rb") as model_file:
    clf = pickle.load(model_file)

# Streamlit UI
st.title("📩 Spam Detection App")
st.write("Enter a message below to check if it's spam or not.")

# User input
user_input = st.text_area("Enter your message here:")

# Predict button
if st.button("Predict"):
    if user_input.strip():  # Ensure input is not empty
        prediction = clf.predict([user_input])[0]
        result = "🚨 Spam" if prediction == 1 else "✅ Not Spam"
        st.subheader(result)
    else:
        st.warning("Please enter a message before predicting.")

# Footer
st.markdown("**Created with ❤️ using Streamlit & Naïve Bayes**")
