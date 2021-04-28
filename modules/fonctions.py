# -*-coding:utf-8 -*
""" module contenant les fonctions nécessaires à la génération du template html"""

import os
import sys
import subprocess
import functools

from .listeBlocs import *
from .styleBlocs import *
from .variables import *


#################################################
# MISE EN FORME DE L'INPUT
#################################################

def creerListeBlocs(typeArticle):

	if typeArticle == all:
		liste = [logo,titre,date,intro,image,dev,outro,auteurs,partage,don,actu,courrier,quizz,pied]

	elif typeArticle == mail:
		liste = [logo,titre,date,intro, image,dev, outro,auteurs,partage,don,actu,courrier,quizz,pied]

	elif typeArticle == web:
		liste = [titre,date,intro,image,dev,outro,auteurs,partage,quizz]

	else:
		liste = [titre,intro,dev,outro,auteurs,partage]

	return(liste)


#################################################
# VÉRIFICATION STRUCTURE TEXTE
#################################################

def creerListeBoxBrackets(txt):
	"""renvoie une liste de tupples, chaque tupple contenant les indices (dans la chaine de caractères txt) de crochets ouvrant [ et fermant ] entre lesquels il n'y a pas d'autre crochets."""

	listeBB = []
	open = False
	indOpen = -1
	for i in range(len(txt)):
		if txt[i] == '[':
			if open == False:
				open = True
				indOpen = i
			else:
				indOpen = i
		if txt[i] == ']':
			if open == True:
				open = False
				listeBB.append((indOpen,i))
	return(listeBB)

def charsAround(i,txt):
	"""return characters around txt[i]"""
	start = (0,i-20)[i-20>=0]
	stop = (len(txt),i+20)[i+20<len(txt)]
	return(txt[start:stop])

def charsAroundString(myString,txt):
	i = txt.find(myString)
	j = i + len(myString)
	k = len(txt)
	start = (0, i-20)[i-20 >= 0]
	stop = (k, j+20)[j+20 < k]
	return(txt[start:stop])

def charsBeforeAfter(myString,txt):
	i = txt.find(myString)
	j = i + len(myString)
	k = len(txt)
	start = (0, i-20)[i-20 >= 0]
	stop = (k, j+20)[j+20 < k]
	return('\n'+txt[start:i]+'\n*****\n'+txt[j+1:stop]+'\n')


def warnSingleBracket(txt):
	# on récupère la liste des box brackets
	listeBB = creerListeBoxBrackets(txt)
	listeBB2 = [i[j] for i in listeBB for j in [0,1]]
	countAll = [i for i in range(len(txt)) if (txt[i] == '[' or txt[i] == ']')]
	for i in countAll:
		if i not in listeBB2:
			msg = charsAround(i,txt)
			print('Il y a un crochet esseulé à cet endroit : "'+msg+'"')



#################################################
# CRÉATION DU CONTENU DE L'ARTICLE
#################################################

