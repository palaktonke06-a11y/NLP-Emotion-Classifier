
import streamlit as st
import joblib
from pathlib import Path

# Page Configuration
st.set_page_config(
    page_title="Emotion AI | NLP",
    page_icon="💬",
    layout="centered"
)

# Load Trained Model
MODEL_PATH = Path(__file__).parent / "sentiment_pipeline.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as e:
    st.error(f"Model loading failed: {e}")
    st.stop()

# UI
st.title("💬 Emotion AI")
st.caption("NLP Based Emotion Classification")

st.write(
    "Discover the emotion expressed in your text "
    "using Machine Learning."
)

st.divider()

user_text = st.text_area(
    "Enter your text",
    placeholder="Example: I feel so happy today!",
    height=150
)

if st.button("Analyze Emotion", type="primary",
             use_container_width=True):

    if user_text.strip():

        prediction = model.predict([user_text])[0]

        st.success("Analysis Complete!")
        st.subheader("Predicted Emotion")
        st.markdown(f"### 💡 {prediction}")

    else:
        st.warning("Please enter some text.")

st.divider()
st.caption("Built with Python • NLP • Machine Learning • Streamlit")
