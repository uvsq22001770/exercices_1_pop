#########################################################

# Exercice 6 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Annuler” placé à gauche du canevas.
#Afficher en haut à gauche du canevas 3 carrés juxtaposés de côté 50 et de couleur verte jaune et bleu.
#Afficher un cercle noir de rayon 50 au centre du canevas.
#Si l’utilisateur clique dans un des carrés du haut, le cercle prend la couleur du carré sur lequel l’utilisateur a cliqué.
#Si l’utilisateur clique en dehors des carrés alors le cercle devient noir.
#Si l’utilisateur clique sur le bouton “Annuler” alors le cercle reprend la couleur qu’il avait avant le dernier changement de couleur. Il doit être possible d’annuler tous les changements de couleur jusqu’au début.

#########################################################

"""import tkinter as tk

WIDTH = 500
HEIGHT = 500
COTE = 50
touche = 0

def clic(event):
    global touche
    touche += 1
    if event.x < COTE and event.y < COTE and touche == 1:
        canvas.delete((200,200), (300,300))
        canvas.delete(carre_bleu)
        canvas.create_oval((200,200), (300,300), fill="blue")
    elif event.x < COTE and event.y < COTE and touche == 2:
        canvas.delete((200,200), (300,300))
        canvas.delete(carre_jaune)
        canvas.create_oval((200,200), (300,300), fill="yellow")
    elif event.x < COTE and event.y < COTE and touche == 3:
        canvas.delete((200,200), (300,300))
        canvas.delete(carre_vert)
        canvas.create_oval((200,200), (300,300), fill="green")


racine = tk.Tk()

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
bouton = tk.Button(racine, text="Annuler")

canvas.grid(column=1, row=0)
bouton.grid(column=0, row=0)

carre_vert = canvas.create_rectangle((COTE, 0), (0,COTE), fill="green")
carre_jaune = canvas.create_rectangle((COTE, 0), (0,COTE), fill="yellow")
carre_bleu = canvas.create_rectangle((COTE, 0), (0,COTE), fill="blue")
cercle_noir = canvas.create_oval((200,200), (300,300), fill="black")

canvas.bind("<Button-1>", clic)


racine.mainloop()"""

import tkinter as tk

WIDTH = 500
HEIGHT = 500
COTE = 50
touche = 0


racine = tk.Tk()

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="white")
bouton = tk.Button(racine, text="Annuler")

canvas.grid(column=1, row=0)
bouton.grid(column=0, row=0)

carre_vert = canvas.create_rectangle((COTE, 0), (0,COTE), fill="green")
carre_jaune = canvas.create_rectangle((COTE, 0), (COTE*2,COTE), fill="yellow")
carre_bleu = canvas.create_rectangle((COTE, 0), (0,COTE), fill="blue")
cercle_noir = canvas.create_oval((200,200), (300,300), fill="black")

racine.mainloop()