# Utiliser une image Python officielle
FROM python:3.12-slim

# Créer le dossier de travail
WORKDIR /app

# # Copier les fichiers nécessaires
# COPY ./app.py ./requirements.txt ./models ./data ./

# # Installer les dépendances
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier toute l'application (y compris les modèles et données)
COPY . .


# Exposer le port par défaut de l'API
EXPOSE 8000

# Commande pour démarrer l'API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
