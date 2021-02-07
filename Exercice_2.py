#########################################################

# Exercice 2 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 500x500 ainsi qu’un bouton avec le texte “Pause” placé en dessous du canevas.
#Attendre deux clics de l’utilisateur.
#Afficher une ligne bleue entre les deux points cliqués.
#Attendre de nouveau deux clics.
#Afficher une ligne rouge entre les deux nouveaux points cliqués.
#Au clic suivant, les deux lignes sont effacées et on recommence (c’est-à-dire on attend de nouveau 2 clics comme au point 2.)
#Si l’utilisateur clique sur le bouton “Pause”, alors le programme est suspendu (c’est-à-dire que cliquer ne modifie pas la fenêtre graphique) et le nom du bouton devient “Restart”.
#Si l’utilisateur clique de nouveau sur le bouton “Restart” alors que le programme était suspendu, alors le programme reprend là où il en était, et le nom du bouton redevient “Pause”.

#########################################################

import tkinter as tk

nb_clic = 0
point1 = (0, 0)
point2 = (0, 0)
ligne1 = 0
ligne2 = 0


def clic(event):
    global nb_clic, point1, point2, ligne1, ligne2
    if nb_clic == 0:
        nb_clic = 1
        point1 = (event.x, event.y)
    elif nb_clic == 1:
        nb_clic = 2
        ligne1 = canvas.create_line(point1, (event.x, event.y), fill="blue")
    elif nb_clic == 2:
        nb_clic = 3
        point2 = (event.x, event.y)
    elif nb_clic == 3:
        nb_clic = 4
        ligne2 = canvas.create_line(point2, (event.x, event.y), fill="red")
    else:
        nb_clic = 0
        canvas.delete(ligne1)
        canvas.delete(ligne2)


def pause():
    bouton.configure(text="Restart")

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width=500, height=500)
bouton = tk.Button(racine, text="Pause", command=pause)

canvas.grid(column=0, row=0)
bouton.grid(column=0, row=1)

racine.bind("<Button-1>", clic)


racine.mainloop()