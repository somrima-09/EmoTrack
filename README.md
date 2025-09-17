# EmoTrack  
A journaling and emotion-tracking web application that helps users monitor their emotional well-being over time.  



## Demo  
- [Demo Link](https://drive.google.com/file/d/1eOtbNht_bxOFS29ck9KLOvYrM4gTPxsC/view?usp=sharing)  




## Features  
- Daily journaling: Log journal entries to track thoughts and emotions.  
- Emotion detection: Uses a fine-tuned NLP model to classify emotions (joy, sadness, anger, fear, disgust, neutral).  
- Mood trends: Visualizes emotional patterns over time with interactive charts.  
- Personalized suggestions: Provides well-being tips based on recent dominant emotions.  
- Data export: Download the journal history as CSV for offline use.  



## Tech Stack  
- **Frontend/UI**: Streamlit (Python)  
- **Backend Logic**: Hugging Face Transformers (local pipeline)  
- **Data Storage**: CSV file (`journal.csv`)  
- **Visualization**: Matplotlib, Streamlit charts  
- **ML Model**: DistilRoBERTa (fine-tuned for emotion classification)  


## Used By  
- Students exploring mental health and AI applications  
- Individuals interested in tracking and improving emotional well-being  



## FAQ  
**Q: How do I log my emotions?**  
A: Enter a journal entry in the app; the model will automatically classify the emotion.  

**Q: Can I track trends over time?**  
A: Yes. Weekly and monthly emotion trends are visualized with charts.  

**Q: Are the suggestions personalized?**  
A: Yes. Suggestions are generated based on recent dominant emotions.  



## Author  
- [@SomrimaSaha](https://github.com/somrima-09) 
