# -*-coding:utf-8 -*
""" module contenant les fonctions nécessaires à la génération du template html"""

from .variables import *
from .styles import *
import subprocess




#################################################
# CONTRÔLE DU CONTENU DU DOCUMENT TEXTE
#################################################


def bloc2rep(listeblocs):
	""" On crée la liste des repères qui doivent être présents, étant donné la liste de blocs que l'on a spécifié """


	listerep = []
	listerep.append(rep.titre_web)

	for i in listeblocs:

		if i == titre:
			listerep.append(rep.titre)

		if i == date:
			listerep.append(rep.date)

		if i == image:
			listerep.append(rep.url_image)

		if i == auteurs:
			listerep.append(rep.auteurs)

		if i == actu:
			listerep.extend((rep.actu,rep.jc))

		if i == partage:
			listerep.append(rep.partage_description)

		if i == courrier:
			listerep.append(rep.question)
			listerep.append(rep.reponse)

	return(listerep)



#################################################
# FONCTIONS SECONDAIRES
#################################################

def generer_fichier_txt_propre(donnees,listeblocs):
	""" On génèrer une version propre du fichier texte. On avertit s'il manque des balises importantes. Une balise est nécessairement seule sur sa ligne. """

	listerep = bloc2rep(listeblocs)


	# on convertit le texte en liste et on trouve les repères
	liste_data = donnees.split('\n')
	liste_balises = ''
	for k in liste_data:
		if (k != ''):
			for repere in listerep:
				if repere in k:
					ind = k.find(repere)
					start = ind + len(repere)
					ind_open = k.find('{',start)
					if ind_open != -1:
						start = ind_open+1
					offset = 0
					subtxt = k[start:]
					offset = subtxt.find('}')
					if offset == -1:
						offset = len(subtxt)
					stop = start + offset
					x = k[start:stop]
					x = enlever_espaces_inutiles(x)
					balise = repere+'{'+x+'}'+'\n'
					liste_balises += balise
	txt = liste_balises

    # on check que les repères délimitant l'article sont dans le bon ordre
	problem = False
	quartette = [rep.intro,rep.dev,rep.outro,rep.fin]
	for i in quartette:
		if not any(i in k for k in liste_data):
			print("il manque le repère ",i)
			problem = True
	for i in range(len(quartette)-1):
		if donnees.find(quartette[i+1]) < donnees.find(quartette[i]):
			problem = True

	if problem:
		data = '\n'+rep.intro+'\n'+rep.dev+'\n'+rep.outro+'\n'+rep.fin
		print("Erreur : au moins l'un des repères",rep.intro,", ",rep.dev,", ",rep.outro," et ",rep.fin," est absent du fichier, ou ces repères ne sont pas dans le bon ordre.\n")
	else:
		# on extrait le texte entre intro et fin et on l'ajoute à txt
		start = donnees.find(rep.intro)
		t = donnees.find(rep.fin)
		stop = t + len(rep.fin)
		data = donnees[start:stop]
		# on s'assure que sur une ligne avec une balise de sous-titre ou de citation, il n'y a rien d'autre que ça
        # on enlève les commentaires
		data = clean_data(data)

	txt += '\n'+data
	return(txt)



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

def enlever_premiers_espaces(str):
	"""enlève les espaces avant du texte, et renvoie '' si str est uniquement constitué d'espaces"""
	if str != '':
		while(str[0] == ' '):
			str = str[1:]
	return(str)

def enlever_espaces_inutiles(str):
	"""enlève les espaces en trop au début et à la fin d'une chaîne de caractères"""
	while(str != '' and str[0] == ' '):
		str = str[1:]
	while(str != '' and str[-1] == ' '):
		str = str[:-1]
	return(str)

def recup_data_jeudicarotte(txt):
	data = ['','','']
	x = extrairecurly(txt,rep.jc).split(",")
	if (len(x) >= 3):
		data = x
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
	n = compter_apparition(txt,rep.code)
	data_code = []
	reperes_code = []
	for i in range(n):
		[chaine,data] = extraire_code(txt)
		data_code.append(data)
		reperes_code.append('*** repère code '+str(i)+' ***')
		txt = txt.replace(chaine,reperes_code[i])


	# un retour à la ligne dans le texte correspond à un retour à la ligne dans le html
	txt = txt.replace("\n","\n<br/>\n")

	# on remplace aussi les "CO2" par "CO<sub>2</sub>"
	txt = txt.replace("CO2","CO<sub>2</sub>")
	#
	# on s'occupe d'une partie des espaces insécables
	txt = inserer_nbsp_num(txt)
	txt = inserer_nbsp_unit(txt)
	txt = txt.replace(" ?","&nbsp;?")
	txt = txt.replace(" !","&nbsp;!")
	txt = txt.replace(" :","&nbsp;:")
	#
	liste = lc_lire(template.liste)
	txt = txt.replace("LISTE ",liste)
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
				# on enlève un retour à la ligne après la balise de sous-titre
				for i in range(1):
					if txt.find(line+'\n')!= -1:
						line += '\n'
				# on remplace la ligne entière par le bloc de citation.
				bloc = tag.texte_sortie+tag.sous_titre_entree+data+tag.sous_titre_sortie+tag.texte_entree
				txt = txt.replace(line,bloc)
	return(txt)

