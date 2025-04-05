# 🕶 Optical Factory Recommender

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

Une application de recommandation de montures de lunettes avec une API FastAPI puissante et un frontend utilisateur avec Streamlit. Parfait pour recommander des lunettes personnalisées selon le profil utilisateur.

## 🌟 Fonctionnalités

- **API REST** de recommandation de montures à partir de modèles Machine Learning
- **Interface utilisateur Streamlit** avec formulaire dynamique
- **Visualisation des recommandations** avec icônes et description des montures
- **Déploiement Render + Streamlit Cloud**

## 📂 Structure du projet

```
optical_factory/
├── backend/
│   ├── app.py                  # API FastAPI principale
│   ├── Dockerfile              # Fichier de déploiement Render
│   ├── requirements.txt        # Dépendances FastAPI
│   ├── models/                 # Modèles ML : encoder, scaler, KNN
│   └── data/                   # Dataset nettoyé au format CSV
├── frontend/
│   ├── app_streamlit.py        # Interface Streamlit
│   ├── requirements.txt        # Dépendances Streamlit
└── README.md                   # Ce fichier
```

## ⚙️ Installation

### Prérequis

- Python 3.12+
- `uv` (optionnel mais recommandé)

### Installation backend

```bash
cd backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
uvicorn app:app --reload
```

API disponible sur : `http://localhost:8000`  
Documentation Swagger : `http://localhost:8000/docs`

### Installation frontend

```bash
cd frontend
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
streamlit run app_streamlit.py
```

Application accessible par défaut sur : `http://localhost:8501`

## 📊 Fonctionnement de l'application

1. L'utilisateur remplit le formulaire avec : genre, marque, forme, style, dimensions...
2. Ces données sont envoyées à l'API via `POST /recommander`
3. L'API renvoie les 10 montures les plus proches selon le modèle KNN
4. Le frontend Streamlit affiche les résultats joliment (icône + infos)

## 💼 Champs du formulaire

- Genre : `Homme`, `Femme`, `Non-binaire`
- Marque : `Ray-Ban`, `Gucci`, `Chanel`, etc.
- Forme : `Aviateur`, `Papillon`, `Ronde`, etc.
- Type : `Cerclée`, `Invisible`, `Semi-cerclee`
- Style : `Sport`, `Business`, `Casual`, `Luxe`
- Couleur : `Noir`, `Transparent`, `Dore`, etc.
- Matériau : `Titane`, `Plastique`, `Metal`
- Age, Taille_Lens, Taille_Bridge, Taille_Temple : `int`

## 🧰 Déploiement

- **Backend (FastAPI)** : Render avec Dockerfile
- **Frontend (Streamlit)** : Streamlit Cloud avec `app_streamlit.py` et `requirements.txt`

## 🧹 Dépendances principales

### Backend
- fastapi
- uvicorn
- pandas
- numpy
- joblib
- scikit-learn

### Frontend
- streamlit
- requests

## 💻 Licence

Ce projet est sous licence **MIT**.

```txt
MIT License

Copyright (c) 2025 Segodo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

