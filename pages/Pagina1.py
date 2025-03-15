import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="p5.js en Streamlit con iframe", layout="wide")

st.title("Integración de p5.js en Streamlit mediante iframe")
st.markdown("Esta aplicación demuestra cómo integrar un sketch de p5.js existente usando iframe")

# URL de tu sketch p5.js - reemplaza con la URL de tu sketch
sketch_url = "https://editor.p5js.org/denunciadorufian492/embed/LYK9Kt-rQ"

# Algunos controles opcionales para la visualización
st.sidebar.header("Opciones de visualización")
iframe_height = st.sidebar.slider("Altura del iframe (px)", 300, 800, 500)
show_border = st.sidebar.checkbox("Mostrar borde", False)

# Estilo del iframe basado en las opciones
border_style = "1px solid #ddd" if show_border else "none"

# Usar components.iframe para mostrar el sketch externo
st.markdown(f"Visualizando sketch desde: `{sketch_url}`")
components.iframe(
    src=sketch_url, 
    height=iframe_height, 
    scrolling=False,
    width="100%",
    style=f"border: {border_style};"
)

# Instrucciones para el usuario
st.markdown("""
## Cómo usar este código

1. Reemplaza la URL de ejemplo con la URL de tu propio sketch de p5.js
2. Los sketches pueden provenir de:
   - editor.p5js.org (usando la opción "embed")
   - GitHub Pages
   - Cualquier servidor web donde tengas alojado tu sketch
3. Ajusta la altura y otras opciones según sea necesario en la barra lateral
""")
