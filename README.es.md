# 🧠 Clasificador de URLs Spam con Flask y SVM

Para el desarrollo de una aplicación web usando **Flask**, hemos utilizado un modelo supervisado SVM (Support Vector Machine) entrenado y desallorado previamente que predice si una URL es **spam** o **no spam**.

---

## 🗂️ Estructura del Repositorio

src/
├── static/
│ └── alarm.wav # Sonido que se reproduce si se detecta spam
├── templates/
│ └── index.html # Interfaz web personalizada de la aplicación
├── 12-opt-svm-model.pkl # Modelo SVM entrenado 
├── 12-vectorizer # Vectorizador TF-IDF necesario para transformar el texto
├── requirements.txt # Dependencias del proyecto
├── utils1.py # Funciones de preprocesamiento y lematización
└── app.py # Lógica principal de la aplicación Flask


---

## ⚙️ Desarrollo de la Aplicación

1. **Modelo supervisado de Machine Learning**
   - Entrenado con SVM para clasificar URLs como spam o no spam.
   - Utiliza un preprocesador de texto,lematizador y vectorizador TF-IDF para transformar las URLs antes de la predicción.

2. **Preprocesamiento del texto introducido por el usuario**
   - Funciones implementadas en `utils1.py`, donde:
     - Se normaliza el texto (minúsculas, eliminación de símbolos).
     - Se lematiza cada palabra.
     - Se eliminan stopwords y palabras cortas.

3. **Interfaz Web (`index.html`)**
   - Basado en **Bootstrap** con tema `darkly` para un diseño moderno.
   - Fondo animado usando **tsParticles** simulando meteoritos.
     - Si la predicción es spam:
       - Los meteoritos se mueven más rápido.
       - Se reproduce un sonido de alerta cada 2 segundos.
       - El mensaje de “¡¡¡SPAM DETECTADO!!!” parpadea en rojo.
     - Al pulsar el botón “Limpiar”:
       - Se detiene el sonido.
       - Se reduce la velocidad de las partículas a la normal.
   - Formulario para ingresar una URL y botón para clasificar o limpiar.

4. **Lógica principal (`app.py`)**
   - Carga el modelo SVM y el vectorizador.
   - Preprocesa, lematiza y vectoriza la URL introducida por el usuario.
   - Realiza la predicción.
   - Renderiza el resultado con la interfaz HTML.

5. **Servidor local**
   - Se ha utilizado **gunicorn** para lanzar el servidor local y probar la aplicación antes de desplegarla.

---

## 🚀 Despliegue en Render

La aplicación ha sido desplegada en la plataforma **Render**. Puedes acceder a la versión en línea desde el siguiente enlace:

🔗 [https://spam-url-detected-flask.onrender.com](https://spam-url-detected-flask.onrender.com)