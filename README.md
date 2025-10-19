# Sprint 7 — Panel web con Streamlit (Starter Pack)

Este repo es tu punto de partida para el proyecto:
- `app.py`: app de Streamlit con histograma y dispersión (usa `plotly_express`).
- `requirements.txt`: dependencias mínimas.
- `notebooks/EDA.ipynb`: cuaderno inicial para EDA.
- **Recuerda** colocar `vehicles_us.csv` en la raíz del proyecto (mismo nivel que `app.py`).

## Cómo ejecutar localmente
```bash
# 1) Crea y activa tu entorno (ejemplo con conda)
conda create -n vehicles_env python=3.11 -y
conda activate vehicles_env

# 2) Instala dependencias
pip install --upgrade pip
pip install -r requirements.txt

# 3) Ejecuta la app
streamlit run app.py
```

## Estructura esperada por el revisor
```
.
├── README.md
├── app.py
├── vehicles_us.csv        # (colócalo aquí)
├── requirements.txt
└── notebooks
    └── EDA.ipynb
```

## Despliegue en Render (resumen)
- Conecta tu GitHub a Render.
- Crea un **Web Service** apuntando a este repo.
- **Build Command**:
  `pip install --upgrade pip && pip install -r requirements.txt`
- **Start Command**:
  `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
