from transformers import pipeline

emotion_model = pipeline(
    "text-classification", 
    model="j-hartmann/emotion-english-distilroberta-base", 
    return_all_scores=True,
)

def analyze_emotion(text):
    scores = emotion_model(text)[0]
    top_emotion = max(scores, key=lambda x: x["score"])
    return top_emotion["label"], round(top_emotion["score"], 2)