# -*-coding:utf-8 -*
""" module contenant les fonctions nécessaires à la génération du template html"""

from lc_var import *
import subprocess


def doctotxt(nftclavier):
	liste = nftclavier.split(".")
	type_doc = liste[-1]
	nom = '.'.join(liste[:-1])
	if (type_doc == "txt"):
		return(nom,nftclavier)
	# si le document est de type doc ou docx ou odt
	elif (type_doc == "doc" or "docx" or "odt"):
		subprocess.run(["soffice", "--headless", "--convert-to", "txt:Text", nftclavier])
		return(nom,nom+".txt")
	else:
		print("nom entré invalide : entrez un nom en .txt, .doc, .docx ou .odt")
		# mettre fin au programme


def fairenomtxt(entree):
	liste = entree.split(".")
	type_doc = liste[-1]
	nom = '.'.join(liste[:-1])
	if (type_doc == "txt"):
		return(entree)
	# si le document est de type doc ou docx ou odt
	elif (type_doc == "doc" or "docx" or "odt"):
		nom = nom+".txt"
		return(nom)
	else:
		print("nom entré invalide : entrez un nom en .txt, .doc, .docx ou .odt")
		# mettre fin au programme

def ajouter_html(html,txt,listeblocs,type_lc,nft):
	# la fonction ajouter_html prend du html et renvoie du html
	# 
	# On commence par vérifier si les repères nécessaires sont là
	# et on les ajoute s'ils n'y sont pas
	txt = verifier_reperes(txt,listeblocs,nft)
	#
	# type_lc est soit "hebdo" soit "artsup"
	#
	# dans cette fonction, on ajoute tous les morceaux de codes 
	# spécifiés dans la liste

	if logo in listeblocs:
		html = ajouter_logo(html)
	if titre in listeblocs:
		html = ajouter_titre(html,txt)
	if date in listeblocs:
		html = ajouter_date(html,txt)
	if intro in listeblocs:
		html = ajouter_intro(html,txt)
	if image in listeblocs:
		html = ajouter_image(html,txt)
	if dev in listeblocs:
		html = ajouter_dev(html,txt,type_lc)
	if outro in listeblocs:
		html = ajouter_outro(html,txt)
	if auteurs in listeblocs:
		html = ajouter_auteurs(html,txt)
	if partage in listeblocs:
		html = ajouter_partage(html,txt,type_lc)
	if quizz in listeblocs:
		html = ajouter_quizz(html,txt)
	if don in listeblocs:
		html = ajouter_don(html)
	if actu in listeblocs:
		html = ajouter_actu(html,txt)
	if courrier in listeblocs:
		html = ajouter_courrier(html,txt)
	if pied in listeblocs:
		html = ajouter_pied(html)

	html = ajouter_image_sup(html)

	return(html,txt)

# verifier_reperes

def verifier_reperes(txt,listeblocs,nft):
	txt_original = txt
	absences = False
	ajouts = ""

	# on vérifie le plus important : titre-web
	if (txt.find(rep_titre_web) == -1):
		ajouts = rep_titre_web+"{"+nft+"}\n"
		absences = True

	listerep = [] # va contenir la liste des repères dont on vérifie la présence
	for i in listeblocs:
		listerep = bloc2rep(listerep,i) # listes des repères indépendants qui doivent être présents
	# on vérifie pour les repères indépendants
	for i in listerep:
		if (txt.find(i) == -1):
			ajouts = ajouts+i+"{}\n"
			absences = True

	# maintenant on regarde pour les repères qui doivent aller deux par deux
	if intro in listeblocs:
		if (txt.find(repintro) == -1 and txt.find(repdev) == -1):
			absences = True
			txt = repintro+repdev+txt
	if dev in listeblocs:
		if (txt.find(repdev) == -1 and txt.find(repoutro) == -1):
			absences = True
			txt = repdev+txt+repoutro
	if outro in listeblocs:
		if (txt.find(repoutro) == -1 and txt.find(repfin) == -1):
			absences = True
			txt = txt+repoutro+repfin

	# et finalement, s'il a manqué qqch...
	if (absences):
		txt = ajouts+txt
		# on écrit le texte original dans fichier_original
		with open(fichier_original,'w') as f:
			f.write(txt_original)
		# on écrit le texte amendé des repères manquants sous le nom initial
		with open(nft+".txt",'w') as f: 
			f.write(txt)
	return(txt)


