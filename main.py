#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
import modules.mainfunc as mainfunc

if len(sys.argv) <= 1:
    print("Erreur : nom de fichier manquant.")
    print("Essayez plutôt : 'python main.py nom_du_fichier [arguments optionnels]'\n")
else:
    arguments = ' '.join(sys.argv[1:])
    mainfunc.txtenhtml(arguments)
