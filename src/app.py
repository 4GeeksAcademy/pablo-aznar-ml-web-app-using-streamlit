from flask import Flask, request, render_template
from pickle import load
from utils1 import preprocess_text, lemmatize_text

app = Flask(__name__)

# Cargamos el modelo y el vectorizado
model = load(open('12-opt-svm-model.pkl', 'rb'))
vectorizer  = load(open('12-vectorizer.pkl', 'rb'))

class_dict = {"0": "No es spam",
              "1": "Es spam"}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', prediction=None, val=None)
    
    if request.method == "POST":
        val1 = request.form["val1"]
        tokens = preprocess_text(val1)
        lemmatized_tokens = lemmatize_text(tokens)
        text_processed = " ".join(lemmatized_tokens)
        
        data = vectorizer.transform([text_processed]).toarray()
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
        
        return render_template('index.html', prediction=pred_class, val=val1)
    return None


if __name__ == '__main__':
    # PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=3000, debug=True)
