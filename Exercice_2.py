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

i = 1
x = 0
y = 0
c = 0
d = 0
u = 0
t = 0

def evenments(event):
   global i , x , y , c , d
   if i == 1 :
      x = event.x
      y = event.y
      i += 1

   elif i == 2 :
      a = event.x
      b = event.y

      canvas.create_line( (x,y) , (a,b) , fill = 'blue')
      i += 1

   elif i == 3 :

      c = event.x
      d = event.y 
      i +=1

   elif i == 4 :
      e = event.x
      f = event.y

      canvas.create_line( (c,d) , (e,f) , fill = 'red')
      i += 1

   elif i == 5 :
      canvas.delete('all')
      i = 1


def changement() :
   global u , i , t
   print(i)
   z = 0
   print(t)

   if u == 0 :
      t = i
      i = 100
      button = tk.Button(racine, text = 'Restart' , command = changement)
      button.grid(column=1, row=1)
      u = 1
      print('i',i,'t',t,'u',u)


   else :
      print(t)
      i = t
      print('i',i,'t',t)
      button = tk.Button(racine, text = ' Pause ' , command = changement)
      button.grid(column=1, row=1)
      u = 0




racine = tk.Tk()

canvas = tk.Canvas(racine, bg = "white", width = 500 , height = 500 )
canvas.grid(row = 0 , column = 1)

click = canvas.bind("<Button-1>" , evenments)

button = tk.Button(racine, text = 'pause' , command = changement)
button.grid(column=1, row=1)

racine.mainloop()