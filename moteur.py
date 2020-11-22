
#-*- coding:Latin-1 -*
####################################################
#Bibliothèque: PyGame 
#Auteur: Tojoniaina Patrick 
#Déscription: Jeu de Puissance 4
####################################################

# -*-coding:Latin-1 -*
import Tkinter as tk
from const import*
from objet import*
from plateau import*
from ia import*
import os

def clicked(col, x):
    """Retourne le numero de la colonne cliquée
        clicked(list, int) -> -1 si aucune n'a été cliquée"""
    i=0
    while i<7:
        if col[i].clic(x):
            return i
        i+=1
    return -1

class Moteur:
    """Moteur de jeu"""
    def __init__(self):
        self.j1=HUMAIN
        self.j2=HUMAIN
        self.plateau=Plateau()
        self.tour=BLUE
        self.gagnant=VIDE
    def isHuman(self):
        """Retourne le type du joueur en fonction de ces pions"""
        if self.tour==BLUE:
            return self.j1==HUMAIN
        else:
            return self.j2==HUMAIN
    def aff(self , j,screen):
        """Methode utile uniquement à la méthode menu
        aff(int, int, Surface) -> None
        """
        if j==1:
            Type=self.j1
            if Type==HUMAIN:
                screen.blit(humain, POSJ1)
            if Type==ORDINATEUR:
                screen.blit(ordinateur, POSJ1)
        if j==2:
            Type=self.j2
            if Type==HUMAIN:
                screen.blit(humain, POSJ2)
            if Type==ORDINATEUR:
                screen.blit(ordinateur, POSJ2)
    def menu(self, screen):
        """Methode qui gère le menu du jeu
          menu(Surface) -> int
          """
        global event
        j1=HUMAIN
        j2=j1
        screen.blit(img_menu, (0,0))
        screen.blit(humain, POSJ1)
        screen.blit(humain, POSJ2)
        while True:
            pygame.display.flip()
            event=pygame.event.wait()
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                return QUITTER
            if event.type==MOUSEBUTTONUP:
                x=event.pos[0]
                y=event.pos[1]
                if (POSJ1[0]< x<POSJ1[0]+humain.get_width())and(POSJ1[1]<y<POSJ1[1]+humain.get_height()):
                    j1+=1
                    j1%=2
                    self.j1=j1
                    screen.blit(img_menu, (0,0))
                    self.aff(2, screen)
                    self.aff(1,screen)
                if (POSJ2[0]<x<POSJ2[0]+humain.get_width())and(POSJ2[1]<y<POSJ2[1]+humain.get_height()):
                    j2+=1
                    j2%=2
                    self.j2=j2
                    screen.blit(img_menu, (0,0))
                    self.aff(1,screen)
                    self.aff(2, screen)
                if (MIN_QUITTER[0]<x<MAX_QUITTER[0])and(MIN_QUITTER[1]<y<MAX_QUITTER[1]):
                    f=tk.Tk()
                    label=tk.Label(f, text="action")
                    label.pack()
                    if askyesno('-*- Hiala', "Hiala?"):
                        f.destroy()
                        return QUITTER
                    else:
                        f.destroy()
                        return MENU
                if (MIN_NOUVEAU[0]<x<MAX_NOUVEAU[0])and(MIN_NOUVEAU[1]<y<MAX_NOUVEAU[1]):
                    return JEU
                if 14<x<153 and 335<y<379:
                    f=tk.Tk()
                    text=tk.Label(f, text="Regle: Chaque joueur joue à tour de rôle en remplissant\n les 7 colonnes.\n\tLes pions tombent au fond; ainsi, une colonne se remplie toujours\n depuis la base.\nBut du jeu: Aligner 4 pions dans les 4 directions")
                    text.pack()
                    f.mainloop()
    def jeu(self, screen):
        """Le Jeu ...jeu(Surface )-> int"""
        prec=0
        tab1=[]
        tab2=[]
        screen.blit(plateau, (0,0))
        self.plateau=Plateau()
        col=self.plateau.col
        self.tour=BLUE #Les BLEU commencent
        j1=self.j1
        j2=self.j2
        if j1 is not HUMAIN:
            ia=IA(BLUE)
        if j2 is not HUMAIN:
            ia1=IA(RED)
        while self.gagnant==VIDE and not self.plateau.remplie():
            pygame.time.Clock().tick(30)
            i=0
            j=0
            pygame.display.flip()
            if not self.isHuman():#Si ce n'est pas à un humain de jouer
                if j1 is not HUMAIN:#Savoir lequel n'est pas un humain
                    if ia.type is self.tour and self.gagnant==VIDE:#Savoir si c'est vraiment son tour
                        cur=pygame.time.get_ticks()
                        self.plateau.last=ia.joue(self.plateau)
                        prec=cur
                        cur=pygame.time.get_ticks()
                        tab1.append((cur-prec)/1000)
                        self.check()
                        self.tour=opp(self.tour)
                if j2 is not HUMAIN:
                    if ia1.type is self.tour and self.gagnant==VIDE:
                        cur=pygame.time.get_ticks()
                        self.plateau.last=ia1.joue(self.plateau)
                        prec=cur
                        cur=pygame.time.get_ticks()
                        tab2.append((cur-prec)/1000)
                        self.check()
                        self.tour=opp(self.tour)
            
            event=pygame.event.poll()
            pygame.time.Clock().tick(30)
            if event.type==QUIT:
                return QUITTER
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    return QUITTER
                if event.key==K_SPACE:
                    return MENU
            if event.type==MOUSEBUTTONUP:
                if event.button==1:
                    x=event.pos[0]
                    if self.isHuman():
                        n=clicked(col, x)
                        if n!=-1:
                            i=self.plateau.jouable(n)
                            if i!=-1:
                                self.plateau.tab[i][n].setType(self.tour)
                                self.plateau.last=(i, n)
                                self.check()
                                self.tour=opp(self.tour)
            self.plateau.aff(screen)
        """if j1!=HUMAIN:
            print("Evaluation effectuée: ", ia.evaluation,"\nIA bleu: ", array(tab1).mean(),"s/coup")
        if j2!=HUMAIN:
            print("Evaluation effectuée: ", ia1.evaluation,"\nIA rouge: ", array(tab2).mean(),"s/coup")"""
        return APRES_JEU
    def apres_jeu(self, screen):
        """Methode qui affiche qui a gagné et demande si l'on veut rejouer ou non
           apres_jeu(Surface ) -> int"""
        #la variable temporaire 'tmp' servira pour rendre le fond un peu sombre
        tmp=pygame.Surface((WIDTH, HEIGHT))
        tmp.fill((0,0,0))
        tmp.set_alpha(120)
        screen.blit(tmp, (0,0))
        police=pygame.font.Font("data/pol.ttf", 50)
        if self.gagnant is not VIDE:
            if self.gagnant is BLUE:
                texte=police.render("Nandresy ny Manga!", True, (255,255,255))
            else:
                texte=police.render("Nandresy ny Mena!", True, (255,255,255))
        elif self.gagnant is VIDE:
            texte=police.render("Sahala!", True, (100,255,100))
        screen.blit(texte, (20,20))
        pygame.display.flip()
        self.plateau.clean()
        self.tour=BLUE
        self.gagnant=VIDE
        f=tk.Tk()
        label=tk.Label(f, text="action")
        label.pack()
        if askyesno('-*- Mifarana ny lalao', "Hiverina hilalao?"):
            os.system("cls")
            f.destroy()
            return JEU
        else:
            os.system("cls")
            f.destroy()
            self.j1=HUMAIN
            self.j2=HUMAIN
            return MENU
        
    def check(self):
        if self.plateau.gagnant()!=VIDE:
            for coord in self.plateau.gagne:
                if self.tour==BLUE:
                    self.plateau.get(coord[0], coord[1]).setType(BGAGNANT)
                else:
                    self.plateau.get(coord[0], coord[1]).setType(RGAGNANT)
            self.gagnant=self.tour
            return APRES_JEU
