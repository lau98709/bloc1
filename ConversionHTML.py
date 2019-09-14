# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

@author: Tautu Tamatai

Ecriture de fichier GIFT
avec questions d'interrogation pour les noms de fichiers
ou par les arguments de ligne de commande

"""

from Format_GIFT import *
import sys


if (len(sys.argv) >= 3):
    gift_name = sys.argv[1]
    out_name = sys.argv[2]
else:
    print("Donnez le nom du fichier GIFT de la question :")
    gift_name = input()   
    print("Donnez le nom du fichier HTML en sortie :")
    out_name = input()


q = Question()

q.ReadGIFT(gift_name)

q.WriteHTML(out_name,"QuestionTemplate.html")