def ajouter_citation(txt,titre_web,categorie):
	n = compter_apparition(txt,rep.citation)
	if n > 0:
		for i in range(n):
			[chaine,data] = extraire_balise(txt,rep.citation)
			if data != '':
				bloc = tag.texte_sortie+tag.citation+tag.texte_entree
				bloc = bloc.replace(rep.citation,data)
				bloc = bloc.replace("URL",generer_url(titre_web,categorie))
			else:
				print("Une balise citation est vide")
				bloc = ''
			txt = txt.replace(chaine,bloc)
	return(txt)

def extraire_code(txt):
	""" Reçoit en entrée une chaîne de caractère contenant CODE{data}, renvoie CODE{data} et data """
	n = compter_apparition(txt,rep.code+'{')
	if n>0:
		start = txt.find(rep.code+'{')+len(rep.code+'{')
		temp = indice_crochet_fermeture(txt[start:])
		if temp != -1:
			stop = start + temp
			data = txt[start:stop]
			chaine = rep.code+'{'+data+'}'
		else:
			print("/!\\  erreur avec la balise ",rep.code)
			return('','')
	return(chaine,data)


def indice_crochet_fermeture(txt):
	""" renvoie -1 si il n'y a pas de '}' dans txt, 0 si '}' est le premier caractère de txt """
	n_close = compter_apparition(txt,'}')
	if n_close == 0:
		return(-1)
	count = 0
	for i in range(len(txt)):
		if txt[i] == '{':
			count += 1
		if txt[i] == '}':
			count -= 1
		if count == -1:
			return(i)



def creer_href(txt,categorie):
	""" la fonction creer_href prend en entrée un texte et renvoie en sortie le même texte où les expressions de type [phrase https://lundicarotte.fr] sont remplacées par le code html d'un lien hypertexte, si les crochets contiennent au moins deux chaines de caractères séparées par un espace et si la dernière chaine de caractères débute par http """
	nb_crochet = compter_apparition(txt,"[")
	if nb_crochet > 0:
		# on initialise j
		j = 0
		#
		for i in range(nb_crochet):
			ind1 = txt.find("[",j)
			ind_fin = txt.find("\n",ind1)
			# on gère le cas où le texte ne contient pas le retour à la ligne (par exemple s'il s'agit du texte de l'actu JeudiCarotte)
			if ind_fin == -1:
				ind_fin = len(txt)
			found_close = False
			found_open = False
			close_ok = False
			# on cherche un crochet de fermeture jusqu'à la fin de la ligne
			for h in range(ind1+1,ind_fin):
				if txt[h] == ']':
					found_close = True
					if not found_open:
						ind2 = h
						close_ok = True
						break
				if txt[h] == '[':
					found_open = True
					# si on rencontre un crochet d'ouverture sans avoir rencontré de crochet de fermeture
					if not found_close:
						print("Il manque un crochet fermant ] dans ce texte : **", txt[ind1:h+1],'**')
						j = ind1+1
						break
			if not close_ok and not found_open:
				# si on revient à la ligne avant de rencontrer le crochet de fermeture ], et qu'on a pas déjà averti, alors on averti qu'il manque un crochet de fermeture
				print("Il manque un crochet dans ce paragraphe : **",txt[ind1:ind_fin],'**')
				j = ind1+1

			if close_ok:
				seq = txt[ind1+1:ind2]
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
							if categorie == "mail":
								http = lien_google + http
								# attention, ça n'inclut pas les liens contenus dans les templates...
							# on remplace la "pré-balise" par la balise
							balise = str1 + http + str2 + expr + str3
							# on renvoie la pré-balise par la balise
							txt = txt.replace("["+seq+"]",balise)
			j = ind2+1
	return(txt)

def creer_json(titre_web,url_image,titre_page,description):
	json = lc_lire(template.json)
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
	with open(nom,'w',encoding = encodage) as f:
		f.write(data)
		print("~~~~~~Fichier créé : "+nom)

#################################################
# DÉBUGAGE
#################################################

def coucou():
	print("coucou")

def debug(txt):
	debug = open("debug.html", "w")
	debug.write(txt)
	debug.close()


# def fonction(parametre):
