# -*-coding:utf-8 -*

from .classeArticle import *
from .fonctions import *

#################################################
# FONCTION PRINCIPALE
#################################################

def txtenhtml(inputString):
	(data, dataInputString) = getData(inputString)
	makeFiles(data, dataInputString)

def getData(inputString):
	"""Reçoit en argument le nom du fichier texte contenant les informations de l'article. Renvoie un objet de la classe Article."""

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
	with open(fileName, "r") as f:
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

	data = Article(txt_propre,'',titre_web,[])

	return(data, dataInputString)

def makeFiles(data, dataInputString):

	############ QUEL TYPE DE FICHIER VEUT-ON ? ############

	# CHOIX N 1
	#
	# si on veut un hebdomadaire
	#
	# dans ce cas le seul argument passé en ligne de commande est le nom du fichier texte
	if (len(dataInputString) == 1):

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


	################################
	# CHOIX N 2
	################################

	if (len(dataInputString) == 2):

		# si on veut un fichier html pour la catégorie lundicarotte.fr/articles/ :
		if dataInputString[1] == "artsup":
			# faire l'article sup en chargeant le bon template
			article = Article(data.txt,"artsup",data.titre_web,listeblocs_artsup)
			article.generer_html()

		# si on veut un minimail de type "les vacances de lundicarotte" :
		elif dataInputString[1] == "minimail":
			listeblocs = [logo,titre,date,intro,dev,outro,auteurs,partage,don,pied]
			article = Article(data.txt,"mail",data.titre_web,listeblocs)
			article.generer_html()
		else:
			print("argument invalide")
			return None

	if (len(dataInputString) > 2):
		print("\nN'entrez pas plus de 2 arguments svp :)\n")
		return None
