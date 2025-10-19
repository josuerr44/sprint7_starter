import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# ==============================
# CONFIGURACIÓN DE LA PÁGINA
# ==============================
st.set_page_config(
    page_title="Vehicle Data Dashboard",
    layout="wide",
)

# ==============================
# FUNCIÓN PARA CARGAR FONDO LOCAL EN BASE64
# ==============================
def get_base64_of_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Cargar imagen GT3-EVO desde el mismo directorio
encoded_image = get_base64_of_image("gt3-evo.jpg")

# ==============================
# CSS CORREGIDO (USA BASE64)
# ==============================
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)), 
                      url("data:image/jpg;base64,{encoded_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
[data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stToolbar"] {{
    background: rgba(0, 0, 0, 0);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ==============================
# CARGA DE DATOS
# ==============================
df = pd.read_csv("vehicles_sample.csv", encoding="latin1")

# ==============================
# TÍTULO PRINCIPAL
# ==============================
st.title("🚗 Vehicle Data Visualization Dashboard")
st.markdown("### Analyze vehicle data interactively with histograms and scatter plots.")

# ==============================
# CONTROLES DE VISUALIZACIÓN
# ==============================
st.subheader("🎛️ Visualization Controls")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📦 Select column for histogram**")
    x_hist = st.selectbox(
        "Choose variable to visualize distribution",
        df.columns,
        index=df.columns.get_loc("manufacturer") if "manufacturer" in df.columns else 0
    )

with col2:
    st.markdown("**📈 X axis (scatter plot)**")
    x_scatter = st.selectbox(
        "Choose variable for horizontal axis",
        df.columns,
        index=df.columns.get_loc("odometer") if "odometer" in df.columns else 0
    )

with col3:
    st.markdown("**📉 Y axis (scatter plot)**")
    y_scatter = st.selectbox(
        "Choose variable for vertical axis",
        df.columns,
        index=df.columns.get_loc("price") if "price" in df.columns else 0
    )

# ==============================
# OPCIONES DE MOSTRADO
# ==============================
show_hist = st.checkbox("📊 Show histogram", value=True)
show_scatter = st.checkbox("📈 Show scatter plot", value=True)

# ==============================
# GENERACIÓN DE GRÁFICAS
# ==============================
col_a, col_b = st.columns(2)

if show_hist:
    with col_a:
        st.markdown(f"### Histogram for `{x_hist}`")
        fig = px.histogram(df, x=x_hist, opacity=0.7)
        fig.update_traces(
            marker_color='rgba(0,255,255,0.6)',
            marker_line_color='rgba(255,255,255,0.2)'
        )
        st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    with col_b:
        st.markdown(f"### Scatter plot `{x_scatter}` vs `{y_scatter}`")
        fig2 = px.scatter(df, x=x_scatter, y=y_scatter, opacity=0.7)
        fig2.update_traces(
            marker=dict(
                color='rgba(0,255,255,0.7)',
                line=dict(width=0.5, color='rgba(255,255,255,0.3)')
            )
        )
        st.plotly_chart(fig2, use_container_width=True)

# ==============================
# FIRMA FINAL (EN INGLÉS)
# ==============================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; opacity: 0.9; font-size: 14px;'>
        <span style='color: #CCCCCC;'>Developed by <b>Josué Rodríguez</b> — Data Analyst | <b>Nennu</b></span>
    </div>
    """,
    unsafe_allow_html=True
)