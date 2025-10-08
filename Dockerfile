# Utilise une image Python légère
FROM python:3.11-slim

# Crée un dossier de travail
WORKDIR /app

# Copie les dépendances
COPY requirements.txt

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définit la commande de démarrage
CMD ["python", "main.py"]
