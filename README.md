# Projet 7 : Créez GrandPy Bot, le papy-robot

## Contexte

Il s’agit de créer une application web en utilisant le micro framework Flask avec les API Google maps et Wikipedia. 
Pour ce faire, un robot renvoie l’adresse, la carte google map et un récit sur un lieu demandé. 
Cela nécessite l’utilisation des fonctionnalités comme AJAX, 
les API de Google Maps et Mediawiki qui sont à respecter dans le cahier des charges
tout comme les tests Driven Development et Mock.

## Liens

* [Lien Trello](https://trello.com/b/uTDkN8Qm/projet-7-ocr-grandpy)
* [Lien Heroku](https://grandpy-project-7-sd.herokuapp.com/)

## Installation

Pour copier le projet en local, ouvrer un terminal et taper les commandes suivantes

```clone
$ git clone https://github.com/souleymanediallo/projet-7-GrandPy.git
```

Installer un environnement virtuel
```virtualenv
$ pip install virtualenv
```

Créer un environnement virtuel
```venv
$ virtualenv venv
```

Activer l'environnement virtuel
```activate
$ source venv/bin/activate
```

Intaller les dépendances du projet
```installer
$ pip install -r requirements.txt
```

## API 

Vous utiliserez l'API de Google Maps et celle de Media Wiki dans le fichier config.py

* [Google API](https://developers.google.com/)
* [wikimedia API](https://www.mediawiki.org/wiki/API:Main_page)

Demarrer l'application avec la commande suivante 

```run
$ python run.py
```

## Tests 

Faire les tests

```test
pytest tests.py
flake8 app/
```

## Crée avec

* Python 3.8
* Flask 
* HTML5 & CSS3
* Bootstrap 5
* Google API
* Wikipedia API

## Auteur

Souleymane Diallo 
Développeur Python, étudiant openclassrooms
