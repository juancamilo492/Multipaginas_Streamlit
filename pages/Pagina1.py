import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="p5.js en Streamlit", layout="wide")

st.title("Integración de p5.js en Streamlit")

# URL de tu sketch p5.js
sketch_url = "https://editor.p5js.org/denunciadorufian492/embed/LYK9Kt-rQ"

# Altura del iframe
iframe_height = 500

# Usar components.html en lugar de components.iframe
html_code = f"""
<div style="display: flex; justify-content: center;">
    <iframe 
        src="{sketch_url}" 
        width="100%" 
        height="{iframe_height}" 
        style="border: none; overflow: hidden;">
    </iframe>
</div>
"""

# Renderizar el HTML con el iframe
components.html(html_code, height=iframe_height + 20)
