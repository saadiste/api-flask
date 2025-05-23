# API Flask avec  Déploiement Kubernetes

Ce projet est une **API Flask** déployée sur un cluster **Kubernetes** avec support de **PostgreSQL**,. Il s'agit d'un TP éducatif pour apprendre à  conteneuriser et orchestrer des applications.

## La Structure du projet

```
api-flask/
-app.py                  # Application Flask principale
-requirements.txt        # Dépendances Python
-Dockerfile              # Image Docker Flask
-flask-deployment.yaml   # Déploiement et service Flask
-postgres.yaml           # Déploiement et service PostgreSQL
-NetworkPolicy.yaml      # Politique réseau (optionnelle)
-tls/                    # Certificats TLS si besoin
```

##Prérequis

- Python 3.8+
- pip
- Docker
- Kubernetes (Minikube, MicroK8s, RKE, etc.)
- Accès `kubectl` fonctionnel

##  Lancement local (dÃ©veloppement)

1. **Cloner le projet**

```bash
git clone https://github.com/saadiste/api-flask.git
cd api-flask
```

2. **Créer et activer lâ€™environnement virtuel**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Installer les dÃ©pendances**

```bash
pip install -r requirements.txt
```

4. **Lancer l'application localement**

```bash
python app.py
```

Elle est disponible sur : [http://localhost:5000](http://localhost:5000)

##  Construction et exÃ©cution Docker

1. **Construire lâ€™image Docker**

```bash
docker build -t flask-api:2.0 .
```

2. **Lancer l'image localement**

```bash
docker run -d -p 5000:5000 flask-api:latest
```

## Déploiement Kubernetes

1. **Appliquer les ressources :**

```bash
kubectl apply -f postgres.yaml
kubectl apply -f flask-deployment.yaml
kubectl apply -f NetworkPolicy.yaml        # Optionnel
```

2. **VÃ©rifier les pods et services**

```bash
kubectl get pods
kubectl get svc
```





## ðŸ” Authentification GitHub avec Token

GitHub **nâ€™accepte plus les mots de passe**. Utilise un **Personal Access Token (PAT)** Ã  la place.

1. Génère un token ici : [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Lors du `git push`, utilise ton **username** et ce **token** comme mot de passe.

### Exemple :

```bash
git add .
git commit -m "update"
git push origin master
```

Git te demandera :

- Username â†’ `ton_username`
- Password â†’ **colle le PAT**

## Endpoints de l'API (exemples)

- `GET /` â†’ Message de bienvenue
- `GET /api/data` â†’ Retourne des donnÃ©es statiques
- `POST /api/data` â†’ Ajoute des donnÃ©es

## Auteur

**Nizar Saadi**

## Licence

Ce projet est sous licence MIT.
