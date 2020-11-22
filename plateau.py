
#-*- coding:Latin-1 -*
####################################################
#Bibliothèque: PyGame 
#Auteur: Tojoniaina Patrick 
#Déscription: Jeu de Puissance 4
####################################################
from objet import*
from const import*

# -*-coding:Latin-1 -*
class Plateau:
    def __init__(self):
        self.tab=[]
        i=0
        j=0
        while i<6:
            self.tab.append([])
            while j<7:
                self.tab[i].append(Objet(i, j, VIDE))
                j+=1
            j=0
            i+=1
        self.nulle=True#la Partie est nulle
        self.gagne=[]
        self.col=[Col(0), Col(1), Col(2), Col(3), Col(4), Col(5), Col(6)]
        self.last=()
    def __str__(self):
        chaine=""
        for ligne in self.tab:
            for elt in ligne:
                chaine+=str(elt.type)+' '
            chaine+='\n'
        return chaine
    def getT(self, x, y):
        return self.get(x, y).type
    ############################################################################################
    def checkline(self, num):
        self.gagne=[]
        for k in range(4):
            if self.getT(num, k)==self.getT(num, k+1)==self.getT(num, k+2)==self.getT(num, k+3) and self.getT(num, k)!=VIDE:
                self.gagne+=[(num, k), (num, k+1), (num, k+2), (num, k+3)]
                return self.getT(num, k)
        return VIDE
    def checkcol(self, num):
        self.gagne=[]
        for k in range(3):
            if self.getT(k, num)==self.getT(k+1, num)==self.getT(k+2, num)==self.getT(k+3, num) and self.getT(k, num)!=VIDE:
                self.gagne+=[(k, num), (k+1,num), (k+2, num), (k+3, num)]
                return self.getT(k, num)
        return VIDE
    def checkdiagD(self, num):
        self.gagne=[]
        for k in range(3):
            if self.getT(k, num)==self.getT(k+1, num+1)==self.getT(k+2, num+2)==self.getT(k+3, num+3) and self.getT(k, num)!=VIDE:
                self.gagne+=[(k, num), (k+1, num+1), (k+2, num+2), (k+3, num+3)]
                return self.getT(k, num)
        return VIDE
    def checkdiagM(self, num):
        self.gagne=[]
        for k in range(3):
            if self.getT(5-k, num)==self.getT(4-k, num+1)==self.getT(3-k, num+2)==self.getT(2-k, num+3) and self.getT(5-k, num)!=VIDE:
                self.gagne+=[(5-k, num), (4-k, num+1), (3-k, num+2), (2-k, num+3)]
                return self.getT(5-k, num)
        return VIDE
    ##############################################################################################
    def get(self, x, y):
        try:
            return self.tab[x][y]
        except IndexError:
            print((x, y))
    def gagnant(self):
        for i in range(6):
            if self.checkline(i)!=VIDE:
                return self.checkline(i)
        for j in range(7):
            if self.checkcol(j)!=VIDE:
                return self.checkcol(j)
        for k in range(4):
            if self.checkdiagD(k)!=VIDE:
                return self.checkdiagD(k)
            if self.checkdiagM(k)!=VIDE:
                return self.checkdiagM(k)
        return VIDE
    def remplie(self):
        for ligne in self.tab:
            for elt in ligne:
                if elt.type==VIDE:
                    return False
        return True
    def fini(self):
        return (self.gagnant()!=VIDE  or self.remplie())
    def clean(self):
        for ligne in self.tab:
            for elt in ligne:
                elt.setType(VIDE)
        self.last=()
    
    def aff(self, screen):
        """Methode qui affiche le plateau de jeu"""
        for ligne in self.tab:
            for elt in ligne:
                elt.aff(screen)#Rien de spéciale, on affiche
                               #chaque case du plateau
    def coup(self):
        """Retourne le nombre coup jouer depuis le début
           coup(...) -> int"""
        cmp=0
        for ligne in self.tab:
            for elt in ligne:
                if elt.type is not VIDE:
                    cmp+=1
        return cmp

    def jouable(self, j):
        """Retourne l'index de la case jouable selon le numero de la colonne donnée en
           argument, jouable(int ) -> int...(-1) si aucune case jouable"""
        i=5
        while i>=0:
            if self.get(i, j).type==VIDE:
                return i
            i-=1
        return -1
    def get_num(self):
        tab=[]
        for i, ligne in enumerate(self.tab):
            tab.append([])
            for elt in ligne:
                tab[i].append(elt.type)
        return tab
    