def bloc2rep(listerep,i):

	if i == titre:
		listerep.append(rep_titre)

	if i == date:
		listerep.append(rep_date)

	if i == image:
		listerep.append(rep_url_image)

	if i == auteurs:
		listerep.append(rep_auteurs)

	if i == actu:
		listerep.extend((rep_actu,rep_url_jc,rep_gagnant_jc,rep_sexe_gagnant,rep_jc_option,rep_date_rtv,rep_rtv_option))

	if i == partage:
		listerep.append(rep_partage_description)

	if i == courrier:
		listerep.append(rep_question)
		listerep.append(rep_reponse)

	return(listerep)

# for i in [partage,quizz,don,pied] on n'a pas de repères à vérifier


### fonctions "ajouter_bloc"

def ajouter_logo(html):
	logo = lc_lire(template_logo)
	html = html.replace(reph_logo,logo)
	return(html)

def ajouter_titre(html,txt):
	verifreperetxt(txt,rep_titre)	# on vérifie que "TITRE-PAGE{" existe dans le fichier texte
	data = extrairecurly(txt,rep_titre)# on extrait ce qu'il y a dans les crochets
	data = valeurpardefaut(data,"Un titre original")
	html = html.replace(reph_titre,data)
	# si TITRE{} est vide, valeur par défaut
	return(html)

def ajouter_date(html,txt):
	verifreperetxt(txt,rep_date)	
	data = extrairecurly(txt,rep_date)
	data = valeurpardefaut(data,"Le 22 octobre 1921") # date de naissance de Georges Brassens
	html = html.replace(reph_date,data)
	return(html)

def ajouter_intro(html,txt):
	verifreperetxt(txt,repintro)
	verifreperetxt(txt,repdev)
	data = extrairesandwich(txt,repintro,repdev)
	data = ral_liste_href(data)
	html = html.replace(reph_intro,data)
	return(html)

def ajouter_image(html,txt):
	verifreperetxt(txt,rep_url_image)	
	data = extrairecurly(txt,rep_url_image)
	data = valeurpardefaut(data,"https://lundicarotte.fr/api/admin/media/img/Agriculture-biologique.svg.png")
	bloc = lc_lire(template_image)
	bloc = bloc.replace("VBA_Image",data)
	html = html.replace(reph_image,bloc)
	return(html)

def ajouter_dev(html,txt,type_lc):
	verifreperetxt(txt,rep_titre_web)
	verifreperetxt(txt,repdev)
	verifreperetxt(txt,repoutro)
	titre_web = extrairecurly(txt,rep_titre_web)
	url = gen_url(titre_web,type_lc)
	data = extrairesandwich(txt,repdev,repoutro)
	data = ral_liste_href(data) # on gère les retours à la ligne avant toute chose
	data = cita_sstitre(data,url)
	html = html.replace(reph_dev,data)
	return(html)

def ajouter_outro(html,txt):
	verifreperetxt(txt,repoutro)
	verifreperetxt(txt,repfin)
	data = extrairesandwich(txt,repoutro,repfin)
	data = ral_liste_href(data)
	html = html.replace(reph_outro,data)
	return(html)

def ajouter_auteurs(html,txt):
	verifreperetxt(txt,rep_auteurs)	
	data = extrairecurly(txt,rep_auteurs)
	data = valeurpardefaut(data,"L'éternel George Brassens")
	html = html.replace(reph_auteurs,data)
	return(html)

