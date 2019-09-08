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
    
    
class BlocReponse():
    reponses = ""
    
    def __init__(self):
        reponses = list()
    
    
class Question():
    titre = ""
    question = ""
    blocs_reponses = None       # blocs reponses
    retour_general = ""

    fichier = None
    

    def __init__(self, nom):
        self.fichier = io.open(nom, mode="r", encoding="utf-8")     # Ouverture mode UTF-8
        self.blocs_reponses = list()
        
        
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
        
        
    def ReadTitle(self):
        c = self.Read()
        if (c==":"):
            self.titre = ""
            while True:
               c1 = self.Read()
               if (len(c1)==0): break
               if (c1==":"): 
                   c2 = self.Read()
                   if (c2 == ":"): 
                       break
                   else:
                       return c2
               self.titre += c1
               #print(c1)
        return None
    
    
    def ReadBlocReponse(self):
        while True:
            c = self.Read()
            if (len(c)==0): break
            if (c == "}"): break
    
    
    def ReadGIFT(self):
        self.question = ""
        while True:
            c = self.Read()
            if (len(c)==0): break;
            if (c == "{"):
                self.ReadBlocReponse()
                self.question += "%1"
                continue
            if (c == ":"):
                c1 = self.ReadTitle()
                if (c1 != None): pass
                continue
            self.question += c


q = Question("C:/Travail/UPF/Formation DIU EIL/Bloc_1/Projet/Fichiers_tests/Grant's tomb.txt")

q.ReadGIFT()
print("\""+q.titre+"\"")
print("\""+q.question+"\"")
