# Mario-kart-project

Jeu de course de voitures 2D pour deux joueurs sur un même clavier, inspiré de Mario Kart et de Trackmania.
Projet réalisé dans le cadre du cours de Python du M1 Robotique de Sorbonne Université.

## Prérequis

- **Python 3.10 à 3.13** (pygame ne supporte pas encore officiellement Python 3.14)
- **Git**

## Installation

git clone https://github.com/yeatss1/Mario-kart-project.git
cd Mario-kart-project
python -m pip install pygame


Optionnel: utiliser un environnement virtuel avant l'installation des dépendances.

python -m venv .venv
#### Windows
.venv\Scripts\activate
#### macOS / Linux
source .venv/bin/activate


## Lancement

Depuis la racine du projet (le dossier qui contient `main.py`):

python main.py


## Commandes

| Action | Touches |
|---|---|
| Lancer une course (menu) | Entrée |
| Quitter (menu) | Échap |
| Accélérer | Z ou ↑ |
| Freiner / reculer | S ou ↓ |
| Tourner à gauche | Q ou ← |
| Tourner à droite | D ou → |

## Structure du projet

Le code suit l'architecture MVC (Modèle / Vue / Contrôleur).

```
main.py                     Point d'entrée: initialise pygame et lance le contrôleur
constants.py                Constantes globales (fenêtre, grille, voiture, couleurs, états du jeu)
model/
    game_model.py           État global du jeu (menu, course), circuit et voiture
    car.py                  Voiture: position, vitesse, angle, sprite
    circuit.py              Circuit: grille de cases et accès par case ou par pixel
    road_tile.py            Case de route
view/
    game_view.py            Affichage du menu et de la course avec pygame
controller/
    game_controller.py      Boucle de jeu, gestion des événements et des états
    input_handler.py        Correspondance entre touches du clavier et actions
```

## Répartition du travail et planning

*À compléter*


## Utilisation des outils d'IA

*à compléter*