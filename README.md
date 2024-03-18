# Rock Paper Scissor using Computer Vision

## Introduction
Le projet "Rock Paper Scissor using Computer Vision" est une implémentation interactive du jeu classique en utilisant la vision par ordinateur. Le code utilise OpenCV pour la capture vidéo et la détection des mains, ainsi que la bibliothèque cvzone pour faciliter le suivi des mains. L'objectif est de permettre aux utilisateurs de jouer contre une IA qui génère des mouvements aléatoires.

## Fonctionnalités du Projet

### 1. Détection des Mains :
Nous avons intégré le module de détection des mains de la bibliothèque cvzone pour localiser les mains dans le flux vidéo de la webcam. Cela permet aux utilisateurs de faire des mouvements spécifiques pour jouer au jeu.

### 2. Interface Utilisateur :
L'interface utilisateur est créée en superposant le flux vidéo de la webcam sur une image d'arrière-plan. Les scores, le minuteur et les messages sont affichés à des emplacements spécifiques pour une expérience utilisateur claire.

### 3. Logique de Jeu :
Le jeu commence lorsque l'utilisateur appuie sur la touche 'S'. Un minuteur est activé pour limiter le temps de prise de décision. Ensuite, l'IA génère un mouvement aléatoire, et les résultats du jeu sont déterminés en fonction des règles classiques de Pierre-Papier-Ciseaux. Le jeu se termine si l'un des joueurs atteint trois points et un message de victoire s'affiche. Les utilisateurs ont la possibilité de redémarrer le jeu en appuyant sur la touche 'R' ou de quitter en appuyant sur la touche 'Esc'.
