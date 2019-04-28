#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys, os


# on s'assure que 'pythoncarotte' est dans le PATH
dossier = os.path.dirname(os.path.abspath(__file__))
while not dossier.endswith('pythoncarotte'):
    dossier = os.path.dirname(dossier)
if dossier not in sys.path:
    sys.path.append(dossier)

from module.mainfunc import *

data = getData('tests/gdoc.txt')[0]

x = data.txt

y = """
nsasuttuieenrrsatsuie nrrstau ienrsat ue

SOUS-TITRE{}
nrsatuie anuriste nrrau einrsat iu
"""
