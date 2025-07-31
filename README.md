# 🧠 Spam URL Classifier with Flask and SVM

For the development of a web application using **Flask**, we have used a pre-trained supervised SVM (Support Vector Machine) model that predicts whether a URL is **spam** or **not spam**.

---

## 🗂️ Repository Structure

```plaintext
main/
├── src/
│   ├── static/
│   │   └── alarm.wav          # Sound played when spam is detected
│   ├── templates/
│   │   └── index.html         # Custom web interface of the application
│   ├── 12-opt-svm-model.pkl   # Trained SVM model
│   ├── 12-vectorizer          # TF-IDF vectorizer needed to transform the text
│   ├── requirements.txt       # Required libraries
│   ├── utils1.py              # Preprocessing and lemmatization functions
│   └── app.py                 # Main logic of the Flask application
├── .env                       # Environment variables for local development
├── .env.example               # Example environment file (template)
├── .gitignore                 # Git ignored files configuration
├── README.es.md               # Project documentation in Spanish
└── README.md                  # Project documentation in English

```


## ⚙️ Application Development

1. **Machine Learning Model**  
   - Trained with SVM to classify URLs as spam or not spam.  
   - Uses a TF-IDF vectorizer to transform URLs before prediction.

2. **Text Preprocessing**  
   - Implemented in `utils1.py`, where:  
     - Text is normalized (lowercase, symbol removal).  
     - Each word is lemmatized.  
     - Stopwords and short words are removed.

3. **Web Interface (`index.html`)**  
   - Based on **Bootstrap** with the `darkly` theme for a modern design.  
   - Animated background using **tsParticles** simulating meteors.  
     - If the prediction is spam:  
       - Meteors move faster.  
       - An alert sound plays every 2 seconds.  
       - The message “!!!SPAM DETECTED!!!” blinks in red.  
     - When pressing the “Clear” button:  
       - The sound stops.  
       - The particle speed returns to normal.  
   - Form to enter a URL and buttons to classify or clear.

4. **Main Logic (`app.py`)**  
   - Loads the SVM model and vectorizer.  
   - Preprocesses, lemmatizes, and vectorizes the input URL.  
   - Performs the prediction.  
   - Renders the result with the HTML interface.

5. **Local Server**  
   - **Gunicorn** is used to launch the local server and test the application before deployment.

---

## 🚀 Deployment on Render

The application has been deployed on the **Render** platform. You can access the online version at the following link:

🔗 [https://spam-url-detected-flask.onrender.com](https://spam-url-detected-flask.onrender.com)