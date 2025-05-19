# ðŸ§ª API Flask â€“ DÃ©ploiement Kubernetes avec Ingress NGINX et MetalLB

Ce projet est une **API Flask** dÃ©ployÃ©e sur un cluster **Kubernetes** avec support de **PostgreSQL**,. Il s'agit d'un TP Ã©ducatif pour apprendre Ã  conteneuriser et orchestrer des applications.

## ðŸ“ Structure du projet

```
api-flask/
-app.py                  # Application Flask principale
-requirements.txt        # DÃ©pendances Python
-Dockerfile              # Image Docker Flask
-flask-deployment.yaml   # DÃ©ploiement et service Flask
-postgres.yaml           # DÃ©ploiement et service PostgreSQL
-NetworkPolicy.yaml      # Politique rÃ©seau (optionnelle)
-tls/                    # Certificats TLS si besoin
```

##Prérequis

- Python 3.8+
- pip
- Docker
- Kubernetes (Minikube, MicroK8s, RKE, etc.)
- AccÃ¨s `kubectl` fonctionnel

## ðŸš€ Lancement local (dÃ©veloppement)

1. **Cloner le projet**

```bash
git clone https://github.com/saadiste/api-flask.git
cd api-flask
```

2. **CrÃ©er et activer lâ€™environnement virtuel**

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

## ðŸ³ Construction et exÃ©cution Docker

1. **Construire lâ€™image Docker**

```bash
docker build -t flask-api:2.0 .
```

2. **Lancer lâ€™image localement**

```bash
docker run -d -p 5000:5000 flask-api:latest
```

## â˜¸ï¸ DÃ©ploiement Kubernetes

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

1. GÃ©nÃ¨re un token ici : [https://github.com/settings/tokens](https://github.com/settings/tokens)
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

## ðŸ“ž Endpoints de lâ€™API (exemples)

- `GET /` â†’ Message de bienvenue
- `GET /api/data` â†’ Retourne des donnÃ©es statiques
- `POST /api/data` â†’ Ajoute des donnÃ©es

## ðŸ™‹â€â™‚ï¸ Auteurs

**Nizar Saadi**

## ðŸ“„ Licence

Ce projet est sous licence MIT.