def ajouter_partage(html,txt,type_lc):
	verifreperetxt(txt,rep_titre_web)
	verifreperetxt(txt,rep_partage_description)
	data = extrairecurly(txt,rep_titre_web)
	url = gen_url(data,type_lc)
	# on prend l'url du fichier, qui est déterminée en haut
	bloc = lc_lire(template_partage)
	bloc = bloc.replace("VBA_url",url)
	html = html.replace(reph_partage,bloc)
	# ensuite on ajoute les infos dans la section <head> du html
	# on remplace le titre
	data = extrairecurly(txt,rep_titre)
	html = html.replace(reph_titre,data)
	# on remplace la description 
	data = extrairecurly(txt,rep_partage_description)
	html = html.replace(reph_partage_description,data)
	# on remplace le lien de l'image
	data = extrairecurly(txt,rep_url_image)
	html = html.replace(reph_partage_image,data)
	

	return(html)

def ajouter_quizz(html,txt):
	verifreperetxt(txt,rep_titre_web)
	data = extrairecurly(txt,rep_titre_web)
	url = "https://lundicarotte.fr/quizz/"+data
	bloc = lc_lire(template_quizz)
	bloc = bloc.replace("VBA_quizz",url)
	html = html.replace(reph_quizz,bloc)
	return(html)

def ajouter_don(html):
	bloc = lc_lire(template_don)
	html = html.replace(reph_don,bloc)
	return(html)

def ajouter_actu(html,txt):
	# on crée une liste avec les actus
	actus = [] # on crée une liste vide
	while txt.find(rep_actu) != -1:
		[txt,txt_actu] = recup_actu(txt) # ev. m.à.j. recup_actu
		if (txt_actu != ""):
			txt_actu = ral_liste_href(txt_actu)
			actus.append(txt_actu) # on ajoute une actu à la liste des actus
	verifreperetxt(txt,rep_date_rtv)
	verifreperetxt(txt,rep_url_jc)
	verifreperetxt(txt,rep_gagnant_jc)
	verifreperetxt(txt,rep_sexe_gagnant)
	verifreperetxt(txt,rep_jc_option)
	verifreperetxt(txt,rep_rtv_option)
	date_rtv = extrairecurly(txt,rep_date_rtv)
	date_rtv = valeurpardefaut(date_rtv,"mois prochain")
	url_jc = extrairecurly(txt,rep_url_jc)
	url_jc = valeurpardefaut(url_jc,"https://lundicarotte.fr")
	gagnant_jc = extrairecurly(txt,rep_gagnant_jc)
	gagnant_jc = valeurpardefaut(gagnant_jc,"Michael Phelps")
	sexe_gagnant = extrairecurly(txt,rep_sexe_gagnant)
	sexe_gagnant = valeurpardefaut(sexe_gagnant,"M")
	texte_jc_option = extrairecurly(txt,rep_jc_option)
	texte_rtv_option = extrairecurly(txt,rep_rtv_option)

	html_actu = lc_lire(template_actu)
	nb_actus = len(actus)
	# Actus temporaires
	if (nb_actus > 0): # si y a au moins une actu
		for i in range(0,nb_actus):
			html_actu_i = lc_lire(template_texte_actu)
			html_actu_i = html_actu_i.replace("<!--VBA_ActuTexte-->",actus[i])
			html_actu = html_actu.replace("<!--VBA_Actu--><!--VBA_Actu-->",html_actu_i+"<!--VBA_Actu--><!--VBA_Actu-->",1)
	# JeudiCarotte
	if (texte_jc_option != ""):
		texte_jc_option = ral_liste_href(texte_jc_option)
		html_jc = lc_lire(template_texte_actu)
		html_jc = html_jc.replace("<!--VBA_ActuTexte-->",texte_jc_option)
	else:
		html_jc = lc_lire(template_texte_jc)
		html_jc = html_jc.replace("VBA_LienJC",url_jc)
		html_jc = html_jc.replace("VBA_Gagnant2",gagnant_jc)
		if sexe_gagnant == "M":
			html_jc = html_jc.replace("VBA_Gagnant1","Le gagnant")
		if sexe_gagnant == "F":
			html_jc = html_jc.replace("VBA_Gagnant1","La gagnante")
	# à ce point-là, on a généré le html  du jeudicarotte
	html_actu = html_actu.replace("<!--VBA_ActuJC--><!--VBA_ActuJC-->",html_jc)
	# Retrouvailles
	if (texte_rtv_option != ""):
		texte_rtv_option = ral_liste_href(texte_rtv_option)
		retrouv = lc_lire(template_texte_actu)
		retrouv = retrouv.replace("<!--VBA_ActuTexte-->",texte_rtv_option)
	else:
		retrouv = lc_lire(template_texte_retrouvailles)
		retrouv = retrouv.replace("VBA_retrouvailles",date_rtv)
	html_actu = html_actu.replace("<!--VBA_TexteRetrouvailles--><!--VBA_TexteRetrouvailles-->",retrouv) 
	# on a terminé le html de l'actu
	html = html.replace(reph_actu,html_actu)
	return(html)

