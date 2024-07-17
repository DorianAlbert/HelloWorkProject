# Utiliser l'image Python 3.9 slim comme base
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur
COPY requirements.txt requirements.txt

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

# Définir le point d'entrée du conteneur pour exécuter votre programme principal
CMD ["python", "script/main.py"]

RUN cd script