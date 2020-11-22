
#-*- coding:Latin-1 -*
"""Module ou les constantes sont definies"""
####################################################
#Bibliotheque: PyGame
#Auteur: Tojoniaina Patrick
#Déscription: Jeu de Puissance 4
####################################################
import pygame
from pygame.locals import*

#-*- coding:Latin-1 -*
INFINI=10000

WIDTH=469
HEIGHT=391

humain=pygame.image.load("data/humain.jpg")
ordinateur=pygame.image.load("data/ordinateur.jpg")
img_menu=pygame.image.load("data/menu.jpg")
plateau=pygame.image.load("data/plateau.jpg")

VIDE=0
BLUE=1#les bleus commencent
RED=2
RGAGNANT=4
BGAGNANT=3

HUMAIN=0
ORDINATEUR=1

MENU=0
JEU=1
APRES_JEU=2
QUITTER=3

POSJ1=(20,196)
POSJ2=(288,205)

MIN_QUITTER=(183, 313)
MAX_QUITTER=(300,371)
MIN_NOUVEAU=(173, 259)
MAX_NOUVEAU=(313,319)

#Enregistrement des positions où coller les images
case=[]
i=0
j=0
while i<6:
    case.append([])
    while j<7:
        case[i].append((j*64+12, i*63+12))
        """Cette inversion est due au chagement de l'orientation des reperes respectifs
            Pour notre matrice 'case' l'axe des x se dirige vers le bas tandis que celui du
            du repère utilisé par pygame est orientée vers la droite c-à-d l'axe des y de
            notre matrice"""
        j+=1
    j=0
    i+=1
def opp(t):
    if t==BLUE:
        return RED
    elif t==RED:
        return BLUE
minD=[]
i=2
j=0
while j<4:
    minD.append((i, j))
    if i==0:
        j+=1
    else:
        i-=1
maxD=[]
i=5
j=3
while i>2:
    maxD.append((i, j))
    if j==6:
        i-=1
    else:
        j+=1
minA=[]
i=3
j=0
while j<4:
    minA.append((i, j))
    if i==5:
        j+=1
    else:
        i+=1
maxA=[]
i=0
j=3
while i<3:
    maxA.append((i, j))
    if j==6:
        i+=1
    else:
        j+=1
