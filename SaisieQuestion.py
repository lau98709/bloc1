# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

@author: Raihei Lie

Saisie des questions ou génération automatique des questions de conversion

Ce programme, par un ensemble de menu et de question, crée les questions
et les enregistre au format GIFT

"""

from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from Format_GIFT import *
from random import randint


def Sauvegarde(q):
    print("Donnez le nom du fichier :")
    s = input()
    q.WriteGIFT(s)


#Choix d'une réponse du type Vrai/Faux
def VraiFaux():

    q = Question();
    q.bloc_reponses = BlocReponses();
    q.bloc_reponses.type = 2

    print("Question vrai ou faux")

    print("Entrez le titre de la question :")
    q.titre = input()

    print("Saisissez l'énoncé de la question :")
    q.enonce = input()

    print("Réponse : vrai ou faux ? [v/f]")
    s = input()
    q.bloc_reponses.vraifaux = (s.lower() == "v")

    # Sauvegarde au format GIFT
    Sauvegarde(q)


#Choix d'une réponse du QCM avec réponse sous forme de texte
def QcmTexte():

    q = Question();
    q.bloc_reponses = BlocReponses();
    q.bloc_reponses.type = 0
    q.bloc_reponses.reponse = list()

    print("QCM avec du texte")

    print("Entrez le titre de la question :")
    q.titre = input()

    print("Saisissez l'énoncé de la question :")
    q.enonce = input()

    while True:
        print("Donnez le nombre de réponses :")
        s = input()
        if (s.isnumeric()):
            nrep = int(s)
            break

    for i in range(0,nrep):
        rep = Reponse()
        rep.type = 0

        print("Réponse %d : Saisissez la réponse :" % (i+1))
        s = input()
        rep.text = s

        print("Réponse %d : réponse exact ? [o/n]" % (i+1))
        s = input()
        s.lower()
        if (s == "o"):
            rep.exact = True
        else:
            rep.exact = False

        if (rep.exact == False):
            print("Réponse %d : pourcentage de points ?" % (i+1))
            rep.pourcent = input()

        print("Réponse %d : rétroaction pour cette réponse" % (i+1))
        rep.retroaction = input();

        q.bloc_reponses.reponses.append(rep)

    print("La suite de l'énoncé :")
    s = input()
    q.enonce = q.enonce + " %Q " + s

    print("Rétroaction globale :")
    q.bloc_reponses.retroaction = input()

    # Sauvegarde au format GIFT
    Sauvegarde(q)


#Choix d'une réponse du QCM avec réponse sous forme de chiffres
def QcmNumerique():

    q = Question();
    q.bloc_reponses = BlocReponses();
    q.bloc_reponses.type = 1
    q.bloc_reponses.reponse = list()

    print("Question numérique")

    print("Entrez le titre de la question :")
    q.titre = input()

    print("Saisissez l'énoncé de la question :")
    q.enonce = input()

    while True:
        print("Donnez le nombre de réponses :")
        s = input()
        if (s.isnumeric()):
            nrep = int(s)
            break

    for i in range(0,nrep):
        rep = Reponse()
        rep.type = 1

        while True:
            print("Réponse %d : Type de réponse :" % (i+1))
            print("1. Valeur exacte")
            print("2. Interval")
            print("3. Avec marge d'erreur")
            s = input()
            if (s.isnumeric()):
                typ = int(s)
                if ((1 <= typ) and (typ <=3)):
                    break;

        if (typ == 1):

            print("Réponse %d : Entrez la valeur" % (i+1))
            s = input()
            rep.valeur = int(s)
            rep.max = rep.min = rep.valeur
            rep.delta = 0

        elif (typ == 2):

            print("Réponse %d : Entrez la valeur min de l'interval :" % (i+1))
            s = input()
            rep.min = int(s)
            print("Réponse %d : Entrez la valeur max de l'interval :" % (i+1))
            s = input()
            rep.max = int(s)
            rep.valeur = (rep.min + rep.max)/2
            rep.delta = -1

        elif (typ == 3):

            print("Réponse %d : Entrez la valeur :" % (i+1))
            s = input()
            rep.valeur = int(s)
            print("Réponse %d : Entrez la marge :" % (i+1))
            s = input()
            rep.delta = int(s)

        print("Réponse %d : Est-ce une bonne réponse ? [o/n]" % (i+1))
        s = input()
        rep.exact = (s.lower() == "o")

        if (not rep.exact):
            print("Réponse %d : Pourcentage des points ?" % (i+1))
            rep.pourcent = input()

        print("Réponse %d : Rétroaction ?" % (i+1))
        rep.retroaction = input()

        q.bloc_reponses.reponses.append(rep)

    print("La suite de l'énoncé :")
    s = input()
    q.enonce = q.enonce + " %Q " + s

    print("Rétroaction globale :")
    q.bloc_reponses.retroaction = input()

    # Sauvegarde au format GIFT
    Sauvegarde(q)


#Choix d'une réponse ouverte
def ReponseOuverte():

    q = Question();
    q.bloc_reponses = BlocReponses();
    q.bloc_reponses.type = 3

    print("Question ouverte")

    print("Entrez le titre de la question :")
    q.titre = input()

    print("Saisissez l'énoncé de la question :")
    q.enonce = input()

    # Sauvegarde au format GIFT
    Sauvegarde(q)


#Choix de la saisie manuelle des questions
def SaisieManuelle():
    print("Saisie manuelle des questions")
#    Screen().input('Appuyer [Entrer] pour continuer')
#    TitreQuestion=str(input("Saisir le titre de la question "))
#    EnonceQuestion=str(input("Saisir l'énoncé de la question "))

    #Création du sous-menu afin de définir le type de réponse
    menu2 = MultiSelectMenu("Types de réponses possibles", "Choisir le type souhaité",
        epilogue_text=(""),
        exit_option_text=('Exit Application'))

    #Ajout des choix possibles pour les types de réponses
    menu2.append_item(FunctionItem("QCM avec du texte", QcmTexte, args=[]))
    menu2.append_item(FunctionItem("Numérique", QcmNumerique, args=[]))
    menu2.append_item(FunctionItem("Vrai/Faux", VraiFaux, args=[]))
    menu2.append_item(FunctionItem("Réponse ouverte", ReponseOuverte, args=[]))

    #Affichage du menu
    menu2.start()
    menu2.join()


#Choix de la génération automatique des questions
def GenerationAuto():

    bases = ['décimale','hexadécimale','binaire']

    q = Question()
    q.titre = "Question de conversion"
    i1 = randint(0,2)
    while True:
        i2 = randint(0,2)
        if (i1 != i2): break

    q.bloc_reponses = BlocReponses()
    q.bloc_reponses.type = 1
    q.bloc_reponses.reponses = list()

    rep = Reponse()
    rep.type = 1
    rep.exact = True

    # Choix du nombre à convertir
    if (i2 == 1):       # hexadécimale
        nombre = randint(0,1024)
    elif (i2 == 2):     # binaire
        nombre = randint(0,256)
    else:               # décimale
        nombre = randint(0,1024)

    # Pour la solution, on retire les préfixes "0b" ou "0x"
    # et les lettres hexadécimales sont en Majuscule
    rep.valeur = nombre
    if (i2 == 1):
        rep.text = hex(nombre)[2:].upper()
    elif (i2 == 2):
        rep.text = bin(nombre)[2:].upper()
    else:
        rep.text = str(nombre)
        
    rep.pourcent = None
    rep.retroaction = "Bonne réponse"

    q.bloc_reponses.reponses.append(rep)

    if (i1 == 1):
        aconvertir = hex(nombre)
    elif (i1 == 2):
        aconvertir = bin(nombre)
    else:
        aconvertir = str(nombre)

    q.enonce = "Convertir le nombre %s \'%s\' en %s." % (bases[i1],aconvertir,bases[i2])

    print(q.enonce)
    print("Réponse : %s" % (rep.text))

    # Sauvegarde au format GIFT
    Sauvegarde(q)


# Création du menu principal
menu = MultiSelectMenu("Menu principal", "Choisir l'option souhaitée",
    epilogue_text=(""),
    exit_option_text=('Exit Application'))  # Customize the exit text

# Ajout des choix possibles au menu principal
menu.append_item(FunctionItem("Saisie manuelle des questions", SaisieManuelle, args=[]))
menu.append_item(FunctionItem("Génération automatique des questions de conversion", GenerationAuto, args=[]))

# Affichage du menu
menu.start()
menu.join()
