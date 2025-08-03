# 🧠 Clasificador de URLs Spam con Streamlit y SVM

Para el desarrollo de una aplicación web usando **Streamlit**, hemos utilizado un modelo supervisado SVM (Support Vector Machine) entrenado y desallorado previamente que predice si una URL es **spam** o **no spam**.

---

## 🗂️ Estructura del Repositorio

```plaintext
main/
├── src/
│   ├── static/
│   │   └── alarm.wav          # Sonido de alerta si se detecta spam
│   ├── 12-opt-svm-model.pkl   # Modelo SVM entrenado
│   ├── 12-vectorizer          # Vectorizador TF-IDF para transformar el texto
│   ├── utils1.py              # Funciones de preprocesamiento y lematización
│   ├── app.py                 # Aplicación principal en Streamlit
├── .env                       # Variables del entorno para el desarrollo local
├── .env.example               # Archivo del entorno de ejemplo (plantilla)
├── .gitignore                 # Git ignored files configuration
├── README.es.md               # Documentacion del proyecto en español
├── README.md                  # Documentacion del proyecto en ingles
└── requirements.txt           # Librerías necesarias

```

## ⚙️ Desarrollo de la Aplicación

1. **Modelo de Machine Learning**
   - Entrenado con un algoritmo SVM para clasificar URLs como spam o no spam.
   - Utikiza preprocesamiento de texto, lematización y vectorización TF-IDF.

2. **Preprocesamiento del texto del usuario**
   - Implementado en `utils1.py`:
     - Limpieza y normalización del texto.
     - Lematización de palabras.
     - Eliminación de símbolos, palabras cortas y stopwords.

3. **Interfaz Web con Streamlit**
   - Interfaz interactiva y moderna con fondo animado tipo gradiente dinámico.
   - El botón **Clasificar** muestra si la URL es segura o spam:
     - Si es spam:
       - Se muestra el mensaje “⚠️ ¡¡¡SPAM DETECTADO!!!” con animación de parpadeo.
       - Se reproduce un sonido de alerta.
     - Si no es spam:
       - Se ofrece un enlace clicable para abrir la URL en una nueva pestaña.
   - Botones personalizados siempre visibles: `Clasificar`, `Enviar valoración` y `Limpiar`.
   - El botón **Limpiar** borra tanto la URL introducida como el mensaje de predicción.

4. **Sin necesidad de servidor**
   - Streamlit ejecuta la app directamente sin necesidad de configurar un servidor web (como Flask o Gunicorn).

---

## 🚀 Despliegue 

La aplicación ha sido desplegada en la plataforma **Streamlit**. Puedes acceder a la versión en línea desde el siguiente enlace:

🔗 [https://pablo-aznar-spam-url-classifier.streamlit.app/](https://pablo-aznar-spam-url-classifier.streamlit.app/)
