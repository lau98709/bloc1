# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:25:46 2019

@author: LAU Wai Tong Christian
"""

# Test de lecture de fichier au format UTF-8

import io

separators = {'=','~'}
separators2 = {'=','~','#'}


def Trim( s ):
    # Supprimer les espaces au début et à la fin d'une chaine
    i1 = 0
    while True:
        if (i1 >= len(s)): break
        if (s[i1]!=' '): break
        i1 += 1
    i2 = len(s)-1
    while True:
        if (i2 < 0): break
        if (s[i2]!=' '): break;
        i2 -= 1
    return s[i1:i2+1]


class Reponse():
    type = None
    exact = False
    text = None
    valeur = 0
    pourcent = 100
    min = 0
    max = 0
    retroaction = None

    def Parse(self, s):
        self.retroaction = ""
        ri = s.find('#')
        if (ri != -1):
           self.retroaction = s[(ri+1):]
           s = s[:ri]
        #print("\""+self.retroaction+"\"")

        if (s[0]=='='):
            self.exact = True
        elif (s[0]=='~'):
            self.exact = False

        if ((s[0]=='=') or (s[0]=='~')):
            s2 = s[1:]
            if (s2[0]=="%"):
                # Extraction du pourcentage
                for i in range(1,len(s2)):
                    if (s2[i]=='%'): break
                pourcent = int(s2[1:i])
                s2 = s2[i+1:]
                #print(pourcent, "\""+s2+"\"")
            self.text = s2

        #print(self.text,self.retroaction)


    def ParseNum(self):
        i = self.text.find("..")
        if (i != -1):
            self.min = int(self.text[0:i])
            self.max = int(self.text[i+2:])
            self.valeur = (self.min + self.max)/2
        elif (self.text.find(':') != -1):
            f = self.text.split(':')
            self.valeur = int(f[0])
            if (len(f) == 2):
                delta = int(f[1])
                self.min = self.valeur - delta
                self.max = self.valeur + delta
            elif (len(f) == 3):                
                self.min = self.valeur - int(f[1])
                self.max = self.valeur + int(f[2])
        else:
            self.valeur = self.min = self.max = int(self.text)
        #print(self.valeur, self.min, self.max)
    

class BlocReponse():
    reponses = None
    type = 0
    retroaction = ""

    def __init__(self):
        self.reponses = list()


    def Parse(self, s):

        # Extraction et retrait de la rétrocation globale
        gri = s.find("####")
        if (gri != -1):
            gri2 = gri+4
            while (gri2 < len(s)):
                if (s[gri2] in separators): break
                gri2 += 1
            self.retroaction = s[(gri+4):gri2]
            s = s[0:gri]+s[gri2:]
            #print(self.retroaction)

        sl = s.lower()
        if ((sl == "t") or (sl == "f") or (sl == "True") or (sl == "false")):
            self.type = 2    # TRUE or FALSE

        else:
            if (s[0]=='#'):
                self.type = 1    # Numérique
                s = Trim(s[1:])
            else:
                self.type = 0

            # Repérage des séparateurs
            sep = list()
            for i in range(len(s)):
                if (s[i] in separators):
                    sep.append(i)
            sep.append(len(s))      # rajouter la position de la fin de la chaine

            # Extraction des réponses
            for i in range(0,len(sep)-1):
                res = Reponse()
                res.Parse(s[sep[i]:sep[i+1]])
                if (self.type == 1): res.ParseNum()
                self.reponses.append(res)
                #print(res.text)


class Question():
    titre = ""
    question = ""
    blocs_reponses = None       # blocs reponses
    retour_general = ""

    fichier = None

    buffer = ""
    bufsize = 5


    def __init__(self, nom):
        self.fichier = io.open(nom, mode="r", encoding="utf-8")     # Ouverture mode UTF-8
        self.blocs_reponses = list()


    def Read0(self):
        c = self.fichier.read(1)
        self.buffer = self.buffer + c
        self.buffer = self.buffer[-self.bufsize:]
        #print(c," ",self.buffer)
        return c


    def Read(self):
        c = self.Read0()
        if (len(c)==0): return ""
        if (ord(c)==10): return self.Read()
        if (c=="/"):
            c1 = self.ReadCommentaire()
            if (ord(c1)==10): return self.Read()
            if (c1=="/"):
                return "/"
            else:
                return c1
        return c


    def ReadCommentaire(self):
        c = self.Read0()
        if (c=="/"):
            while True:
                c = self.fichier.read(1)
                if ((len(c)==0) or (ord(c)==10)): return chr(10)
        else:
            return c


    def ReadTitre(self):
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
        self.blocs_reponses = ""
        while True:
            c = self.Read()
            if (len(c)==0): break
            if (c == "}"): break
            self.blocs_reponses += c


    def ReadGIFT(self):
        self.question = ""
        while True:
            c = self.Read()
            if (len(c)==0): break;
            if (c == "{"):
                self.ReadBlocReponse()
                self.question += "%Q"
                continue
            if (c == ":"):
                c1 = self.ReadTitre()
                if (c1 != None): pass
                continue
            self.question += c


q = Question("Test001.txt")

q.ReadGIFT()
print("\""+q.titre+"\"")
print("\""+q.question+"\"")
#print("\""+q.blocs_reponses+"\"")

bloc = BlocReponse()
bloc.Parse(q.blocs_reponses)
