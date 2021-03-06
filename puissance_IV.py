# -*-coding:utf-8 -*

####################################################
#Bibliothèque: PyGame 
#Auteur: Tojoniaina Patrick 
#Déscription: Jeu de Puissance 4
####################################################

# -*-coding:Latin-1 -*
import pygame
from pygame.locals import*
from const import*
from moteur import*

moteur=Moteur()
pygame.init()
humain.set_colorkey((255,255,255))
ordinateur.set_colorkey((0,0,0))
pygame.display.set_icon(pygame.image.load("data/icone.ico"))
pygame.display.set_caption("Puissance 4")
screen=pygame.display.set_mode((WIDTH,HEIGHT))
done=False
choix=MENU
while not done:
    if choix==MENU:
        choix=moteur.menu(screen)
    if choix==JEU:
        choix=moteur.jeu(screen)
    if choix==APRES_JEU:
        choix=moteur.apres_jeu(screen)
    if choix==QUITTER:
        done=True
pygame.quit()
