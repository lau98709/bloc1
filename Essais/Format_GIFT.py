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
    # Représentation d'une réponse
    # type : 0 = QCM textuel
    #        1 = numérique
    #        2 = vrai ou faux
    
    type = None
    exact = False
    pourcent = 100
    text = None
    valeur = 0
    min = 0
    max = 0
    retroaction = None

    def Parse(self, s):
        # Interprétation d'une réponse
        
        # Extraire la rétroaction si elle existe
        self.retroaction = ""
        ri = s.find('#')
        if (ri != -1):
           self.retroaction = s[(ri+1):]
           s = s[:ri]
        #print("\""+self.retroaction+"\"")

        # Bonne réponse, mauvaise réponse
        if (s[0]=='='):
            self.exact = True
        elif (s[0]=='~'):
            self.exact = False

        # Extraire le texte de la réponse
        if ((s[0]=='=') or (s[0]=='~')):
            s2 = s[1:]
            if (s2[0]=="%"):
                # Extraction du pourcentage
                for i in range(1,len(s2)):
                    if (s2[i]=='%'): break
                self.pourcent = int(s2[1:i])
                s2 = s2[i+1:]                
                #print(pourcent, "\""+s2+"\"")
            else:
                self.pourcent = 100
            self.text = s2
            self.type = 0


    def ParseNum(self):
        # Interprétation d'une réponse numérique
                
        i = self.text.find("..")
        if (i != -1):           # Si interval
            self.min = int(self.text[0:i])
            self.max = int(self.text[i+2:])
            self.valeur = (self.min + self.max)/2
        elif (self.text.find(':') != -1):
            f = self.text.split(':')
            self.valeur = int(f[0])
            if (len(f) == 2):
                # Si 2 champs, une valeur, un delta
                delta = int(f[1])
                self.min = self.valeur - delta
                self.max = self.valeur + delta
        else:
            # Valeur unique
            self.valeur = self.min = self.max = int(self.text)
        self.type = 1
        #print(self.valeur, self.min, self.max)
    

class BlocReponses():
    # Représentation d'un bloc de réponse
    
    reponses = None             # Liste des réponses
    type = 0                    # Type de questions
    retroaction = ""            # Rétroaction globale

    def __init__(self):
        self.reponses = list()


    def Parse(self, s):
        # Interprétation d'un bloc de réponse

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
            # Si question type vrai ou faux
            self.type = 2    # TRUE or FALSE

        else:
            # Type de question numérique ou QCM
            if (s[0]=='#'):
                self.type = 1       # Numérique
                s = Trim(s[1:])     # Retrait du signe #
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
    # Représentation d'une question
    
    titre = ""                  # Titre de la question entre ::
    enonce = ""               # Texte de la question
    bloc_reponses = None       # blocs reponses

    fichier = None              # Objet pour lecture écriture du fichier

    buffer = ""                 # Buffer de lecture du fichier
    bufsize = 5                 #   contient les derniers caractères lus


    def __init__(self):
        pass

    def Read0(self):
        # Lecture bufferisé du fichier
        #   Permet de retenir les derniers caractères lus
        c = self.fichier.read(1)
        self.buffer = self.buffer + c
        self.buffer = self.buffer[-self.bufsize:]
        #print(c," ",self.buffer)
        return c


    def Read(self):
        # Lecture du fichier en ignorant les "retours chariot" et
        #   les commentaires
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
        # Rejet des commentaires
        # (Lire jusqu'à la fin de la ligne)
        # Le pointeur de fichier doit être sur le 2e '/' du commentaire
        c = self.Read0()
        if (c=="/"):
            while True:
                c = self.fichier.read(1)
                if ((len(c)==0) or (ord(c)==10)): return chr(10)
        else:
            return c


    def ReadTitre(self):
        # Lecture du titre
        # Le pointeur de fichier doit être sur le 2e ':' du titre
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


    def ReadBlocReponses(self):
        # Lecture d'un bloc réponse {}
        s = ""
        while True:
            c = self.Read()
            if (len(c)==0): break
            if (c == "}"): break
            s += c
        return s


    def ReadGIFT(self, nomfichier):
        # Lecture d'un fichier GIFT
        self.fichier = io.open(nomfichier, mode="r", encoding="utf-8")     # Ouverture mode UTF-8
        self.enonce = ""
        while True:
            c = self.Read()
            if (len(c)==0): 
                break;
            elif (c == "{"):
                # Lecture de bloc de réponses
                s = self.ReadBlocReponses()
                self.bloc_reponses = BlocReponses()
                self.bloc_reponses.Parse(s)
                self.enonce += "%Q"
                continue
            elif (c == ":"):
                # Lecture d'un titre
                c1 = self.ReadTitre()
                if (c1 != None): pass
                continue
            self.enonce += c
            
    
    def WriteGIFT(self, nomfichier):
        self.fichier = io.open(nomfichier, mode="w", encoding="utf-8")     # Ouverture mode UTF-8
        if (self.title != ""): self.fichier.write("::"+self.titre+"::")
        if (self.enonce != ""): self.fichier.write(self.enonce)
        if (self.bloc_reponses != None):
            pass

#        
#q = Question()
#
#q.ReadGIFT("Test001.txt")
#print("\""+q.titre+"\"")
#print("\""+q.enonce+"\"")
#print(len(q.bloc_reponses.reponses))
#for res in q.bloc_reponses.reponses:
#    print(res.type, res.exact, res.text, res.valeur)
