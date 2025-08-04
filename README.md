# 🧠 Spam URL Classifier with Streamlit and SVM

For the development of a web application using **Streamlit**, we used a previously trained and developed supervised **SVM (Support Vector Machine)** model that predicts whether a URL is **spam** or **not spam**.

---

## 🗂️ Repository Structure

```plaintext
main/
├── src/
│   ├── static/
│   │   └── alarm.wav          # Alert sound played if spam is detected
│   ├── 12-opt-svm-model.pkl   # Trained SVM model
│   ├── 12-vectorizer          # TF-IDF vectorizer used to transform the input text
│   ├── utils1.py              # Text preprocessing and lemmatization functions
│   ├── app.py                 # Main Streamlit application
├── .env                       # Environment variables for local development
├── .env.example               # Example environment configuration file
├── .gitignore                 # Git ignore file configuration
├── README.es.md               # Project documentation in Spanish
├── README.md                  # Project documentation in English
└── requirements.txt       # Required Python libraries

```

⚙️ Application Overview

1. **Machine Learning Model**
   - Trained using an SVM algorithm to classify URLs as spam or not spam.
   - Uses text preprocessing, lemmatization, and TF-IDF vectorization.

2. **User Text Preprocessing**
   - Implemented in `utils1.py`:
     - Text cleaning and normalization.
     - Word lemmatization.
     - Removal of symbols, short words, and stopwords.

3. **Web Interface with Streamlit**
   - Interactive and modern UI with an animated dynamic gradient background.
   - The **Classify** button determines whether the entered URL is safe or spam:
     - If spam:
       - A blinking warning message “⚠️ SPAM DETECTED!!!” is shown.
       - An alert sound is played.
     - If not spam:
       - A clickable link is provided to open the URL in a new tab.
   - Custom buttons are always visible: `Classify`, `Submit Rating`, and `Clear`.
   - The **Clear** button removes both the entered URL and the prediction message.

4. **No Web Server Needed**
   - Streamlit runs the app directly without the need for a web server (unlike Flask or Gunicorn). Terminal: streamlit run src/app.py

🚀 Deployment

The application has been deployed on the Streamlit platform. You can access the online version via the following link

🔗 [https://pablo-aznar-spam-url-classifier.streamlit.app/](https://pablo-aznar-spam-url-classifier.streamlit.app/)