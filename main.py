#!/usr/bin/env python3
# -*-coding:utf-8 -*

import os
import sys

import modules.mainfunc as mainfunc

arguments = sys.argv[1:]

if len(arguments) == 0:
    print("ERREUR : nom de fichier manquant.")
    print("Essayez plutôt : 'python main.py nom_du_fichier [arguments optionnels]")
    exit()

if len(arguments) > 2:
    print("ERREUR: n'entrez pas plus de 2 arguments svp :)")
    exit()

fileName = arguments[0]
if (not os.path.isfile(fileName)):
    print("ERREUR : le fichier '{0}' n'existe pas".format(fileName))
    exit()

format = "hebdomadaire"
if len(arguments) == 2:
    format = arguments[1]
    if (not format in ["artsup", "minimail"]):
        print("ERREUR: format de fichier '{0}' invalide.".format(format))
        print("Formats autorisés: artsup, minimail.")
        exit()

mainfunc.txtenhtml(fileName, format)