
# NLP Emotion Classifier

An NLP-based Machine Learning application that predicts emotions from text using TF-IDF, Naive Bayes, and Logistic Regression, with an interactive Streamlit interface.

## Problem Statement
Manually identifying emotions from large volumes of textual feedback, reviews, and messages can be time-consuming. Understanding the emotional tone of text can help organize and analyze feedback more efficiently.

## Solution
This project uses Natural Language Processing and Machine Learning to classify text into emotion categories. It compares multiple ML approaches and provides an interactive interface where users can enter text and view the predicted emotion.

## Key Features
- Text-based emotion prediction
- Text representation using Bag of Words and TF-IDF
- Comparison of Naive Bayes and Logistic Regression
- Model evaluation using accuracy, precision, recall, F1-score, and confusion matrix
- Interactive Streamlit web application
- Saved model pipeline for reusable predictions

## Tech Stack
- Python
- Pandas and NumPy
- Scikit-learn
- NLP and TF-IDF
- Bag of Words
- Naive Bayes
- Logistic Regression
- Streamlit
- Joblib
- Jupyter Notebook

## Workflow
1. Load and inspect the dataset
2. Clean the text data
3. Split the data into training and testing sets
4. Convert text into numerical features
5. Train and compare machine learning models
6. Evaluate model performance
7. Save the selected model pipeline
8. Deploy the model through a Streamlit interface

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run Locally

```bash
python -m streamlit run app.py
```

## Model Evaluation
The models are compared using test-set accuracy. The selected model is also evaluated using a classification report and confusion matrix.

## Applications
- Customer feedback analysis
- Review emotion classification
- Text analytics and research
- Exploring emotional patterns in written feedback

## Limitations
Predictions depend on the training data and may not reliably interpret sarcasm, context, or complex expressions. The predicted emotion is a model estimate, not a definitive assessment of a person's feelings.

## Future Improvements
- Evaluate on diverse, unseen text
- Improve model generalization
- Add supported prediction-confidence information
- Visualize emotion patterns across larger feedback datasets
- Enhance the Streamlit interface

## Author
Palak Tonke

Computer Science Engineering | Data Science

**Note:** This project is developed for learning and demonstration of NLP, Machine Learning, and model deployment.
