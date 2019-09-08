# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:25:46 2019

@author: LAU Wai Tong Christian
"""

# Test de lecture de fichier au format UTF-8

import io

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
    
Test_lecture_fichier("C:/Travail/UPF/Formation DIU EIL/Bloc_1/Projet/Fichiers_tests/Grant's tomb.txt")
