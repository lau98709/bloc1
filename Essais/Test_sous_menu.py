# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:13:12 2019

@author: Raihei
"""

from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *
from Format_GIFT import *
from random import randint

#Choix d'une réponse du type Vrai/Faux
def VraiFaux():
    print("Vrai/Faux")
    Screen().input('Appuyer [Entrer] pour continuer')

#Choix d'une réponse du QCM avec réponse sous forme de texte
def QcmTexte():
    print("QCM avec du texte à saisir")
    Screen().input('Appuyer [Entrer] pour continuer')

#Choix d'une réponse du QCM avec réponse sous forme de chiffres
def QcmNumerique():
    print("QCM avec des chiffres à saisir")
    Screen().input('Appuyer [Entrer] pour continuer')

#Choix d'une réponse ouverte
def ReponseOuverte():
    print("Réponse ouverte")
    Screen().input('Appuyer [Entrer] pour continuer')


#Choix de la saisie manuelle des questions
def SaisieManuelle():
    print("Saisie manuelle des questions")
    Screen().input('Appuyer [Entrer] pour continuer')
    TitreQuestion=str(input("Saisir le titre de la question"))
    EnonceQuestion=str(input("Saisir l'énoncé de la question"))
    
def main():
    #Création du sous-menu afin de définir le type de réponse 
    menu2 = MultiSelectMenu("Types de réponses possibles", "Choisir le type souhaité",
                        epilogue_text=("Please select one or more entries separated by commas, and/or a range "
                                          "of numbers. For example:  1,2,3   or   1-4   or   1,3-4"),
                       exit_option_text=('Exit Application'))
    
    #Ajout des choix possibles pour les types de réponses
    menu2.append_item(FunctionItem("Vrai/Faux", VraiFaux, args=[]))
    menu2.append_item(FunctionItem("QCM avec du texte à saisir", QcmTexte, args=[]))
    menu2.append_item(FunctionItem("QCM avec des chiffres à saisir", QcmNumerique, args=[]))
    menu2.append_item(FunctionItem("Réponse ouverte", ReponseOuverte, args=[]))
    
    #Affichage du menu
    menu2.start()
    menu2.join()
    
if __name__ == "__main__":
    main()