def ajouter_courrier(html,txt):
	# recup courrier
	questions = []
	reponses = [] # ces listes vides vont contenir le texte des questions et réponses
	while txt.find(rep_question) != -1:
		[txt,txt_q,txt_r] = recup_qr(txt)
		if (txt_q != ""): # une réponse est forcément associée à une question
			txt_q = ral_liste_href(txt_q)
			txt_r = ral_liste_href(txt_r)
			questions.append(txt_q)
			reponses.append(txt_r)

	html_courrier = lc_lire(template_courrier)
	nb_q = len(questions)
	for i in range(0,nb_q):
		html_qr = lc_lire(template_texte_qr)
		html_qr = html_qr.replace("VBA_question",questions[i])
		html_qr = html_qr.replace("VBA_reponse",reponses[i])
		html_courrier = html_courrier.replace("<!--VBA_QR--><!--VBA_QR-->",html_qr+"<!--VBA_QR--><!--VBA_QR-->",1)

	html = html.replace(reph_courrier,html_courrier)

	return(html)

def ajouter_pied(html):
	bloc = lc_lire(template_pied)
	html = html.replace(reph_pied,bloc)

	return(html)

def ajouter_image_sup(html):
	nb_image_supp = compter_apparition(html,rep_image_supp)
	if nb_image_supp > 0:
		html_imgsup = lc_lire(template_image_supp)
		for i in range(nb_image_supp):
			[chaine,url] = extraire_txt(html,rep_image_supp)
			bloc = html_imgsup
			bloc = bloc.replace("VBA_Image",url)
			html = html.replace(chaine,bloc)
	return(html)	


### nouvelles fonctions

def verifreperetxt(txt,repere):
	if (txt.find(repere) == -1):
		print("!! il manque le repère ",repere) # si ça existe pas, message d'erreur
		# faire que le programme s'arrête

def extrairecurly(txt,repere): 
# cette fonction assume l'existence du repère dans le texte
# le nom c'est parce que curly brackets {}
	ind1 = txt.find(repere)
	ind2 = txt.find("}",ind1)
	data = txt[ind1+len(repere+"{"):ind2]
	return(data)

def extrairesandwich(txt,rep1,rep2):
	ind1 = txt.find(rep1)
	ind2 = txt.find(rep2)
	data = txt[ind1+len(rep1):ind2]
	return(data)

def gen_url(titre_web,type_lc):
	if (type_lc == "hebdo"):
		url = "https://lundicarotte.fr/"+titre_web
	if (type_lc == "artsup"):
		url = "https://lundicarotte.fr/articles/"+titre_web
	return(url)

def valeurpardefaut(txt,txt2):
	if txt == "":
		txt = txt2
	return(txt)


#### ANCIENNES FONCTIONS ENCORE UTILISÉES





def recup_actu(contenu):
	[chaine,txt] = extraire_txt(contenu,"ACTU")
	contenu = contenu.replace(chaine," ")
	return(contenu,txt)


