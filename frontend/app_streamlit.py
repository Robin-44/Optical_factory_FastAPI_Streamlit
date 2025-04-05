import streamlit as st
import requests

# URL de ton API (à adapter selon ton déploiement)
API_URL = "https://optical-api.onrender.com/recommander"

# Valeurs disponibles pour le formulaire
genres = ["Homme", "Femme", "Non-binaire"]
marques = ["Oakley", "Ray-Ban", "Persol", "Gucci", "Chanel"]
types = ["Cerclée", "Semi-cerclee", "Invisible"]
couleurs = ["Transparent", "Ecaille", "Noir", "Argent", "Bleu", "Dore"]
formes = ["Ronde", "Aviateur", "Rectangulaire", "Papillon"]
materiaux = ["Plastique", "Metal", "Titane"]
styles = ["Sport", "Business", "Luxe", "Casual"]

st.set_page_config(page_title="Recommandation de Montures", layout="centered")
st.title("🕶️ Recommandation personnalisée de lunettes")

st.markdown("Remplis ce formulaire pour obtenir des suggestions de montures qui te correspondent :")

with st.form("formulaire_monture"):
    col1, col2 = st.columns(2)

    with col1:
        genre = st.selectbox("Genre", genres)
        marque = st.selectbox("Marque", marques)
        type_ = st.selectbox("Type de monture", types)
        forme = st.selectbox("Forme", formes)

    with col2:
        materiau = st.selectbox("Matériau", materiaux)
        couleur = st.selectbox("Couleur", couleurs)
        style = st.selectbox("Style", styles)
        age = st.number_input("Âge", min_value=10, max_value=100, value=30)

    st.markdown("### Dimensions de la monture")
    taille_lens = st.number_input("Taille Lens (mm)", min_value=30, max_value=80, value=54)
    taille_bridge = st.number_input("Taille Bridge (mm)", min_value=10, max_value=30, value=18)
    taille_temple = st.number_input("Taille Temple (mm)", min_value=100, max_value=160, value=140)

    submit = st.form_submit_button("🔍 Obtenir mes recommandations")

if submit:
    with st.spinner("Analyse de ton profil..."):
        payload = {
            "Genre": genre,
            "Marque": marque,
            "Type": type_,
            "Forme": forme,
            "Materiau": materiau,
            "Couleur": couleur,
            "Style": style,
            "Age": age,
            "Taille_Lens": taille_lens,
            "Taille_Bridge": taille_bridge,
            "Taille_Temple": taille_temple
        }

        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status()
            result = response.json()

            st.success("Voici les montures recommandées pour toi :")
            montures = result["montures_recommandees"]
            icon_url = "https://cdn-icons-png.flaticon.com/512/7501/7501225.png"  # Icône lunettes stylée

            for i in range(0, len(montures), 2):
                cols = st.columns(2)
                for j in range(2):
                    if i + j < len(montures):
                        reco = montures[i + j]
                        with cols[j]:
                            st.image(icon_url, width=80)
                            st.markdown(f"**Marque :** {reco['Marque']}")
                            st.markdown(f"**Forme :** {reco['Forme']}")
                            st.markdown(f"**Style :** {reco['Style']}")
                            st.markdown(f"**Couleur :** {reco['Couleur']}")
                            st.markdown("---")

        except Exception as e:
            st.error("Une erreur est survenue. Veuillez vérifier l'API ou vos données.")
            st.exception(e)
