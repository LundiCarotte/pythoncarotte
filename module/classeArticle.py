# -*-coding:utf-8 -*
""" module contenant les classes nécessaires à la génération du template html"""


from .fonctions import *
from .styleBlocs import *

class coupleHtml:
    """Associe un repère HTML au code HTML qui sera inséré dans le template à la place de ce repère HTML"""
    def __init__(self):
        self.repereHtml = ""
        self.codeHtml = ""

class Article:
    """Classe définissant la structure d'un article"""
    def __init__(self,txt,categorie,titre_web,listeblocs):
        self.txt = txt
        self.categorie = categorie
        self.titre_web = titre_web
        self.listeblocs = listeblocs
        self.dictHtml = ""
        self.html = ""
        self.nom_fichier_html = ""

    def checkerTexte(self):
        """ regroupe les fonctions qui checkent que le contenu est bien formaté """

    def generer_html(self):
#        self.afficher_balises_manquantes()
        self.creerDictHtml()
        self.init_html()
        self.ajouter_background()
        self.insererContenuHtml()
        self.ajouter_spacer()
        self.ajouter_carotte()
        self.ajouterInfosMeta()
        self.generer_nom_html()
        self.ecrire_html()

    def repereExiste(self,repere):
        """renvoie un booléen : True si 'repere' est présent dans self.txt, False sinon"""
        return((False, True)[self.txt.find(repere) != -1])

    def creerDictHtml(self):
        """ Génère un dictionnaire dont les clés sont les listes de blocs, et les valeurs sont des objets coupleHtml. Stocke ce dictionnaire dans self.dictHtml."""

        dictHtml = {}
        listeblocs = self.listeblocs
        for i in listeblocs:
            myCouple = coupleHtml()
            bloc = creerBloc(i)
            if bloc.nom != "":
                myCouple.repereHtml = bloc.repereHtml
                contenu = creerContenu(self,bloc)
                myCouple.codeHtml = bloc.codeAvant + contenu + bloc.codeApres
                # on ajoute le couple créé dans le dictionnaire
                dictHtml[i] = myCouple
                # on stocke également des informations utiles pour la suite en tant qu'attributs de l'article

                # pour ce qui suit : cf fonction ajouter_infos_meta)
                if i == titre:
                    self.titrePage = contenu
        self.dictHtml = dictHtml

    def init_html(self):
        with open(template_article,"r",encoding='utf-8') as f:
            self.html = f.read()

    def ajouter_background(self):

        if self.categorie == 'web' or self.categorie == 'artsup':
            # le background est blanc
            self.html = self.html.replace('<body><!--color-body-->','<body style="background-color:#ffffff;">')
            self.html = self.html.replace('<div><!--color-div-->','<div style="background-color:#ffffff;">')

        if self.categorie == "mail":
            # le background est gris
            self.html = self.html.replace('<body><!--color-body-->','<body style="background-color:#F5F5F5;">',1)
            self.html = self.html.replace('<div><!--color-div-->','<div style="background-color:#F5F5F5;">',1)

    def insererContenuHtml(self):
        """ Pour chacun des couples (a,b) du dictionnaire self.dictHtml, cette fonction remplace a par b (dans self.html) """
        dict = self.dictHtml
        for i in dict:
            self.html = self.html.replace(dict[i].repereHtml,dict[i].codeHtml)

    def ajouterInfosMeta(self):
        # meta titre
        if 'titrePage' in dir(self):
            titrePage = self.titrePage
            self.html = self.html.replace('content="titre"','content="'+titrePage+'"')
        # meta partage
        if self.repereExiste(rep.partage_description):
            descriptionPartage = extrairecurly(self.txt,rep.partage_description)
            self.html = self.html.replace('content="partage_description"','content="' + descriptionPartage + '"')
        # meta image
        repUrlImage = creerBloc(image).repereTexte
        metaImage = ''
        if self.categorie == web and self.repereExiste(repUrlImage):
            urlImage = extrairecurly(self.txt,repUrlImage)
            metaImage = '<meta property="og:image" content="' + urlImage + '" />'
        self.html = self.html.replace('<meta property="og:image" content="url_partage_image" />', metaImage)

    def ajouter_spacer(self):
        self.html = self.html.replace(reph.spacer,tag.spacer)

    def ajouter_carotte(self):
        self.html = self.html.replace(reph.carotte,tag.carotte)

    def generer_nom_html(self):
        begin = self.titre_web
        mid = "/lundicarotte-"
        end = self.titre_web+".html"
        if self.categorie == "mail":
            mid = "/mail-lundicarotte-"
        if self.categorie == "artsup":
            mid = "/article-"
        self.nom_fichier_html = begin + mid + end

    def ecrire_html(self):
        ecrire_fichier(self.nom_fichier_html,self.html)

    def generer_json(self):
    	nom_json = self.titre_web+"/"+self.titre_web+".json"
    	url_image = extrairecurly(self.txt,creerBloc(image).repereTexte)
    	titre_page = extrairecurly(self.txt,creerBloc(titre).repereTexte)
    	description = extrairecurly(self.txt,rep.partage_description)
    	json = creer_json(self.titre_web,url_image,titre_page,description)
    	ecrire_fichier(nom_json,json)
