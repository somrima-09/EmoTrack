import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import numpy as np

from model import analyze_emotion
from data_handling import load_journal, save_entry
from visualization import plot_mood_bar, plot_mood_pie

journal_df=load_journal()

st.title("EmoTrack")
st.subheader("How are you feeling today?")

entry = st.text_area("Write your thoughts...", height=200)

if(st.button("Analyze Emotion")):
    if(entry.strip()):
        emotion, score= analyze_emotion(entry)
        st.success(f"Detect Emotion **{emotion}** with confidence **{score}**")

        save_entry(entry, emotion, score)
        journal_df = load_journal()     # Refresh after adding
    else:
        st.warning("Please write something before analyzing.")

# Show journal table
with st.expander("📓 View Past Entries"):
    st.dataframe(journal_df[["Date", "Emotion", "Score"]].sort_values(by="Date", ascending=False))

# Show mood graph
if not journal_df.empty:
    st.subheader("📊 Mood Overview")
    plot_mood_bar(journal_df)

    st.subheader("🧁 Emotion Distribution Pie")
    plot_mood_pie(journal_df)

#Emotion Trend Line
st.subheader("**📈  Emotion Frequency per Day**")
journal_df['Date'] = pd.to_datetime(journal_df['Date'])

# Count frequency of each emotion per day
emotion_counts = journal_df.groupby(['Date', 'Emotion']).size().reset_index(name='Frequency')

# Add small vertical jitter only for plotting
np.random.seed(42)
emotion_counts['y_plot'] = emotion_counts['Frequency'] + np.random.uniform(-0.1, 0.1, size=len(emotion_counts))

fig = px.scatter(
    emotion_counts,
    x='Date',
    y='y_plot',                 # jittered for visibility
    color='Emotion',
    size='Frequency',            # size reflects actual frequency
    hover_data=['Emotion', 'Frequency'],  # shows real frequency
    title="Emotion Occurrences Over Time"
)
fig.update_yaxes(showticklabels=False, title='')
st.plotly_chart(fig, use_container_width=True)

#Suggestions
st.subheader("💡 Well-being Suggestion")
recent_df = journal_df.tail(7)   # last 7 entries
if not recent_df.empty:
    dominant_emotion = recent_df["Emotion"].mode()[0]
dominant_emotion = dominant_emotion.capitalize()
emotion_suggestions = {
    "Joy": "Keep up the good vibes! Maybe share your happiness with a friend 😊",
    "Sadness": "Take a short walk or write down 3 things you're grateful for 🌱",
    "Anger": "Try some deep breathing exercises or listen to calming music 🎶",
    "Fear": "Talk to someone you trust or try journaling about your worries ✍️",
    "Disgust": "Do something uplifting—watch a comedy or spend time outdoors 🌸",
    "Neutral": "Use this calm moment to plan your goals or do something creative 🌞"
}

suggestion = emotion_suggestions.get(dominant_emotion, "Take care of yourself today 💙")
st.info(f"Suggestion: {suggestion}")

# CSV Export
st.markdown("### 📥 Export Your Journal")
if not journal_df.empty:
    csv = journal_df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Journal as CSV", data=csv, file_name="mindscope_journal.csv", mime='text/csv')
else:
    st.info("Add entries to enable download.")

