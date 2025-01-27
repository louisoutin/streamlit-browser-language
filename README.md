# Streamlit Browser Language Detector

A Streamlit component that detects the user's browser language and allows you to customize your app's content based on the detected language.

---

## **Installation**

You can install the component via pip:

```bash
pip install streamlit-browser-language
```

---

## **Usage**

### **Basic Usage**

To detect the user's browser language and display content accordingly:

```python
import streamlit as st
from language_detection import detect_browser_language

# Detect the browser language
browser_language = detect_browser_language()

# Display content based on the detected language
if browser_language.startswith('es'):
    st.write("¡Hola! Bienvenido a nuestra aplicación.")
elif browser_language.startswith('fr'):
    st.write("Bonjour! Bienvenue dans notre application.")
else:
    st.write("Hello! Welcome to our application.")

# Display the detected language for debugging
st.write(f"Detected browser language: {browser_language}")
```

---

### **Function Parameters**

The `detect_browser_language` function has the following parameters:

| Parameter   | Type               | Default | Description                                                                 |
|-------------|--------------------|---------|-----------------------------------------------------------------------------|
| `timeout`   | `Union[int, float]`| `5`     | Maximum time (in seconds) to wait for the language detection.               |
| `interval`  | `Union[int, float]`| `0.1`   | Interval (in seconds) to check for the language detection result.           |
| `key`       | `str`              | `"browser_language"` | A unique key for the component to avoid conflicts.                     |

---

## **How It Works**

1. The component uses the `navigator.language` property in the browser to detect the user's preferred language.
2. The detected language is sent back to the Streamlit app, where you can use it to customize the content.
3. The component is invisible and does not affect the layout of your app.

---

## **Example Output**

If the user's browser language is set to `es-ES` (Spanish), the app might display:

```
¡Hola! Bienvenido a nuestra aplicación.
Detected browser language: es-ES
```

If the user's browser language is set to `fr-FR` (French), the app might display:

```
Bonjour! Bienvenue dans notre application.
Detected browser language: fr-FR
```

For all other languages, the app defaults to English:

```
Hello! Welcome to our application.
Detected browser language: en-US
```

---

## **Development**

### **Setting Up the Development Environment**

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/streamlit-browser-language-detector.git
   cd streamlit-browser-language-detector
   ```

2. Navigate to the `frontend` directory and install dependencies:

   ```bash
   cd language_detection/frontend
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

4. In a separate terminal, run the Streamlit app (set RELEASE to False for development in __init__.py):

   ```bash
   streamlit run example.py
   ```

---

### **Building for Production**

1. Build the React component:

   ```bash
   cd language_detection/frontend
   npm run build
   ```

2. Package and distribute the component:

   ```bash
   python setup.py sdist bdist_wheel
   twine upload dist/*
   ```

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

---

## **Acknowledgments**

- Built with [Streamlit](https://streamlit.io/) and [React](https://reactjs.org/).
- Inspired by the need for multilingual support in Streamlit apps.