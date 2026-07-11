import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Analyzer", page_icon="🤖", layout="centered")

st.title("🤖 AI Text Analyzer")
st.write("Enter your text below and the app will analyze the sentiment, named entities, and topic.")

@st.cache_resource
def load_models():
    sentiment_classifier = pipeline(
        "sentiment-analysis",
        model="Saved_Model/sentiment",
        tokenizer="Saved_Model/sentiment"
    )

    ner_classifier = pipeline(
        "ner",
        model="Saved_Model/ner",
        tokenizer="Saved_Model/ner",
        aggregation_strategy="simple"
    )

    zero_shot_classifier = pipeline(
        "zero-shot-classification",
        model="Saved_Model/zero_shot",
        tokenizer="Saved_Model/zero_shot"
    )

    return sentiment_classifier, ner_classifier, zero_shot_classifier


sentiment_classifier, ner_classifier, zero_shot_classifier = load_models()

text = st.text_area("Enter your text here:", height=200)

candidate_labels = [
    "technology",
    "business",
    "education",
    "health",
    "sports",
    "politics",
    "entertainment",
    "science"
]

if st.button("Analyze Text"):
    if text.strip() == "":
        st.warning("Please enter some text before analyzing.")
    else:
        with st.spinner("Analyzing your text, please wait..."):
            sentiment_result = sentiment_classifier(text)
            ner_result = ner_classifier(text)
            topic_result = zero_shot_classifier(
                text,
                candidate_labels=candidate_labels,
                hypothesis_template="This text is about {}."
            )

        result = sentiment_result[0]

        st.success(f"Sentiment: {result['label']}")
        st.metric(
            "Confidence",
            f"{result['score']*100:.2f}%"
        )

        st.subheader("Named Entities")
        if ner_result:
            for entity in ner_result:
                st.write(
                    f"**Word:** {entity['word']} | **Type:** {entity['entity_group']} | **Score:** {entity['score']:.2f}"
                )
        else:
            st.write("No named entities were found in the provided text.")

        st.subheader("Predicted Topic")
        st.write(f"**Topic:** {topic_result['labels'][0]}")
        st.write(f"**Confidence:** {topic_result['scores'][0]:.2f}")

        st.subheader("All Topic Scores")
        for label, score in zip(topic_result["labels"], topic_result["scores"]):
            st.write(f"**{label}** - {score:.2f}")
            st.progress(float(score))