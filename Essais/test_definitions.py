# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:25:46 2019

@author: LAU Wai Tong Christian
"""

# Test de lecture de fichier au format UTF-8

import io


class Reponse():
    type = 0
    exact=""
    text = ""
    valeur = 0
    pourcent = 100
    min = 0
    max = 0
    retroaction = ""
    
    
class Question():
    titre = ""
    question = ""
    reponses = list()
    retour_general = ""

    fichier = None

    def __init__(self, nom):
        self.fichier = io.open(nom, mode="r", encoding="utf-8")     # Ouverture mode UTF-8
        
    def Read(self):
        c = self.fichier.read(1)
        if (len(c)==0): return ""
        if (ord(c)==10): return self.Read()
        if (c=="/"):
            c1 = self.ReadComment()
            if (ord(c1)==10): return self.Read()
            if (c1=="/"):
                return "/"
            else:
                return c1
        return c
    
    def ReadComment(self):
        c = self.fichier.read(1)
        if (c=="/"):
            while True:
                c = self.fichier.read(1)
                if ((len(c)==0) or (ord(c)==10)): return chr(10)
        else:
            return c


def Test_lecture_fichier(nom):
    fichier = io.open(nom, mode="r", encoding="utf-8")     # Ouverture mode UTF-8
#    fichier = open(nom,"r")           # Ouverture standard, mode ASCII
    i = 0
    while True:
        c = fichier.read(1)
        if (len(c)==0): break          # Quitte la boucle si fin de fichier
        if (ord(c)==10): continue      # Si "retour à la ligne, ignorer
        print("%04X, %s %d" % (i,c,ord(c)))
        i += 1
    
#Test_lecture_fichier("C:/Travail/UPF/Formation DIU EIL/Bloc_1/Projet/Fichiers_tests/Grant's tomb.txt")

q = Question("C:/Travail/UPF/Formation DIU EIL/Bloc_1/Projet/Fichiers_tests/Grant's tomb.txt")

while True:
    c = q.Read()
    if (len(c)==0): break
    print("%s, %d" % (c,ord(c)))
