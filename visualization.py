import matplotlib.pyplot as plt
import streamlit as st

def plot_mood_bar(df):
    mood_counts = df['Emotion'].value_counts()
    fig, ax = plt.subplots()
    mood_counts.plot(kind='bar', color='lightgreen', ax=ax)
    ax.set_title("Most Frequent Emotions")
    ax.set_ylabel("Count")
    ax.set_xlabel("Emotion")
    st.pyplot(fig)

def plot_mood_pie(df):
    mood_counts = df['Emotion'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(
        mood_counts, 
        labels=mood_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=plt.cm.Pastel1.colors
    )
    ax.set_title("Emotion Distribution")
    st.pyplot(fig)