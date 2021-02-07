#########################################################

# Exercice 4 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
#Afficher un carré rempli de rouge de côté 50 au milieu du canevas.
#Si l’utilisateur clique à l’intérieur du carré et que le côté du carré est au moins égale à 20, alors le côté du carré diminue de 10 (effacer et réafficher).
#Si l’utilisateur clique à l’extérieur du carré et que le côté du carré est au plus égal à 100, alors le côté du carré augmente de 10 (effacer et réafficher).
#Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie plus le carré) et le nom du bouton devient “Restart”.
#Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”.

#########################################################

import tkinter as tk

coord1 = 225
coord2 = 275
cote = coord2 - coord1

def clic(event):
    global coord1, coord2, cote
    if event.x > coord1 and event.x < coord2 and event.y > coord1 and event.y < coord2 and cote >= 20:
        coord1 += 5
        coord2 -= 5
        canvas.delete("all")
        canvas.create_rectangle((coord1, coord1), (coord2, coord2), fill="red")
    elif (event.x < coord1 or event.x > coord2 or event.y < coord1 or event.y > coord2) and cote <= 100:
        coord1 -= 5
        coord2 += 5
        canvas.delete("all")
        canvas.create_rectangle((coord1, coord1), (coord2, coord2), fill="red")

def pause():
    bouton.configure(text="Restart")

racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="white")
bouton = tk.Button(racine, text="Pause", command=pause)

canvas.grid(column=0, row=0)
bouton.grid(column=0, row=1)

carre = canvas.create_rectangle((coord1, coord1), (coord2, coord2), fill="red")

racine.bind("<Button-1>", clic)

racine.mainloop()