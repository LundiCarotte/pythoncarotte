# -*-coding:utf-8 -*
from lc_func import * 
from lc_var import *
import sys

# vérifier si argv[1] existe
if (len(sys.argv)<2):
	print("entrée incorrecte : spécifier nom fichier texte en argument")
	# mettre fin au programme python

# on récupère le nom du fichier texte (nft) entré au clavier
nftclavier =  sys.argv[1]

# astuce : on peut entrer un nom en .docx ou .doc ou .odt
	# si c'est le cas, ça génère le .txt
	# si on passe le txt en argument, ça ne fait rien
[nft,nft_txt] = doctotxt(nftclavier) 

# ensuite on vérifie l'existence du fichier en .txt #### À FAIRE
#


# on récupère les données textes
txt = lc_lire(nft_txt)

# on définit le titre du document
if txt.find(rep_titre_web) == -1:
	titre_web = nft
else:
	titre_web = extrairecurly(txt,rep_titre_web)

# quel type de fichier veut-on ?

# si on veut un hebdomadaire :
if (len(sys.argv) == 2): # si on veut un article hebdo lundicarotte (web et mail)
	type_lc = "hebdo"
	# on utilise le template lundicarotte
	html = lc_lire(template_html_lundicarotte)
	# on commence par l'article web
	# on veut pas le logo, don, actu, courrier, pied
	# listeblocs = [reseaux,titre,date,image,intro,dev,outro,auteurs,partage,don,actu,courrier,quizz,pied]
#	listeblocs = [titre,date,image,intro,dev,outro,auteurs,partage,quizz]
	listeblocs = [titre,date,image,intro,dev,outro,auteurs,partage]
	[html,txt] = ajouter_html(html,txt,listeblocs,type_lc,nft)
	# génerer le nom du fichier web
	nom_fichier_web = "lundicarotte-"+titre_web+".html"
	ecrire_html_final(nom_fichier_web,html)

	# une fois qu'on a écrit la page web, on génère le mail
	# on ajoute logo, don, actu, courrier, pied
	listeblocs = [logo,don,actu,courrier,pied]
	[html,txt] = ajouter_html(html,txt,listeblocs,type_lc,nft)
	nom_fichier_mail = "lundicarotte-"+titre_web+"-MAIL.html"
	ecrire_html_final(nom_fichier_mail,html)

	# on crée aussi le fichier .json
	nom_json = titre_web+".json"
	url_image = extrairecurly(txt,rep_url_image)
	titre_page = extrairecurly(txt,rep_titre)
	description = extrairecurly(txt,rep_partage_description)
	json = creer_json(titre_web,url_image,titre_page,description)
	ecrire_html_final(nom_json,json)

if (len(sys.argv) == 3):

	# si on veut un article supplémentaire :
	if sys.argv[2] == "artsup":
		# faire l'article sup en chargeant le bon template
		type_lc = "artsup"
		html = lc_lire(template_html_artsup)
		listeblocs = [titre,intro,dev,outro,auteurs,partage]
		# 
		[html,txt] = ajouter_html(html,txt,listeblocs,type_lc,nft)
		# génerer le nom du fichier web
		nom_fichier_web = "article-"+titre_web+".html"
		ecrire_html_final(nom_fichier_web,html)

	# si on veut un minimail de type "les vacances de lundicarotte" :
	elif sys.argv[2] == "minimail":
		type_lc = "artsup"
		html = lc_lire(template_html_artsup)
		listeblocs = [titre,dev,auteurs,pied]
		# 
		[html,txt] = ajouter_html(html,txt,listeblocs,type_lc,nft)
		# génerer le nom du fichier web
		nom_fichier_web = "article-"+titre_web+".html"
		ecrire_html_final(nom_fichier_web,html)
	else:
		print("argument invalide")
if (len(sys.argv) > 3):
	print("\nN'entrez pas plus de 2 arguments svp :)\n")
