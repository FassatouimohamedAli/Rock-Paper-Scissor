# Importer les bibliothèques nécessaires
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time

# Initialiser la webcam et définir ses propriétés
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Initialiser le détecteur de main à partir de la bibliothèque cvzone
detector = HandDetector(maxHands=1)

# Initialiser les variables pour la logique du jeu
timer = 0
stateResult = False
startGame = False
scores = [0, 0]  # [IA, Joueur]

while True:
    # Lire l'image d'arrière-plan
    imgBG = cv2.imread("Resources/BG.png")

    # Lire le cadre actuel de la webcam
    success, img = cap.read()

    # Redimensionner le cadre et le recadrer
    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Trouver les mains dans le cadre redimensionné et recadré
    hands, img = detector.findHands(imgScaled)  # avec dessin

    # Vérifier si le jeu a commencé
    if startGame:

        # Vérifier si l'état du résultat est False
        if stateResult is False:
            # Calculer la valeur du minuteur
            timer = time.time() - initialTime
            # Afficher le minuteur sur l'image d'arrière-plan
            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            # Vérifier si le minuteur a atteint 3 secondes
            if timer >= 3:
                stateResult = True
                timer = 0

                # Vérifier si des mains sont détectées
                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    # Déterminer le mouvement du joueur en fonction des positions des doigts
                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1
                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2
                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3

                    # Générer un mouvement aléatoire pour l'IA
                    randomNumber = random.randint(1, 3)
                    imgAI = cv2.imread(f'Resources/{randomNumber}.png', cv2.IMREAD_UNCHANGED)
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

                    # Mettre à jour les scores en fonction de la logique du jeu
                    if (playerMove == 1 and randomNumber == 3) or \
                            (playerMove == 2 and randomNumber == 1) or \
                            (playerMove == 3 and randomNumber == 2):
                        scores[1] += 1  # Le joueur gagne

                    if (playerMove == 3 and randomNumber == 1) or \
                            (playerMove == 1 and randomNumber == 2) or \
                            (playerMove == 2 and randomNumber == 3):
                        scores[0] += 1  # L'IA gagne

                    # Vérifier s'il y a un gagnant (le premier à atteindre 3 points)
                    if scores[0] == 3 or scores[1] == 3:
                        winner_message = "IA Gagne !" if scores[0] == 3 else "Joueur Gagne !"
                        text_size = cv2.getTextSize(winner_message, cv2.FONT_HERSHEY_PLAIN, 4, 6)[0]
                        text_x = (imgBG.shape[1] - text_size[0]) // 2
                        text_y = (imgBG.shape[0] + text_size[1]) // 2
                        cv2.putText(imgBG, winner_message, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, 4,
                                    (0, 255, 0) if scores[0] == 3 else (0, 0, 255), 6)
                        cv2.imshow("BG", imgBG)
                        cv2.waitKey(3000)  # Afficher le message final pendant 3 secondes

                        # Demander à l'utilisateur s'il veut recommencer
                        cv2.putText(imgBG, "Appuyez sur 'R' pour RECOMMENCER", (230, 350), cv2.FONT_HERSHEY_PLAIN, 2,
                                    (200, 200, 220), 3)
                        cv2.imshow("BG", imgBG)
                        key_restart = cv2.waitKey(0)

                        if key_restart == ord('r') or key_restart == ord('R'):
                            # Réinitialiser les variables du jeu
                            startGame = False
                            scores = [0, 0]
                            stateResult = False
                        else:
                            break

    # Superposer le cadre redimensionné et recadré sur l'image d'arrière-plan
    imgBG[234:654, 795:1195] = imgScaled

    # Superposer l'image de l'IA sur l'image d'arrière-plan
    if stateResult:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    # Afficher les scores sur l'image d'arrière-plan
    cv2.putText(imgBG, str(scores[0]), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)
    cv2.putText(imgBG, str(scores[1]), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)

    # Afficher l'image d'arrière-plan avec les superpositions
    cv2.imshow("BG", imgBG)

    # Vérifier les touches pressées
    key = cv2.waitKey(1)

    # Vérifier si la touche 's' est pressée pour démarrer le jeu
    if key == ord('s'):
        startGame = True
        initialTime = time.time()
        stateResult = False

    # Vérifier si la touche 'Esc' est pressée pour quitter le jeu
    if key == 27:
        break

# Libérer la webcam et fermer toutes les fenêtres lorsque le jeu est terminé
cap.release()
cv2.destroyAllWindows()