def creerContenu(article, bloc):
	""" Retourne le contenu (HTML) d'un bloc du html"""

	contenu = ""
	nom = bloc.nom

	# si le bloc est de type "a":
	if bloc.a:
		if article.repereExiste(bloc.repereTexte):
			contenu = extrairecurly(article.txt,bloc.repereTexte)

	elif nom == logo:
		contenu = bloc.code

	elif nom in [intro,dev,outro]:
		if (article.repereExiste(bloc.repereTexte1) and article.repereExiste(bloc.repereTexte2)):
			data = extrairesandwich(article.txt,bloc.repereTexte1,bloc.repereTexte2)
			contenu = mise_en_forme(data,article.titre_web,article.categorie)

	elif nom == image:
		if article.repereExiste(bloc.repereTexte):
			data = extrairecurly(article.txt,bloc.repereTexte)
			data = enlever_espaces_inutiles(data)
			if data != '':
				contenu = bloc.code
				contenu = contenu.replace("url_Image",data)

	elif nom == auteurs:
		if article.repereExiste(bloc.repereTexte):
			listeLignes = recup_liste(article.txt,bloc.repereTexte,article.titre_web,article.categorie)
			contenu = ''
			nbLines = len(listeLignes)
			contenu = listeLignes[0]
			if nbLines >1:
				for i in range(1,nbLines):
					contenu+=bloc.codeApres+bloc.codeAvant+listeLignes[i]

	elif nom == partage:
		url = generer_url(article.titre_web,article.categorie)
		contenu = bloc.code
		contenu = contenu.replace("_URL_",url)

	elif nom == don:
		contenu = bloc.code

	elif nom == actu:
		# on récupère données actu
		n = 0
		data_jc = ['']
		if article.repereExiste(bloc.repereTexte):
			actus  = recup_liste(article.txt,bloc.repereTexte,article.titre_web,article.categorie)
			n = len(actus)
        # on récupère les données du jeudicarotte
		if article.repereExiste(bloc.repereJc):
			data_jc = recup_data_jeudicarotte(article.txt,bloc.repereJc)

        # s'il y a au moins une actu/jeudicarotte
        # on créé la case actu

		if (n != 0 or data_jc[0] != ''):
			contenu = bloc.case_actu_entree
			if (n >= 0):
				for i in range(0,n):
					contenu += bloc.texte_actu_entree+actus[i]+bloc.texte_actu_sortie
            # JeudiCarotte
			if (data_jc[0] != ''):
                # si on veut remplacer le jeudicarotte habituel par autre chose
				if (len(data_jc) >= 4):
					alt = ','.join(data_jc[3:])
					alt = mise_en_forme(alt,article.titre_web,article.categorie)
					contenu += bloc.texte_actu_entree+alt+bloc.texte_actu_sortie
				else:
					jc = bloc.texte_jc
					jc = jc.replace("Lien_JC",data_jc[2])
					jc = jc.replace("Gagnant_2",data_jc[0])
					if data_jc[1] == 'M':
						jc = jc.replace("Gagnant_1","Le gagnant")
					else:
						jc = jc.replace("Gagnant_1","La gagnante")
					contenu += jc

			contenu += bloc.case_actu_sortie

	elif nom == courrier:

		questions = []
		reponses = []
		if article.repereExiste(bloc.question):
			questions = recup_liste(article.txt,bloc.question,article.titre_web,article.categorie)
		if article.repereExiste(bloc.reponse):
			reponses = recup_liste(article.txt,bloc.reponse,article.titre_web,article.categorie)

		contenu = bloc.case_courrier_entree
		for i in range(0,len(questions)):
		    contenu += bloc.texte_qr_1+questions[i]
		    if i <= (len(reponses)-1):
		        contenu += bloc.texte_qr_2+reponses[i]+bloc.texte_qr_3
		    contenu += bloc.texte_qr_4
		#
		contenu += bloc.case_courrier_sortie

	elif nom == quizz:
		if article.repereExiste(repere_titre_web) and article.repereExiste(bloc.repereTexte):
			status = extrairecurly(article.txt, bloc.repereTexte)
			status = oui_non_to_bool(status)
			if status:
			    data = extrairecurly(article.txt,repere_titre_web)
			    data = enlever_espaces(data)
			    if data != '':
			        url = "https://lundicarotte.fr/quizz/"+data
			        contenu = bloc.code
			        contenu = contenu.replace("url_quizz",url)

	elif nom == pied:
		contenu = bloc.code

	return(contenu)

#################################################
# FONCTIONS SECONDAIRES
#################################################

def creerListeReperesTexte(listeblocs):
	"""renvoie une liste des balises de type "REPERE{}" qu'il est possible d'utiliser.
	Cela inclut les attributs repereTexte, repereJc, question, reponse."""
	listeReperesBlocs = ['repereTexte', 'repereJc', 'question', 'reponse']
	listeRBAttr = []
	for i in listeblocs:
		bloc = creerBloc(i)
		temp = [getattr(bloc,j) for j in listeReperesBlocs if j in dir(bloc)]
		listeRBAttr+=temp
	listeGetAttrRep = [getattr(rep,a) for a in dir(rep) if not a.startswith('__') and not callable(getattr(rep,a))]
	r = listeRBAttr+listeGetAttrRep
	return(r)

