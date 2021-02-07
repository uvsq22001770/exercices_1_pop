#########################################################

# Exercice 1 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
#Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
#A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
#Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
#A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné.

#########################################################

import tkinter as tk

nombre = 0


def color():
    global nombre
    if nombre % 2 == 0:
        return("red")
    elif nombre % 2 == 1:
        return("blue")


def clic(event):
    global nombre
    nombre += 1
    if event.x > 50 and event.x < 450 and event.y > 150 and event.y < 350:
        canvas.itemconfigure(rectangle, fill=color())
    else:
        racine.destroy()   

def recommencer():
    canvas.itemconfigure(rectangle, fill="red")


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", width=500, height=500)
bouton = tk.Button(racine, text="Recommencer", command=recommencer)

rectangle = canvas.create_rectangle((50, 150), (450, 350), fill="red")

canvas.grid(column=0, row=0)
bouton.grid(column=0, row=1)

racine.bind("<Button-1>", clic)

racine.mainloop()