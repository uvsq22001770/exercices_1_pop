#########################################################

# Exercice 5 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond blanche et de taille 600x600 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
#Afficher deux lignes verticales séparant le canevas en trois parties égales. Celle de gauche est rouge, et celle de droite est bleu.
#A chaque fois que l’utilisateur clique sur le canevas, les lignes verticales se déplacent de 10 pixels vers l’endroit cliqué: par exemple si le clic est entre les deux lignes, celle de gauche se déplace vers la droite, et celle de droite se déplace vers la gauche. De plus, les couleurs des lignes sont échangées.
#Si l’utilisateur clique sur le bouton “Recommencer”, alors les 2 lignes verticales retournent à leur position initiale.

#########################################################

"""import tkinter as tk

COTE = 600
nombre = True
def clic(event):
    if nombre not False
        if event.x < COTE//3:
            canvas.move(ligne_gauche, -10, 0)
            canvas.move(ligne_droite, -10, 0)
        elif event.x > 2*COTE//3:
            canvas.move(ligne_gauche, +10, 0)
            canvas.move(ligne_droite, +10, 0)
        else:
            canvas.move(ligne_gauche, +10, 0)
            canvas.move(ligne_droite, -10, 0)


def recommencer():
    canvas.delete("all")
    ligne_gauche = canvas.create_line((COTE//3, 0), (COTE//3, COTE), fill="red", width=3)
    ligne_droite = canvas.create_line((2*COTE//3, 0), (2*COTE//3, COTE), fill="blue", width=3)
    nombre = 1

racine = tk.Tk()

canvas = tk.Canvas(racine, width= COTE, height= COTE, bg="black")
bouton = tk.Button(racine, text= "Recommencer", command= recommencer)

ligne_gauche = canvas.create_line((COTE//3, 0), (COTE//3, COTE), fill="red", width=3)
ligne_droite = canvas.create_line((2*COTE//3, 0), (2*COTE//3, COTE), fill="blue", width=3)
canvas.grid()
bouton.grid(row=1)

canvas.bind("<Button-1>", clic)


racine.mainloop()"""


import tkinter as tk


WIDTH = 600
HEIGHT = 600


def clic(event):
    if event.x < 200:
        canvas.move(ligne_gauche, -10, 0)
        canvas.move(ligne_droite, -10, 0)
    elif event.x > 400:
        canvas.move(ligne_gauche, 10, 0)
        canvas.move(ligne_droite, 10, 0)
    else:
        canvas.move(ligne_gauche, 10, 0)
        canvas.move(ligne_droite, -10, 0)
        

def recommencer():
    canvas.delete("all")
    canvas.create_line((WIDTH/3, 0), (WIDTH/3, HEIGHT), fill="red", width=5)
    canvas.create_line((2*WIDTH/3, 0), (2*WIDTH/3, HEIGHT), fill="yellow", width=5)
    #clic(event)


racine = tk.Tk()

canvas = tk.Canvas(racine, width=WIDTH, height=HEIGHT, bg="black")
bouton = tk.Button(racine, text="Recommencer", command=recommencer)

canvas.grid(column=1, row=0)
bouton.grid(column=0, row=0)

ligne_gauche = canvas.create_line((WIDTH/3, 0), (WIDTH/3, HEIGHT), fill="red", width=5)
ligne_droite = canvas.create_line((2*WIDTH/3, 0), (2*WIDTH/3, HEIGHT), fill="yellow", width=5)

canvas.bind("<Button-1>", clic)

racine.mainloop()