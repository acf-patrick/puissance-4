
#-*- coding:Latin-1 -*
####################################################
#Biblioth�que: PyGame
#Auteur: Tojoniaina Patrick
#Déscription: Jeu de Puissance 4
####################################################
import pygame
from pygame.locals import*
from const import*
from objet import*
from random import randrange
#-*- coding:Latin-1 -*

heuristique=[[3,4,5,7,5,4,3],
             [4,6,8,10,8,6,4],
             [5,8,11,13,11,8,5],
             [5,8,11,13,11,8,5],
             [4,6,8,10,8,6,4],
             [3,4,5,7,5,4,3]]
def estime(t):
    if t[0]>=3:
        return 3*t[1]
    if t[0]==2:
        return 2*t[1]
    if t[0]==1:
        return t[1]
    else:
        return 0
class IA:
    def __init__(self, t):
        self.type=t
        if t is BLUE:
            self.first=True
            self.second=False
            self._first=False
        else:
            self.first=False
            self._first=True
        self.evaluation=0
    def evalue(self, plateau):
        pionIA=0
        score=0
        self.evaluation+=1
        if plateau.gagnant()==self.type:
            return 1000-plateau.coup()
        elif plateau.gagnant()==VIDE:
            return 0
        elif plateau.gagnant()==opp(self.type):
            return -1000+plateau.coup()
        for i, ligne in enumerate(plateau.tab):
            for j, elt in enumerate(ligne):
                if elt.type==self.type:
                    score+=heuristique[i][j]
                elif elt.type==opp(self.type):
                    score-=heuristique[i][j]
        ##Parcour des lignes
        for igne in plateau.tab:
            pion=0
            pionIA=0
            for elt in ligne:
                if elt.type!=VIDE:
                    pion+=1
                    if elt.type==self.type:
                        pionIA+=1
                    else:
                        pionIA-=1
            score+=estime((pion, pionIA))
        ##Parcour des colonnes
        i=0
        j=0
        while j<7:
            pion=0
            pionIA=0
            while i<6:
                if plateau.get(i, j).type!=VIDE:
                    pion+=1
                    if plateau.get(i, j).type==self.type:
                        pionIA+=1
                    else:
                        pionIA-=1
                i+=1
            score+=estime((pion, pionIA))
            i=0
            j+=1
        ##Parcour des diagonales
        #Parcour déscendant
        k=0
        while k<6:
            i=minD[k][0]
            pion=0
            pionIA=0
            while i<=maxD[k][0]:
                a=(minD[k][1]-maxD[k][1])//(minD[k][0]-maxD[k][0])
                b=minD[k][1]-a*minD[k][0]
                j=a*i+b
                if plateau.get(i, j).type!=VIDE:
                    pion+=1
                    if plateau.get(i, j).type==self.type:
                        pionIA+=1
                    else:
                        pionIA-=1
                i+=1
            score+=estime((pion, pionIA))
            k+=1
        #Parcour ascendant
        k=0
        while k<6:
            i=minA[k][0]
            pion=0
            pionIA=0
            while i<=maxA[k][0]:
                a=(minA[k][1]-maxA[k][1])//(minA[k][0]-maxA[k][0])
                b=minA[k][1]-a*minA[k][0]
                j=a*i+b
                if plateau.get(i, j).type!=VIDE:
                    pion+=1
                    if plateau.get(i, j).type==self.type:
                        pionIA+=1
                    else:
                        pionIA-=1
                i+=1
            score+=estime((pion, pionIA))
            k+=1
        
        return score

    def Max(self, plateau, depth, alpha, beta):
        if depth is 0 or plateau.remplie() or plateau.gagnant()!=VIDE:
            return self.evalue(plateau)
        i=0
        j=i
        tmp=j
        while j<7:
            i=plateau.jouable(j)
            if i!=-1:
                plateau.tab[i][j].setType(self.type)
                plateau.last=(i, j)
                tmp=self.Min(plateau, depth-1, alpha, beta)
                plateau.tab[i][j].setType(VIDE)
                alpha=max(tmp, alpha)
                if beta<=alpha:
                    return alpha
            j+=1
        return alpha
    
    def Min(self, plateau, depth, alpha, beta):
        if depth is 0 or plateau.remplie() or plateau.gagnant()!=VIDE:
            return self.evalue(plateau)
        i=0
        j=i
        tmp=j
        while j<7:
            i=plateau.jouable(j)
            if i!=-1:
                plateau.tab[i][j].setType(self.type)
                plateau.last=(i, j)
                tmp=self.Max(plateau, depth-1, alpha, beta)
                plateau.tab[i][j].setType(VIDE)
                beta=min(tmp, beta)
                if beta<=alpha:
                    return beta
            j+=1
        return beta
    
    def joue(self, plateau):
        i=0
        j=i
        tmp=0
        maxI=-INFINI
        maxJ=-INFINI
        alpha=-INFINI
        beta=INFINI
        #'first , _first et seconde servent à eviter de parcourir l'arbre inutilement et gagner ainsi du temps
        while j<7 and not self.first and not self._first and not self.second:
            ##Si ce n'est pas le premier coup pour chaque type choisi
            ##On parcour l'arbre
            i=plateau.jouable(j)
            if i!=-1:##Si cette colonne est jouable
                plateau.tab[i][j].setType(self.type)
                tmp=self.Min(plateau, 4, alpha, beta)
                if alpha<tmp:
                    alpha=tmp
                    maxI=i
                    maxJ=j
                print(tmp)
                plateau.tab[i][j].setType(VIDE)
            j+=1
        print('choisie: ', alpha)
        if self._first or (self.second and not self.first):
            ##Autrement, si c'est l'IA qui suit, joue l'une des colonnes libres du milieu pour bloquer
            #ou si c'est le second coup d'un IA BLUE
            self._first=False
            self.second=False
            #De préference le centre
            if plateau.get(5,3).type==VIDE:
                 maxI, maxJ=5, 3
            elif plateau.get(5,2).type==VIDE:
                maxI, maxJ=5, 2
            elif plateau.get(5,4).type==VIDE:
                maxI, maxJ=5, 4
            
        if self.first:
            ##Si c'est l'IA qui ouvre la partie ,choisir une colonne aléatoirement
            j=randrange(7)
            maxI, maxJ= plateau.jouable(j), j
            self.first=False
            self.second=True
        print("evaluation :", self.evaluation)
        self.evaluation=0
        plateau.get(maxI, maxJ).setType(self.type)
        return (maxI, maxJ)
