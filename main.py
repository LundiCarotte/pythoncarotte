#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
import modules.mainfunc as mainfunc

arguments = sys.argv[1:]
if len(arguments) == 0:
    print("Erreur : nom de fichier manquant.")
    print("Essayez plutôt : 'python main.py nom_du_fichier [arguments optionnels]'\n")
else:
    mainfunc.txtenhtml(arguments)