def creerListeReperesSandwich(listeblocs):
	"""renvoie la valeur des attributs repereTexte1 et repereTexte2
	des blocs définis dans le module styleBlocs"""
	listeAttrSand = ['repereTexte1', 'repereTexte2']
	listeGetAttrSand = []
	for i in listeblocs:
		temp = [getattr(creerBloc(i),j) for j in listeAttrSand if j in dir(creerBloc(i))]
		for k in temp:
			if k not in listeGetAttrSand:
				listeGetAttrSand.append(k)
	return(listeGetAttrSand)


def creerFichierTextePropre(donnees, listeblocs):
	""" On génèrer une version propre du fichier texte. On avertit s'il manque des balises importantes. Une balise est nécessairement seule sur sa ligne.  """

	listeReperesTextes = creerListeReperesTexte(listeblocs)
	# s'assurer que les balises sont bien formées
	liste_data = donnees.split('\n')
	for i in range(len(liste_data)):
		line = liste_data[i]
		newLine = cleanBalise(line, listeReperesTextes)
		liste_data[i] = newLine

	# on enlève les commentaires
	for i in liste_data:
		if len(i)>=2 and i[0:2] == '//':
			liste_data.remove(i)

	# on vérifie que les repères intro, développement, conclusion et fin sont présents et dans le bon ordre
	listeRepSand = creerListeReperesSandwich(listeblocs)

	# is there only one occurence of those in the data ?
	# count number of occurences
	occurList = [sum(i in k for k in liste_data) for i in listeRepSand]
	# product of those list terms should be one
	onlyOneOccurence = bool(functools.reduce(lambda x,y: x*y, occurList) == 1)

	# are they in the right order ?
	indexList = [k for k in range(len(liste_data)) for i in listeRepSand if i in liste_data[k]]
	# comparison of all pairs of consecutive items
	consItemsComp = [i<j for i,j in zip(indexList,indexList[1:])]
	# all terms of this list should be True (i.e) their product is one
	inTheRightOrder = bool(functools.reduce(lambda x,y: x*y, consItemsComp) == 1)

	if(onlyOneOccurence and inTheRightOrder):
		return('\n'.join(liste_data))
	else:
		print("Erreur : au moins l'un des repères",listeRepSand," est absent du fichier, ou ces repères ne sont pas dans le bon ordre.\n")
		return('')

def cleanBalise(line, listeReperesTextes):
	"""renvoie la première balise rencontrée sur une ligne, mise en forme"""

	if line: #if line not empty
		for repere in listeReperesTextes:
			if repere in line:
				indRep = line.find(repere)
				start = indRep + len(repere)
				ind_open = line.find('{',start)
				# if found { : update start
				if ind_open != -1:
					start = ind_open+1
				offset = 0
				subtxt = line[start:]
				offset = subtxt.find('}')
				if offset == -1:
					offset = len(subtxt)
				stop = start + offset
				x = line[start:stop]
				x = enlever_espaces_inutiles(x)
				balise = repere+'{'+x+'}'+'\n'
				return(balise)
		# si après la boucle sur les repères textes on a rien trouvé
		return(line)
	else: # if line was empty
		return('')

def clean_data(data):
	""" On utilise cette fonction pour nettoyer le texte entre le repère d'introduction et le repère de fin de texte. Lorsqu'une ligne de texte débute par une balise, on supprime le reste de la ligne ; on supprime les commentaires. """

	liste = data.split('\n')
	i = 0
	while i < len(liste):
		# si la ligne commence par //, on la supprime
		if len(liste[i])>=2:
			if liste[i][0:2] == '//':
				liste.pop(i)


		# on gère la mise en forme des balises de sous-titre, citation, image supplémentaire.
		for repere in [rep.citation,rep.sous_titre,rep.ajout_image]:
			if repere in liste[i]:
				# on ajoute un '\n' à la fin de la case pour que la fonction extrairecurly s'arrête dans tous les cas
				temp = liste[i]+'\n'
				[balise,data] = extraire_balise(temp,repere)
				data = enlever_espaces_inutiles(data)
				liste[i] = repere+'{'+data+'}'
		#
		i += 1

	texte = '\n'.join(liste)
	return(texte)

