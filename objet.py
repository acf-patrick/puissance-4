
#-*- coding:Latin-1 -*
####################################################
#Bibliothèque: PyGame 
#Auteur: Tojoniaina Patrick 
#Déscription: Jeu de Puissance 4
####################################################
from const import*

# -*-coding:Latin-1 -*

class Objet:
    def __init__(self, x=0, y=0, t=VIDE):
        """Objet(tuple, int) -> Objet"""
        self.image=pygame.Surface((56, 56))
        self.type=t
        self.vide=True#un booleen ,simple quéstion de lisibilité
        self.x=case[x][y][0]#coordonnées en pixel..Rappelons que 'case' est une liste bidimensionnelle de tuple
        self.y=case[x][y][1]
    def __eq__(self, objet):#Surcharge de l'operateur égalité
        return objet.type==self.type
    def __str__(self):
        return str(self.type)
    def aff(self, screen):
        """affiche l'objet en quéstion
          aff(Surface ) -> None"""
        if self.type is not VIDE:
            screen.blit(self.image ,(self.x, self.y))   
    def setType(self, t):
        """Met à jour le type de l'objet
           setType(int ) -> None""" 
        self.type=t
        self.vide=(t is VIDE)
        if t is BLUE:
            self.image=pygame.image.load("data/blue.jpg")
        elif t is RED:
            self.image=pygame.image.load("data/red.jpg")
        elif t is BGAGNANT:
            self.image=pygame.image.load("data/winner blue.jpg")
        elif t is RGAGNANT:
            self.image=pygame.image.load("data/winner red.jpg")
        else:
            self.image=pygame.Surface((56,56))
            
#Vide object
vide=Objet()

class Col:
    def __init__(self, n):
        self.num=n
        self.x=case[0][n][0]
    def clic(self, x):
        """Gestion du clic
           clic(int, int) -> bool"""
        return (self.x<x and x<self.x+60)
