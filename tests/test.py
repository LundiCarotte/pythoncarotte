#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys, os


# on s'assure que 'pythoncarotte' est dans le PATH
dossier = os.path.dirname(os.path.abspath(__file__))
while not dossier.endswith('pythoncarotte'):
    dossier = os.path.dirname(dossier)
print(dossier)
if dossier not in sys.path:
    sys.path.append(dossier)

from module.mainfunc import *

listeblocs = creerListeBlocs(mail)
article = Article(txt_propre,"mail",titre_web,listeblocs)

if not inputString: # if void input string
	return None

dataInputString = creerListeElemNonVide(inputString)

fileName = dataInputString[0]

# ensuite on vérifie l'existence du fichier en .txt
# si le fichier texte n'existe pas, on arrête la fonction
if os.path.isfile(fileName) is not True:
	print("Erreur : le fichier %s n'existe pas." % fileName)
	return None

# on récupère les données textes
with open(fileName,"r") as f:
	txt = f.read()

# on définit le titre web du document
# il correspond à l'url qui sera utilisée pour accéder à l'article
titre_web = extrairecurly(txt,repere_titre_web)
titre_web = enlever_espaces(titre_web)
# si le titre du document n'est pas défini dans le fichier .txt, on demande à l'utilisateur d'entrer le titre web du fichier
while titre_web == '':
	titre_web = input("Entrez le titre web du fichier : ")


# on crée le dossier qui va contenir les fichiers HTML
if not os.path.exists(titre_web):
    os.makedirs(titre_web)



# ici on génère un fichier "propre" à partir du fichier transmis
listeblocs = creerListeBlocs(all)
txt_propre = creerFichierTextePropre(txt,listeblocs)
ecrire_fichier(titre_web+'/'+titre_web+'.txt',txt_propre)


print(article.titre_web)
