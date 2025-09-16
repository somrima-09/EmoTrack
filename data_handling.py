import pandas as pd
from datetime import datetime

FILENAME = "journal.csv"

def load_journal():
    try:
        df = pd.read_csv(FILENAME)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        # Drop rows where Date failed to parse
        df = df.dropna(subset=["Date"])

        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Entry", "Emotion", "Score"])


def save_entry(entry, emotion, score):
    df = load_journal()
    new_row = {
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Entry": entry,
        "Emotion": emotion,
        "Score": score
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(FILENAME, index=False)