def enlever_premiers_espaces(text):
	"""enlève les espaces avant du texte, et renvoie '' si text est uniquement constitué d'espaces"""
	if text != '':
		while(text[0] == ' '):
			text = text[1:]
	return(text)

def enlever_espaces_inutiles(text):
	"""enlève les espaces au début et à la fin d'une chaîne de caractères"""
	while(text != '' and text[0] == ' '):
		text = text[1:]
	while(text != '' and text[-1] == ' '):
		text = text[:-1]
	return(text)

def oui_non_to_bool(txt):
	""" Reçoit du texte en entrée, et renvoie True si ce texte est 'oui', False sinon."""
	txt = enlever_espaces_inutiles(txt).lower()
	return(bool(txt == "oui"))

def enleverPrePostBackspace(text):
	"""enlève les retours à la ligne au début et à la fin d'une chaîne de caractères"""
	while(text != '' and text[0] == '\n'):
		text = text[1:]
	while(text != '' and text[-1] == '\n'):
		text = text[:-1]
	return(text)


def recup_data_jeudicarotte(txt,rep):
	data = ['','','']
	x = extrairecurly(txt,rep).split(",")
	if (len(x) == 3):
		for i in range(len(x)):
			data[i] = enlever_espaces_inutiles(x[i])
	return(data)

def recup_data_retrouvailles(txt):
	data = ''
	if txt.find(rep.rtv):
		data = extrairecurly(txt,rep.rtv)
		data_rtv = data.split(",")
		if len(data_rtv) == 0:
			return('')
		else:
			return(data_rtv)
	return(data)

def recup_liste(txt,repere,titre_web,categorie):
	liste = []
	i = 0
	n = compter_apparition(txt,repere)
	for j in range(n):
		indice_next = txt.find(repere,i)
		[chaine,data] = extraire_balise(txt[i:],repere)
		i = indice_next + len(chaine)
		if (data != ""):
			# on formatte le texte
			data = mise_en_forme(data,titre_web,categorie)
			# on ajoute une actu à la liste
			liste.append(data)
	return(liste)

def verifreperetxt(txt,repere):
	if (txt.find(repere) == -1):
		# si ça existe pas, message d'erreur
		print("!! il manque le repère ",repere)

def generer_url(titre_web,categorie):
	if (categorie == "web" or categorie == "mail"):
		url = "https://lundicarotte.fr/"+titre_web
	if (categorie == "artsup"):
		url = "https://lundicarotte.fr/articles/"+titre_web
	return(url)

def valeurpardefaut(txt,txt2):
	if txt == '':
		txt = txt2
	return(txt)

def recup_qr(contenu):
	[chaine1,txt_q] = extraire_balise(contenu,rep.question)
	contenu = contenu.replace(chaine1," ")
	[chaine2,txt_r] = extraire_balise(contenu,rep.reponse)
	contenu = contenu.replace(chaine2," ")
	return(contenu,txt_q,txt_r)

