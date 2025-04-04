from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

# Charger les éléments
ohe = joblib.load("models/ohe_encoder_cb.pkl")
scaler = joblib.load("models/scaler_cb.pkl")
knn = joblib.load("models/knn_model.pkl")
df = pd.read_csv("data/df_clean.csv", sep=';', index_col="Monture_ID")

# 🔧 Vérifier et nettoyer la colonne 'Taille' si nécessaire
if "Taille" in df.columns:
    df['Taille'] = df['Taille'].astype(str).str.replace(r'\s+', '', regex=True)
    taille_split = df['Taille'].str.split('-', expand=True)

    for i in range(3):
        if i not in taille_split.columns:
            taille_split[i] = 0

    df['Taille_Lens'] = pd.to_numeric(taille_split[0], errors='coerce')
    df['Taille_Bridge'] = pd.to_numeric(taille_split[1], errors='coerce')
    df['Taille_Temple'] = pd.to_numeric(taille_split[2], errors='coerce')

    df.drop(columns=['Taille'], inplace=True)

# Init API
app = FastAPI(
    title="API Recommandation Montures",
    description="🔎 Cette API recommande des montures en fonction du profil utilisateur saisi dans un formulaire. Elle repose sur un modèle KNN pré-entraîné.",
    version="1.0.0",
    contact={
        "name": "Segodo Ulrich",
        "email": "segodoulrich21@gmail.com",
        "url": "https://www.linkedin.com/in/ulrich-segodo/"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    }
)


# Schéma d’entrée utilisateur
class ProfilUtilisateur(BaseModel):
    Genre: str
    Marque: str
    Type: str
    Forme: str
    Materiau: str
    Couleur: str
    Style: str
    Age: int
    Taille_Lens: int
    Taille_Bridge: int
    Taille_Temple: int

@app.get("/info")
def info():
    return {
        "description": "🔎 API de recommandation de montures basée sur le profil utilisateur.",
        "usage": "Envoyez une requête POST à /recommander avec les informations du formulaire pour obtenir une liste personnalisée de montures.",
        "champs_obligatoires": [
            "Genre", "Marque", "Type", "Forme", "Materiau", "Couleur", "Style",
            "Age", "Taille_Lens", "Taille_Bridge", "Taille_Temple"
        ],
        "exemple_requete": {
            "Genre": "Homme",
            "Marque": "Ray-Ban",
            "Type": "Cerclée",
            "Forme": "Rectangulaire",
            "Materiau": "Acier",
            "Couleur": "Noir",
            "Style": "Business",
            "Age": 32,
            "Taille_Lens": 54,
            "Taille_Bridge": 18,
            "Taille_Temple": 140
        },
        "endpoint_recommandation": "POST /recommander"
    }


@app.post("/recommander")
def recommander(profil: ProfilUtilisateur):
    # ✅ Encodage
    data = pd.DataFrame([profil.model_dump()])
    profil_cat = ohe.transform(data[ohe.feature_names_in_])
    profil_num = scaler.transform(data[['Age', 'Taille_Lens', 'Taille_Bridge', 'Taille_Temple']])
    profil_encoded = np.hstack([profil_cat, profil_num])


    # Recommandation
    distances, indices = knn.kneighbors(profil_encoded)
    ids = df.index[indices[0]].tolist()

    recommandations = []
    for id_ in ids:
        m = df.loc[id_]
        recommandations.append({
            "id": id_,
            "Marque": m['Marque'],
            "Forme": m['Forme'],
            "Style": m['Style'],
            "Couleur": m['Couleur'],
            "Taille": f"{m['Taille_Lens']}-{m['Taille_Bridge']}-{m['Taille_Temple']}"
        })

    return {"montures_recommandees": recommandations}