# cette fonction cherche repere et renvoie repere{data} et data
def extraire_txt(txt,repere):
	test = txt.find(repere)
	if (test == -1):
		print("repère ",repere," non trouvé")
		return("","")
	else:
		data = extrairecurly(txt,repere)
		chaine = repere+"{"+data+"}"
		return(chaine,data)

def recup_qr(contenu):
	[chaine1,txt_q] = extraire_txt(contenu,rep_question)
	contenu = contenu.replace(chaine1," ")
	[chaine2,txt_r] = extraire_txt(contenu,rep_reponse)	
	contenu = contenu.replace(chaine2," ")
	return(contenu,txt_q,txt_r)



def lc_lire_avecparametres(nom,mode,encodage):
	with open(nom,mode,encoding = encodage) as f:
		texte = f.read()
	return(texte)

def lc_lire(nom):
	return(lc_lire_avecparametres(nom,"r",encodage))


def ecrire_html_final(nom,html):
	with open(nom,'w',encoding = encodage) as f:
		f.write(html)
		print("Le fichier "+nom+" a été créé.")

# débugage

def coucou():
	print("coucou")

def debug(txt):
	debug = open("debug.html", "w")
	debug.write(txt)
	debug.close()

def ral_liste_href(txt):
	# on génère les retours à la ligne, les liens hyperref et les listes d'un texte
	# on remplace aussi les "CO2" par "CO<sub>2</sub>"
	txt = txt.replace("\n","<br/>")
	txt = txt.replace("CO2","CO<sub>2</sub>")
	txt = creer_liste(txt)
	txt = creer_href(txt)
	return(txt)	

def cita_sstitre(txt,url):

	nb_cit = compter_apparition(txt,rep_cit)
	if nb_cit > 0:
		html_cit = lc_lire(template_citation)
		for i in range(nb_cit):
			[chaine,phrase] = extraire_txt(txt,rep_cit)
			html = html_cit
			html = html.replace("VBA_citation",phrase)
			html = html.replace("VBA_url",url)
			txt = txt.replace(chaine,html)

	nb_sstitre = compter_apparition(txt,rep_sstitre)
	if nb_sstitre > 0:
		html_sstitre = lc_lire(template_soustitre)
		for i in range(nb_sstitre):			
			[chaine,sstitre] = extraire_txt(txt,rep_sstitre)
			html = html_sstitre
			html = html.replace("VBA_soustitre",sstitre)
			txt = txt.replace(chaine,html)


	return(txt)

def compter_apparition(txt,repere):
	i = 0
	ind = txt.find(repere)
	while(ind != -1):
			ind = txt.find(repere,ind+1)
			i = i+1
	return(i)


def creer_liste(contenu):
	html = lc_lire(template_liste)
	contenu = contenu.replace("#LISTE ",html)
	return(contenu)



# la fonction creer_balise parcourt un texte contenant une balise a créer et 
# transforme la première balise à créer qu'elle rencontre en balise html

def creer_href(txt):
	nb_crochet = compter_apparition(txt,"[")
	if nb_crochet > 0:
		j = txt.find("[")
		for i in range(nb_crochet):
			ind1 = txt.find("[",j)
			ind2 = txt.find("]",j)
			seq = txt[ind1+1:ind2]
			if (seq != "..."):
				seq_list = seq.split()
				http = seq_list[-1]
				expr = " ".join(seq_list[:-1])
				#formation de la balise
				str1 = '<a target="_blank" href="'
				str2 = '" style="text-decoration: none; color: #E36C0A;">'
				str3 = '</a>'
				# on remplace la "pré-balise" par la balise
				balise = str1 + http + str2 + expr + str3
				# on renvoie la pré-balise par la balise
				txt = txt.replace("["+seq+"]",balise)
			j = ind2+1
	return(txt)

def creer_json(titre_web,url_image,titre_page,description):
	json = lc_lire(template_json)
	json = json.replace("json-id",titre_web)
	json = json.replace("json-title",titre_page)
	json = json.replace("json-img",url_image)
	json = json.replace("json-description",description)
	return(json)
	
# def fonction(parametre):