def mise_en_forme(txt,titre_web,categorie):
	"""on enlève le texte contenu dans les balises CODE, on génère les retours à la ligne, les liens hyperref et les listes d'un texte, puis on réajoute le texte contenu dans les balises CODE """

	# on enlève le texte dans les balises CODE pour qu'il ne soit pas modifié
	n = compter_apparition(txt,repTexteCode)
	data_code = []
	reperes_code = []
	for i in range(n):
		[chaine,data] = extraire_code(txt)
		data_code.append(data)
		reperes_code.append('*** repère code '+str(i)+' ***')
		txt = txt.replace(chaine,reperes_code[i])

	# on enlève les espaces avant et après le texte
	txt = enleverPrePostBackspace(txt)
	# un retour à la ligne dans le texte correspond à un retour à la ligne dans le html
	txt = txt.replace("\n","<br/>\n")

	# on remplace aussi les "CO2" par "CO<sub>2</sub>"
	txt = txt.replace("CO2","CO<sub>2</sub>")
	#
	# on s'occupe d'une partie des espaces insécables
	txt = inserer_nbsp_num(txt)
	txt = inserer_nbsp_unit(txt)
	txt = txt.replace(" ?","&nbsp;?")
	txt = txt.replace(" !","&nbsp;!")
	txt = txt.replace(" :","&nbsp;:")
	# on génère les listes
	txt = txt.replace(repTexteListe,htmlListe)
	# on génère les images supplémentaires
	txt = ajouter_image_sup(txt,categorie)
	# on génère les sous-titres éventuels
	txt = ajouter_sous_titre(txt)
	#
	txt = ajouter_citation(txt,titre_web,categorie)
	#
	txt = creer_href(txt,categorie)


	# pour faciliter la lecture du fichier html :
	txt = txt.replace("<br/>\n\n<br/>","<br/>\n<br/>")
	txt = txt.replace("<br/>\n\n<br/>","<br/>\n<br/>")

	# après avoir fait toutes ces modifications, on réinsère dans le texte le contenu des balises CODE
	for i in range(n):
		bloc = tag.texte_sortie+data_code[i]+tag.texte_entree
		txt = txt.replace(reperes_code[i],bloc)

	return(txt)

def inserer_nbsp_num(txt):
	p = txt.split(' ')
	if len(p)>1:
		for i in range(1,len(p)):
			if (len(p[i])==3 and is_number(p[i])):
				if is_number(p[i-1]):
					old = p[i-1]+' '+p[i]
					new = p[i-1]+'&nbsp;'+p[i]
					txt = txt.replace(old,new)
	return(txt)

def inserer_nbsp_unit(txt):
	symbols = ['€', '%' ,'g', 'm', 'kg', '$', 'ans', 'km', 'millions']
	marks = ['', '.', ',']
	list = []
	for j in marks:
		for i in symbols:
			list.append(i+j)
	p = txt.split(' ')
	if len(p)>1:
		for i in range(0,len(p)-1):
			if is_number(p[i]):
				if p[i+1] in list:
					old = p[i]+' '+p[i+1]
					new = p[i]+'&nbsp;'+p[i+1]
					txt = txt.replace(old,new)
	return(txt)

def is_number(s):
	p = list(s)
	for i in p:
		if (i != '0' and i != '1' and i != '2' and i != '3' and i != '4' and i != '5' and i != '6' and i != '7' and i != '8' and i != '9') :
			return False
	return True


def ajouter_image_sup(txt,categorie):
	""" On remplace les balises AJOUT-IMAGE{blabla} par le bloc html correspondant """

	n = compter_apparition(txt,rep.ajout_image)
	if n>0:
		bloc_vide = tag.image_sup
		for i in range(n):
			[chaine,data] = extraire_balise(txt,rep.ajout_image)
			data = enlever_espaces_inutiles(data)
			if not data: # if data empty
				print("une balise AJOUT-IMAGE est vide")
			else:
				data_i = data.split(",")
				bloc = bloc_vide
				bloc = bloc.replace(rep.ajout_image,data_i[0])
				# si l'on précise la largeur :
				if len(data_i)>=2:
					width = data_i[1]
					width = width.replace(' ','')
					if (width != ''):
						bloc = bloc.replace('width:300px','width:'+width+'px')
						bloc = bloc.replace('width="300"','width="'+width+'"')
				if len(data_i)>=3:
					if (data_i[2] != ''):
						legende = ','.join(data_i[2:])
						bloc_legende = tag.legende_entree+legende+tag.legende_sortie
						bloc = bloc + bloc_legende

				# on insère les balises de sortie / entrée dans le bloc de texte
				bloc = tag.texte_sortie+bloc+tag.texte_entree
				txt = txt.replace(chaine,bloc)
	return(txt)


