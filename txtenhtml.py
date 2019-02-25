#!/usr/bin/env python3
# -*-coding:utf-8 -*

from module.fonctions import *
from module.variables import *
from module.styles import *
from module.classes import *
import sys
import os

# le lien google analytics est défini dans le fichier module/variables

# liste des blocs disponibles :
listeblocs = [logo,titre,date,image,auteurs,partage,don,actu,courrier,quizz,pied]
# les blocs intro, dev et outro sont présents par défaut

listeblocs_web = [titre,date,image,auteurs,partage,quizz]

listeblocs_mail = [logo,titre,date,image,auteurs,partage,don,actu,courrier,quizz,pied]

listeblocs_artsup = [titre,auteurs,partage]


# vérifier si argv[1] existe
if (len(sys.argv)<2):
	print("entrée incorrecte : spécifier nom fichier texte en argument")
	sys.exit()
	# mettre fin au programme python

# on récupère le nom du fichier texte entré au clavier
entree_clavier =  sys.argv[1]

# ensuite on vérifie l'existence du fichier en .txt
# si le fichier texte n'existe pas, on arrête le programme
if os.path.isfile(entree_clavier) is not True:
	print("Erreur : le fichier %s n'existe pas." % entree_clavier)
	sys.exit()


# on récupère les données textes
txt = lc_lire(entree_clavier)

# on définit le titre web du document
# il correspond à l'url qui sera utilisée pour accéder à l'article
titre_web = extrairecurly(txt,rep.titre_web)
titre_web = enlever_espaces(titre_web)
# si le titre du document n'est pas défini dans le fichier .txt, on demande à l'utilisateur d'entrer le titre web du fichier
while titre_web == '':
	titre_web = input("Entrez le titre web du fichier : ")


# on crée le dossier qui va contenir les fichiers html
if not os.path.exists(titre_web):
    os.makedirs(titre_web)

# ici on génère un fichier "propre" à partir du fichier transmis

txt_propre = generer_fichier_txt_propre(txt,listeblocs)
ecrire_fichier(titre_web+'/'+titre_web+'.txt',txt_propre)

#print(txt_propre)

################################################################
#
############ QUEL TYPE DE FICHIER VEUT-ON ? ############
#
################################################################


################################
# CHOIX N 1
################################
#
# si on veut un hebdomadaire
#
# dans ce cas le seul argument passé en ligne de commande est le nom du fichier texte
if (len(sys.argv) == 2):

	############ CRÉATION FICHIER MAIL ############
	#
	# génération du html pour Mailjet
	#
	# on crée un objet de classe Article, de catégorie "mail"
	article = Article(txt_propre,"mail",titre_web,listeblocs_mail)
	article.generer_html()

	############ CRÉATION FICHIER WEB ############
	#
	# génération du html pour le site web
	#
	# on crée un objet (?) de classe Article
	article = Article(txt_propre,"web",titre_web,listeblocs_web)
	article.generer_html()
	article.generer_json()


################################
# CHOIX N 2
################################

if (len(sys.argv) == 3):

	# si on veut un fichier html pour la catégorie lundicarotte.fr/articles/ :
	if sys.argv[2] == "artsup":
		# faire l'article sup en chargeant le bon template
		article = Article(txt_propre,"artsup",titre_web,listeblocs_artsup)
		article.generer_html()

	# si on veut un minimail de type "les vacances de lundicarotte" :
	elif sys.argv[2] == "minimail":
		listeblocs = [logo,titre,date,intro,dev,outro,auteurs,partage,don,pied]
		article = Article(txt_propre,"mail",titre_web,listeblocs)
		article.generer_html()
	else:
		print("argument invalide")

if (len(sys.argv) > 3):
	print("\nN'entrez pas plus de 2 arguments svp :)\n")
