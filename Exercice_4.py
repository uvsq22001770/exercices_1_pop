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

cote = 50
pause = False

def bouton_pause():
    global pause
    if not pause:
        bouton.config(text="Restart")
        pause = True
    else:
        bouton.config(text="Pause")
        pause = False

def est_dans_carre(x, y):
    """La fonction retourne True si le point de coordonnées (x,y) est dans le carré et False sinon"""
    inf = 250-cote//2
    sup = 250+cote//2
    return inf <= x <= sup and inf <= y <= sup

def change_taille(event):
    global cote
    if not pause:
        if est_dans_carre(event.x, event.y) and cote >= 20:
            cote -= 10
            canvas.coords(carre, 250-cote//2, 250-cote//2,250+cote//2, 250+cote//2)
        elif not est_dans_carre(event.x, event.y) and cote <= 100:
            cote += 10
            canvas.coords(carre, 250-cote//2, 250-cote//2,250+cote//2, 250+cote//2)


racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", width=500, height=500)
canvas.grid(row=0, column=0)

bouton = tk.Button(racine, text="Pause", command=bouton_pause)
bouton.grid(row=1)

carre = canvas.create_rectangle((250-cote//2, 250-cote//2),(250+cote//2, 250+cote//2), fill="red", outline="red")
canvas.bind("<Button-1>", change_taille)

racine.mainloop()