def ajouter_sous_titre(txt):
	n = compter_apparition(txt,rep.sous_titre)
	if n>0:
		for i in range(n):
			line = extraire_ligne(txt,rep.sous_titre)
			if line != '':
				[chaine,data] = extraire_balise(line,rep.sous_titre)
				if data == '':
					print("Une balise de sous-titre est vide")
					data = '~'
				# on enlève les retours à la ligne avant et après la ligne de sous-titre
				if txt.find('\n'+line) != -1:
					line = '\n' + line
				pre = '\n<br/>'
				while txt.find(pre+line) != -1:
					line = pre + line
				post = '<br/>\n'
				while txt.find(line+post) != -1:
					line = line + post
				# on remplace la ligne entière par le bloc de citation.
				bloc = tag.texte_sortie+tag.sous_titre_entree+data+tag.sous_titre_sortie+tag.texte_entree
				txt = txt.replace(line,bloc)
	return(txt)

def ajouter_citation(txt,titre_web,categorie):
	n = compter_apparition(txt,rep.citation)
	if n > 0:
		for i in range(n):
			bloc = ''
			[chaine,data] = extraire_balise(txt,rep.citation)
			if not data: # if data empty
				print("Une balise citation est vide")
			else:
				bloc = tag.texte_sortie+tag.citation+tag.texte_entree
				bloc = bloc.replace(rep.citation,data)
				bloc = bloc.replace("CIT_URL",data.replace("<sub>", "").replace("</sub>", ""))
				bloc = bloc.replace("URL",generer_url(titre_web,categorie))
			txt = txt.replace(chaine,bloc)
	return(txt)

def extraire_code(txt):
	""" Reçoit en entrée une chaîne de caractère contenant CODE{data}, renvoie CODE{data} et data """
	n = compter_apparition(txt,repTexteCode+'{')
	if n>0:
		start = txt.find(repTexteCode+'{')+len(repTexteCode+'{')
		temp = indice_crochet_fermeture(txt[start:])
		if temp != -1:
			stop = start + temp
			data = txt[start:stop]
			chaine = repTexteCode+'{'+data+'}'
		else:
			print("/!\\  erreur avec la balise ",repTexteCode)
			return('','')
	return(chaine,data)


def indice_crochet_fermeture(txt):
	""" renvoie -1 si il n'y a pas de '}' dans txt, 0 si '}' est le premier caractère de txt """
	n_close = compter_apparition(txt,'}')
	if n_close == 0:
		return(-1)
	else:
		count = 0
		for i in range(len(txt)):
			if txt[i] == '{':
				count += 1
			if txt[i] == '}':
				count -= 1
			if count == -1:
				return(i)


def creer_href(txt,categorie):
	""" la fonction creer_href prend en entrée un texte et renvoie en sortie le même texte où les expressions de type [phrase https://lundicarotte.fr] sont remplacées par le code html d'un lien hypertexte, si les crochets contiennent au moins deux chaines de caractères séparées par un espace et si la dernière chaine de caractères débute par 'http' """
	# recup la liste des []
	listeBB = creerListeBoxBrackets(txt)
	# faire une liste des [..]
	coupleList = []
	for i in listeBB:
		seq = txt[i[0]:i[1]+1]
		html = makeOneHref(seq)
		coupleList.append((seq,html))
	for i in coupleList:
		txt = txt.replace(i[0],i[1])
	return(txt)

def makeOneHref(seq):
	""" on envoie '[texte https://www.google.com]' en entrée, et on récupère le code HTML du lien hypertexte en sortie"""
	code = ''
	seq = seq[1:-1]
	seq_list = seq.split()
	if (len(seq_list)>1):
		if (len(seq_list[-1])>3):
			if seq_list[-1][0:4] == 'http':
				http = seq_list[-1]
				expr = " ".join(seq_list[:-1])
				# formation de la balise
				str1 = '<a target="_blank" href="'
				str2 = '" style="text-decoration: none; color: #E36C0A;">'
				str3 = '</a>'
				# ajout éventuel du lien google analytics
				#if categorie == "mail":
				#	http = lien_google + http
				# on remplace la "pré-balise" par la balise
				code = str1 + http + str2 + expr + str3
	return(code)


def creer_json(titre_web,url_image,titre_page,description):
	json = """{
    "id": "json-id",
    "title": "json-title",
    "img": "json-img",
    "description": "json-description"
	}
	"""
	json = json.replace("json-id",titre_web)
	json = json.replace("json-title",titre_page)
	json = json.replace("json-img",url_image)
	json = json.replace("json-description",description)
	return(json)

