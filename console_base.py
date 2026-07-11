from transformers import pipeline

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

def main():
    while True:
        print("\n--- Welcome to AI Text Analyzer ---\n")

        text = input("Enter text you want to analyze: ").strip()

        while text == "":
            print("Text cannot be empty. Please try again.")
            text = input("Enter text you want to analyze: ").strip()

        print("\nAnalyzing...\n")

        sentiment = sentiment_classifier(text)
        zero_shot = zero_shot_classifier(
            text,
            candidate_labels=candidate_labels,
            hypothesis_template="This text is about {}."
        )
        ner = ner_classifier(text)

        print("=" * 40)
        print("SENTIMENT ANALYSIS")
        print("=" * 40)
        result = sentiment[0]
        print(f"Label  : {result['label']}")
        print(f"Score  : {result['score']*100:.2f}%")

        print("=" * 40)
        print("NAMED ENTITIES")
        print("=" * 40)
        if ner:
            for entity in ner:
                print(f"Word   : {entity['word']}")
                print(f"Type   : {entity['entity_group']}")
                print(f"Score  : {entity['score']*100:.2f}%")
                print("-" * 20)
        else:
            print("No entities found.")

        print("=" * 40)
        print("TOPIC PREDICTION")
        print("=" * 40)
        print(f"Topic  : {zero_shot['labels'][0]}")
        print(f"Score  : {zero_shot['scores'][0]*100:.2f}%")

        print("\nAll Topic Scores:")
        for label, score in zip(zero_shot["labels"], zero_shot["scores"]):
            bar = "█" * int(score * 20)
            print(f"  {label:<15} {score*100:.2f}%  {bar}")

        print("=" * 40)

        ch = input("\nPress Y to exit or any key to analyze again: ")
        if ch.lower() == "y":
            print("\nThank you for using AI Text Analyzer. Goodbye!\n")
            break

main()