# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

@author: LAU Wai Tong Christian

Test d'écriture de fichier GIFT

"""

from Format_GIFT import *

q = Question()

q.ReadGIFT("Test000.txt")

q.WriteHTML("Test_html0.html","QuestionTemplate.html")