#################################################
# FONCTIONS DE MANIPULATION DE TEXTE
#################################################

def compter_apparition(txt,repere):
	i = 0
	ind = txt.find(repere)
	while(ind != -1):
			i = i+1
			ind = txt.find(repere,ind+1)
	return(i)

def extrairesandwich(txt,rep1,rep2):
	# renvoie le texte présent entre deux repères
	ind1 = txt.find(rep1)
	ind2 = txt.find(rep2)
	data = txt[ind1+len(rep1):ind2]
	return(data)

def extrairecurly(txt,repere):
	""" La fonction cherche repere dans le texte, renvoie data si repere{data} existe.
	S'il manque le crochet d'ouverture, l'indice de début est l'indice consécutif à repere.
	S'il manque le crochet de fermeture, l'indice de fin est le premier retour à la ligne rencontré. S'il n'est pas trouvé non plus, extrairecurly ne renvoie rien.  """
	# le nom c'est parce que curly brackets {}
	ind = txt.find(repere)
	start = ind + len(repere)
	if txt[start:start+1] == '{':
		start = start+1
	offset = 0
	subtxt = txt[start:]
	for i in range(len(subtxt)):
		if subtxt[i] == '}' or subtxt[i] == '\n':
			offset = i
			break
	stop = start + offset
	data = txt[start:stop]
	return(data)

def enlever_espaces(txt):
	txt = txt.replace(' ','')
	return(txt)

def subcurly(html,repere):
	# texte utilisant le repère #LAMBDA{}
	# on veut extraire le texte entre {} et l'insérer
	# dans le template approprié
	nb_repere = compter_apparition(html,repere)
	if nb_repere > 0:
		name = "templates/"+repere+".html"
		html_template = lc_lire(name)
		for i in range(nb_repere):
			[chaine,txt] = extraire_balise(html,repere)
			html_bloc = html_template
			html_bloc = html_bloc.replace(repere,txt)
			html = html.replace(chaine,html_bloc)
	return(html)

def extraire_balise(txt,repere):
	""" on suppose qu'il n'y a pas de {} contenus dans la balise. Renvoie la balise et les données contenues dans la première balise trouvée dans txt. """
	ind = txt.find(repere)
	if (ind == -1):
		print("repère ",repere," non trouvé")
		return('','')
	else:
		start = ind
		data = extrairecurly(txt,repere)
		ind2 = txt.find(data,start)
		stop = ind2 + len(data)
		# y a-t-il un } après data ?
		if txt[stop:stop+1] == '}':
			stop = stop+1
		chaine = txt[start:stop]
		return(chaine,data)

def extraire_ligne(txt,repere):
	ind = txt.find(repere)
	if (ind == -1):
		print('repère ',repere,' non trouvé')
		return('')
	else:
		ind_n = txt.find('\n',ind)
		ind_br = txt.find('<br/>',ind)
		if (ind_n == -1 and ind_br == -1):
			return('')
		if (ind_n == -1):
			return(txt[ind:ind_br])
		if (ind_br == -1):
			return(txt[ind:ind_n])
		if (ind_n < ind_br):
			return(txt[ind:ind_n])
		else:
			return(txt[ind:ind_br])


#################################################
# LECTURE ET ÉCRITURE
#################################################


def lc_lire_avecparametres(nom,mode,encodage):
	with open(nom,mode,encoding = encodage) as f:
		texte = f.read()
	return(texte)

def lc_lire(nom):
	return(lc_lire_avecparametres(nom,"r",encodage))


def ecrire_fichier(nom,data):
	with open(nom,'w',encoding='utf-8') as f:
		f.write(data)
		print("~~~~~~Fichier créé : "+nom)

#################################################
# DÉBUGAGE
#################################################

def printDict(dict):
	max = 0
	for i in dict:
		m = len(i)
		if m>max:
			max = m
	for i in dict:
		print(i,(max+2-len(i))*' ',dict[i])

def coucou():
	print("coucou")

def debug(txt):
	debug = open("debug.html", "w")
	debug.write(txt)
	debug.close()


# def fonction(parametre):
