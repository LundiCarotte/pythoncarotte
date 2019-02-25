# -*-coding:utf-8 -*
""" module contenant les classes nécessaires à la génération du template html"""

from .fonctions import *
from .styles import *
from .variables import *


class Article:
    """Classe définissant la structure d'un article"""
    def __init__(self,txt,categorie,titre_web,listeblocs):
        self.txt = txt
        self.categorie = categorie
        self.titre_web = titre_web
        self.listeblocs = listeblocs
        self.html = ""
        self.nom_fichier_html = ""

    def generer_html(self):
        self.afficher_balises_manquantes()
        self.init_html()
        self.remplir_html()
        self.generer_nom_html()
        self.ecrire_html()

    def afficher_balises_manquantes(self):
        """ rendu ici, on sait que toutes les balises présentes on leurs deux crochets """

        listerep = bloc2rep(self.listeblocs)

        liste_data = self.txt.split('\n')
        for repere in listerep:
            missing_rep = True
            for k in liste_data:
                if repere in k:
                    missing_rep = False
            if missing_rep:
                print("/!\\   La balise ",repere,"{} est absente du fichier texte.")

    def init_html(self):
        self.html = lc_lire(template.article)

    def remplacer_html(self,repere_html,code):
        self.html = self.html.replace(repere_html,code)

    def remplir_html(self):

        self.ajouter_background()

        self.ajouter_intro()
        self.ajouter_dev()
        self.ajouter_outro()

        for i in self.listeblocs:
            if i == logo:
                self.ajouter_logo()
            if i == titre:
                self.ajouter_titre()
            if i == date:
                self.ajouter_date()
            if i == image:
                self.ajouter_image()
            if i == auteurs:
                self.ajouter_auteurs()
            if i == partage:
                self.ajouter_partage()
            if i == quizz:
                self.ajouter_quizz()
            if i == don:
                self.ajouter_don()
            if i == actu:
                self.ajouter_actu()
            if i == courrier:
                self.ajouter_courrier()
            if i == pied:
                self.ajouter_pied()

        self.ajouter_spacer()


    def ajouter_background(self):

        if self.categorie == 'web' or self.categorie == 'artsup':
            # le background est blanc
            self.html = self.html.replace('<body><!--color-body-->','<body style="background-color:#ffffff;">')
            self.html = self.html.replace('<div><!--color-div-->','<div style="background-color:#ffffff;">')

        if self.categorie == "mail":
            # le background est gris
            self.html = self.html.replace('<body><!--color-body-->','<body style="background-color:#F5F5F5;">',1)
            self.html = self.html.replace('<div><!--color-div-->','<div style="background-color:#F5F5F5;">',1)

    def ajouter_logo(self):
        logo = lc_lire(template.logo)
        self.html = self.html.replace(reph.logo,logo)

    def ajouter_titre(self):
        if self.txt.find(rep.titre) != -1:
            data = extrairecurly(self.txt,rep.titre)
            data = enlever_espaces_inutiles(data)
            # si TITRE{} est vide, on lui donne une valeur par défaut
            data = valeurpardefaut(data,"Un titre original")
            bloc = tag.titre_entree+data+tag.titre_sortie
            # on insère le titre au bon endroit dans le code html
            self.html = self.html.replace(reph.titre,bloc)

    def ajouter_date(self):
        if self.txt.find(rep.date) != -1:
            data = extrairecurly(self.txt,rep.date)
            data = enlever_espaces_inutiles(data)
            data = valeurpardefaut(data,"Un titre original")
            bloc = tag.date_entree+data+tag.date_sortie
            self.html = self.html.replace(reph.date,bloc)

    def ajouter_intro(self):
        if (self.txt.find(rep.intro) != -1 and self.txt.find(rep.dev) != -1):
            data = extrairesandwich(self.txt,rep.intro,rep.dev)
            data = mise_en_forme(data,self.titre_web,self.categorie)
            bloc = tag.texte_entree+data+tag.texte_sortie
            self.html = self.html.replace(reph.intro,bloc)

    def ajouter_image(self):
        if self.txt.find(rep.url_image) != -1:
            data = extrairecurly(self.txt,rep.url_image)
            data = enlever_espaces_inutiles(data)
            if data != '':
                bloc = tag.image
                bloc = bloc.replace("url_Image",data)
                self.html = self.html.replace(reph.image,bloc)

    def ajouter_dev(self):
        if (self.txt.find(rep.dev) != -1 and self.txt.find(rep.outro) != -1):
            data = extrairesandwich(self.txt,rep.dev,rep.outro)
            data = mise_en_forme(data,self.titre_web,self.categorie)
            bloc = tag.texte_entree+data+tag.texte_sortie
            self.html = self.html.replace(reph.dev,bloc)

    def ajouter_outro(self):
        self.remplacer_html(reph.carotte,tag.carotte)
        if (self.txt.find(rep.outro) != -1 and self.txt.find(rep.fin) != -1):
            data = extrairesandwich(self.txt,rep.outro,rep.fin)
            data = mise_en_forme(data,self.titre_web,self.categorie)
            bloc = tag.texte_entree+data+tag.texte_sortie
            self.remplacer_html(reph.outro,bloc)

    def ajouter_auteurs(self):
        if self.txt.find(rep.auteurs) != -1:
            data = extrairecurly(self.txt,rep.auteurs)
            data = enlever_espaces_inutiles(data)
            data = valeurpardefaut(data,"L'éternel Georges Brassens")
            bloc = tag.auteurs_entree+data+tag.auteurs_sortie
            self.remplacer_html(reph.auteurs,bloc)

    def ajouter_partage(self):
        url = generer_url(self.titre_web,self.categorie)
        bloc = tag.partage
        bloc = bloc.replace("_URL_",url)
        self.remplacer_html(reph.partage,bloc)
        # ensuite on ajoute les infos dans la section <head> du html
        # on remplace le titre
        data = extrairecurly(self.txt,rep.titre)
        if data != '':
            self.remplacer_html('content="titre"','content="'+data+'"')
            # on remplace la description
            data = extrairecurly(self.txt,rep.partage_description)
            self.remplacer_html('content="partage_description"','content="' + data + '"')
        # on remplace le lien de l'image
    	# seulement si c'est un article hebdomadaire pour le site internet
        if self.categorie == 'web':
            if self.txt.find(rep.url_image) != -1:
                data = extrairecurly(self.txt,rep.url_image)
                data = enlever_espaces(data)
                if data != '':
                    self.remplacer_html('content="url_partage_image"','content="' + data + '"')

    def ajouter_quizz(self):
        if self.txt.find(rep.titre_web) != -1:
            data = extrairecurly(self.txt,rep.titre_web)
            data = enlever_espaces(data)
            if data != '':
                url = "https://lundicarotte.fr/quizz/"+data
                bloc = tag.case_quizz
                bloc = bloc.replace("url_quizz",url)
                self.remplacer_html(reph.quizz,bloc)

    def ajouter_don(self):
        self.remplacer_html(reph.don,tag.don)

    def ajouter_actu(self):

        actus  = recup_liste(self.txt,rep.actu,self.titre_web,self.categorie)
        n = len(actus)
        # on récupère les données du jeudicarotte
        data_jc = recup_data_jeudicarotte(self.txt)
        # on récupère les données pour les retrouvailles
        data_rtv = recup_data_retrouvailles(self.txt)

        # s'il y a au moins une actu/jeudicarotte/info retrouvailles
        # on créé la case actu

        if (n != 0 or data_jc[0] != '' or data_rtv[0] != ''):
            bloc = tag.case_actu_entree
            if (n >= 0):
                for i in range(0,n):
                    bloc += tag.texte_actu_entree+actus[i]+tag.texte_actu_sortie
            # JeudiCarotte
            if (data_jc[0] != ''):
                # si on veut remplacer le jeudicarotte habituel par autre chose
                if (len(data_jc) >= 4):
                    alt = ','.join(data_jc[3:])
                    alt = mise_en_forme(alt,self.titre_web,self.categorie)
                    bloc += tag.texte_actu_entree+alt+tag.texte_actu_sortie
                else:
                    jc = tag.texte_jc
                    jc = jc.replace("Lien_JC",data_jc[2])
                    jc = jc.replace("Gagnant_2",data_jc[0])
                    if data_jc[1] == 'M':
                        jc = jc.replace("Gagnant_1","Le gagnant")
                    else:
                        jc = jc.replace("Gagnant_1","La gagnante")
                    bloc += jc

            bloc += tag.case_actu_sortie
            self.remplacer_html(reph.actu,bloc)

    def ajouter_courrier(self):
        questions = recup_liste(self.txt,rep.question,self.titre_web,self.categorie)
        reponses = recup_liste(self.txt,rep.reponse,self.titre_web,self.categorie)

        bloc = tag.case_courrier_entree
        for i in range(0,len(questions)):
            bloc += tag.texte_qr_1+questions[i]
            if i <= (len(reponses)-1):
                bloc += tag.texte_qr_2+reponses[i]+tag.texte_qr_3
            bloc += tag.texte_qr_4
        #
        bloc += tag.case_courrier_sortie
        self.remplacer_html(reph.courrier,bloc)


    def ajouter_pied(self):
        self.remplacer_html(reph.pied,tag.pied)


    def ajouter_spacer(self):
        self.remplacer_html(reph.spacer,tag.spacer)


    def generer_nom_html(self):
        if self.categorie == "web":
            self.nom_fichier_html = self.titre_web+"/lundicarotte-"+self.titre_web+".html"
        if self.categorie == "mail":
            self.nom_fichier_html = self.titre_web+"/mail-lundicarotte-"+self.titre_web+".html"
        if self.categorie == "artsup":
            self.nom_fichier_html = self.titre_web+"/article-"+self.titre_web+".html"

    def ecrire_html(self):
        ecrire_fichier(self.nom_fichier_html,self.html)

    def generer_json(self):
    	nom_json = self.titre_web+"/"+self.titre_web+".json"
    	url_image = extrairecurly(self.txt,rep.url_image)
    	titre_page = extrairecurly(self.txt,rep.titre)
    	description = extrairecurly(self.txt,rep.partage_description)
    	json = creer_json(self.titre_web,url_image,titre_page,description)
    	ecrire_fichier(nom_json,json)
