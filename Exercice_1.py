#########################################################

# Exercice 1 :

#Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille 500x500 ainsi qu’un bouton avec le texte “Recommencer” placé en dessous du canevas.
#Dessiner un rectangle rempli de rouge sur le canvas (la taille et la position sont au choix).
#A chaque clic de l’utilisateur dans le rectangle, le rectangle devient bleu, puis rouge alternativement.
#Si l’utilisateur clique en dehors du rectangle alors le rectangle est figé: c’est-à-dire que si on reclique à l’intérieur de celui-ci, rien ne se passe.
#A tout moment, si l’utilisateur clique sur le bouton “recommencer”, alors on recommence du début avec le rectangle rempli de rouge dessiné.

#########################################################

import tkinter as tk 

def restart():
    global couleur
    couleur = 'red'

def changecouleur(event) :
    global couleur
    x = event.x 
    y = event.y
    if x < 149 or y <= 200 or y >= 300 or  x > 401:
        couleur = 'bloqué'
    else : 
        if couleur == 'red' :
            couleur = 'blue'
            rectangle = canvas.create_rectangle ( (150,200) , (400 , 300) , fill = couleur )
        elif couleur == 'blue' :
            couleur = 'red'
            rectangle = canvas.create_rectangle ( (150,200) , (400 , 300) , fill = couleur )

couleur = "red"


racine = tk.Tk() 


canvas = tk.Canvas(racine, bg = "black", width = 500 , height = 500 )
canvas.grid(column=0, row=0)

rectangle = canvas.create_rectangle ( (150,200) , (400 , 300) , fill = couleur )

button = tk.Button(racine, text="recommencer", command = restart)
button.grid(column=0, row=1)

canvas.bind("<Button-1>" , changecouleur)

racine.mainloop()