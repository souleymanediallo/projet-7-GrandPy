# Projet 7 : Créez GrandPy Bot, le papy-robot

## Parcours utilisateur

L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [En savoir plus sur Wikipedia]"

## Liens

* [Lien Trello](https://trello.com/b/uTDkN8Qm/projet-7-ocr-grandpy)
* [Lien Heroku](https://grandpy-project-7-sd.herokuapp.com/)

## Installation

```python
git clone https://github.com/souleymanediallo/projet-7-GrandPy.git
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

## API 

Vous utiliserez l'API de Google Maps et celle de Media Wiki dans le fichier config.py

* [Google API](https://developers.google.com/)
* [wikimedia API](https://www.mediawiki.org/wiki/API:Main_page)

## Tests 

Lancer la commande

```test
pytest tests.py
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
