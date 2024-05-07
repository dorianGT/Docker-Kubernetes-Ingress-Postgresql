# Docker Kubernetes Ingress PostgreSQL
Un projet simple utilisant plusieurs services avec Docker, Kubernetes, des routes via Ingress, et une base de données PostgreSQL.

# Introduction
Ce projet a été conçu pour démontrer comment créer et déployer une architecture de microservices en utilisant Docker et Kubernetes. L'objectif est de créer deux services différents et une base de données PostgreSQL, puis de les interconnecter via un Ingress Gateway. Cela permet de gérer le trafic externe et de simplifier la communication entre les services.

# Outils Utilisés
Docker : Permet de créer des conteneurs isolés pour chaque service. Chaque service est empaqueté avec ses dépendances, ce qui facilite le déploiement.
Kubernetes : Un orchestrateur de conteneurs qui gère le déploiement, le scaling et la gestion des services conteneurisés.
Minikube : Un environnement Kubernetes local pour le développement et les tests.
Ingress : Un composant Kubernetes qui gère les routes externes vers les services internes. C'est essentiel pour exposer vos services aux utilisateurs finaux.
PostgreSQL : Une base de données relationnelle open source pour stocker et gérer les données.

# Objectif
Le projet vise à mettre en place une architecture de microservices avec les éléments suivants :

Deux services distincts : Un service Flask (backend API) et un autre service secondaire.
Une base de données PostgreSQL : Pour stocker les données requises par les services.
Ingress Gateway : Pour exposer les services au monde extérieur et permettre aux clients de communiquer avec eux.

L'utilisation de Docker et Kubernetes permet de créer des services facilement redéployables et évolutifs. Minikube simplifie le processus de test en local, ce qui permet aux développeurs de valider rapidement les modifications apportées à l'application avant de déployer dans un environnement de production.


# Guide de déploiement avec Docker, Minikube, et Kubernetes
Ce guide décrit le processus de construction, de déploiement et de test d'une application utilisant Docker et Kubernetes, avec Minikube comme plateforme de déploiement local.

## Étape 1 : Activation de l'environnement virtuel

```bash
venv\Scripts\activate.bat
```

Cette commande active votre environnement virtuel Python. Cela vous permet de travailler avec des dépendances spécifiques sans interférer avec votre configuration Python globale.

## Étape 2 : Connexion à Docker

docker login

Ici, vous vous connectez à Docker Hub. Cela vous permet de pousser vos images Docker sur le cloud, ce qui est nécessaire pour le déploiement dans un environnement Kubernetes.

## Étape 3 : Démarrage de Minikube

minikube start

Cette commande démarre Minikube, qui est une solution permettant de faire tourner des clusters Kubernetes en local. C'est utile pour tester et développer des applications Kubernetes sans avoir besoin d'une infrastructure complète.

## Étape 4 : Construction des images Docker

docker build -t my_flask_app:latest -f Dockerfile_flask .
docker build -t my_second_service:latest -f Dockerfile_second_service .
docker build -t postgresql -f Dockerfile_postgresql .

Ces commandes créent des images Docker à partir de fichiers Dockerfile spécifiques. Chacune de ces images représente un service ou une partie de votre application.

my_flask_app: une application Flask.
my_second_service: un autre service.
postgresql: une base de données PostgreSQL.

## Étape 5 : Taguer les images Docker

docker tag my_flask_app doriang12/my_flask_app:latest
docker tag my_second_service doriang12/my_second_service:latest
docker tag postgresql doriang12/postgresql:latest

Le taggage permet de donner des noms significatifs à vos images Docker. Ici, vous ajoutez des tags avec votre nom d'utilisateur Docker Hub pour pouvoir les pousser vers votre compte.

## Étape 6 : Pousser les images sur Docker Hub

docker push doriang12/my_flask_app:latest
docker push doriang12/my_second_service:latest
docker push doriang12/postgresql:latest

Ces commandes envoient vos images Docker sur Docker Hub. Cela rend vos images disponibles pour un déploiement ultérieur sur Kubernetes.

## Étape 7 : Application des configurations Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f flask-ingress.yaml

Ces commandes utilisent kubectl pour appliquer les fichiers de configuration Kubernetes. Les fichiers deployment.yaml, service.yaml, et flask-ingress.yaml définissent respectivement le déploiement de vos applications, les services exposés par Kubernetes, et la configuration de l'ingress (qui gère le trafic externe vers vos services).

## Étape 8 : Vérification de l'état des déploiements

kubectl get deployments
kubectl get pods
kubectl get services
kubectl get ingress

Ces commandes permettent de vérifier l'état de votre cluster Kubernetes. Vous pouvez voir si les déploiements, les pods, les services, et l'ingress fonctionnent correctement.

## Étape 9 : Ouverture d'un tunnel Minikube

minikube tunnel

La commande minikube tunnel permet de créer un tunnel réseau qui connecte votre environnement local avec les services exécutés dans Minikube. Cela vous permet de tester votre application localement comme si elle était déployée sur un cluster Kubernetes externe.
