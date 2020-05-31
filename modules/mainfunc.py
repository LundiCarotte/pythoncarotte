# -*-coding:utf-8 -*

from .classeArticle import *
from .fonctions import *

#################################################
# FONCTION PRINCIPALE
#################################################

def txtenhtml(fileName, format):
	data = getData(fileName)
	makeFiles(data, format)

def getData(fileName):
	"""Reçoit en argument le nom du fichier texte contenant les informations de l'article. Renvoie un objet de la classe Article, dont l'attribut texte contient les informations de l'article."""

	# ensuite on vérifie l'existence du fichier en .txt
	# si le fichier texte n'existe pas, on arrête la fonction
	if os.path.isfile(fileName) is not True:
		print("Erreur : le fichier %s n'existe pas." % fileName)
		return None

	# on récupère les données textes
	with open(fileName, "r", encoding='utf-8') as f:
		txt = f.read()

	# on définit le titre web du document
	# il correspond à l'url qui sera utilisée pour accéder à l'article
	titre_web = extrairecurly(txt,repere_titre_web)
	titre_web = enlever_espaces(titre_web)
	# si le titre du document n'est pas défini dans le fichier .txt, on demande à l'utilisateur d'entrer le titre web du fichier
	while titre_web == '':
		titre_web = input("Entrez le titre web du fichier : ")

	# on crée le dossier qui va contenir les fichiers HTML
	folder = "articles/{0}".format(titre_web)
	if not os.path.exists(folder):
	    os.makedirs(folder)

	# ici on génère un fichier "propre" à partir du fichier transmis
	listeblocs = creerListeBlocs(all)
	txt_propre = creerFichierTextePropre(txt, listeblocs)
	cheminFichier = "articles/{0}/{0}.txt".format(titre_web)
	ecrire_fichier(cheminFichier,txt_propre)

	data = Article(txt_propre,'',titre_web,[])

	return data

def makeFiles(data, format):

	############ QUEL FORMAT DE FICHIER VEUT-ON ? ############

	# CHOIX N 1 : hebdomadaire
	#
	if (format == "hebdomadaire"):

		############ CRÉATION FICHIER MAIL ############
		#
		# génération du html pour Mailjet
		#
		# on crée une instance de la classe Article, de catégorie "mail"
		listeblocs = creerListeBlocs(mail)
		article = Article(data.txt,"mail",data.titre_web,listeblocs)
		article.generer_html()

		############ CRÉATION FICHIER WEB ############
		#
		# génération du html pour le site web
		#
		# on crée une instance de la classe Article, catégorie "web"
		listeblocs = creerListeBlocs(web)
		article = Article(data.txt,"web",data.titre_web,listeblocs)
		article.generer_html()

		# also json
		article.generer_json()

	# CHOIX N 2
	# si on veut un fichier html pour la catégorie lundicarotte.fr/articles/ :
	elif (format == "artsup"):
		# faire l'article sup en chargeant le bon template
		article = Article(data.txt,"artsup",data.titre_web,listeblocs_artsup)
		article.generer_html()
	elif (format == "minimail"):
		# si on veut un minimail de type "les vacances de lundicarotte" :
		listeblocs = [logo,titre,date,intro,dev,outro,auteurs,partage,don,pied]
		article = Article(data.txt,"mail",data.titre_web,listeblocs)
		article.generer_html()
	else:
		raise Exception("Wrong content for string format: " + format)