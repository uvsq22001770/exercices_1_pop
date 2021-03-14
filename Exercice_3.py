#########################################################

# Exercice 3 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Redémarrer” placé en dessous du canevas.
#Diviser la fenêtre en 3 en affichant deux traits verticaux blancs.
#Tant qu’il y a strictement moins de 2 croix, un clic dans la partie gauche affiche une croix bleue inscrite dans un carré de côté 50 centré sur le clic, et sinon ça ne fait rien.
#Tant qu’il y a strictement moins de 3 carrés, un clic dans la partie du milieu affiche un carré vert de côté 50 centré sur le clic, et sinon ça ne fait rien.
#Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
#A tout moment, si l’utilisateur clique sur le bouton “Redémarrer”, alors tous les cercles, les carrés et les croix s’effacent.

#########################################################

import tkinter as tk

nb_croix = 0
nb_carre = 0
nb_cercle = 0

def clic(event):
    global nb_croix, nb_carre, nb_cercle
    if event.x < 167 and nb_croix < 2:
        canvas.create_rectangle((event.x - 25, event.y - 5), (event.x + 25, event.y + 5), fill="blue")
        canvas.create_rectangle((event.x - 5, event.y - 25), (event.x + 5, event.y +  25), fill="blue")
        nb_croix += 1
    elif event.x > 167 and event.x < 334 and nb_carre < 3:
        canvas.create_rectangle((event.x - 25, event.y - 25), (event.x + 25, event.y + 25), fill="green")
        nb_carre += 1
    elif event.x > 334 and nb_cercle < 3:
        canvas.create_oval((event.x - 25, event.y - 25), (event.x + 25, event.y + 25), fill="red")
        nb_cercle += 1

def effacer():
    if nb_croix>0 or nb_cercle>0 or nb_carre>0:
        canvas.delete("all")
        canvas.create_line((167, 0), (167, 500), fill="white")
        canvas.create_line((334, 0), (334, 500), fill="white")
    else:
        pass

racine = tk.Tk()

canvas = tk.Canvas(racine, width=500, height=500, bg="black")
bouton = tk.Button(racine, text="Redémarrer", command=effacer)

canvas.create_line((167, 0), (167, 500), fill="white")
canvas.create_line((334, 0), (334, 500), fill="white")

canvas.grid(column=0, row=0)
bouton.grid(column=0, row=1)
racine.bind("<Button-1>", clic)

racine.mainloop()



### code Gab ###

"""import tkinter as tk

root = tk.Tk()
root.title("exercice n°3")


### Constantes: ###
HEIGHT = 500
WIDTH = 500
nb_croix = 0
nb_carrés = 0
nb_cercles = 0
### Fonctions: ###

def clic(event):
    global nb_croix, nb_carrés, nb_cercles
    if event.x < WIDTH//3 and nb_croix < 2:
        canevas.create_rectangle((event.x - 25, event.y - 5),(event.x + 25, event.y + 5),fill="blue")
        canevas.create_rectangle((event.x - 5, event.y - 25),(event.x + 5, event.y + 25),fill="blue")
        nb_croix += 1
    elif event.x > WIDTH//3 and event.x < WIDTH//3 * 2 and nb_carrés < 3:
        canevas.create_rectangle((event.x - 25, event.y - 25),(event.x + 25, event.y + 25),fill="green")
        nb_carrés += 1        
    elif event.x > WIDTH//3 * 2 and nb_cercles < 3:
        canevas.create_oval((event.x - 25, event.y - 25),(event.x + 25, event.y + 25),fill="red")
        nb_cercles += 1   


def effacer():
    global nb_croix, nb_carrés, nb_cercles
    canevas.delete("all")
    for i in range(0,2):
        canevas.create_line((WIDTH//3)*(1+i), 0, (WIDTH//3)*(1+i), HEIGHT, fill="white", dash=(10,))
    nb_croix = 0
    nb_carrés = 0
    nb_cercles = 0



### Création des widgets: ###
canevas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
bouton = tk.Button(root, text="Redémarrer", command=effacer)

###########################
for i in range(0,2):
    canevas.create_line((WIDTH//3)*(1+i), 0, (WIDTH//3)*(1+i), HEIGHT, fill="white", dash=(10,))

canevas.bind("<Button-1>", clic)

### Placement des widgets: ###
canevas.grid(column=0, row=0)
bouton.grid(column=0, row=1)

root.mainloop()"""
