# -*-coding:utf-8 -*
""" module contenant les variables nécessaires à la génération du template html"""

# lien google analytics
lien_google = ''


# définissons l'encodage des templates
encodage = "utf-8"

# noms de fichiers
fichier_original = "fichier-original.txt"

# emplacement des templates

class Template:

    def __init__(self):
        self.json = "templates/JSON.json"
        self.logo = "templates/LOGO.html"
        self.spacer = "templates/SPACER.html"
        self.liste = "templates/LISTE.html"
        self.partage = "templates/PARTAGE.html"
        self.texte_actu = "templates/TEXTE-ACTU.html"
        self.texte_jc = "templates/TEXTE-JC.html"
        self.texte_qr = "templates/TEXTE-QR.html"
        self.article = "templates/lundicarottetemplate.html"
        self.quizz = "templates/QUIZZ.html"

template = Template()


# repères dans le html: les emplacements où sont insérés le titre etc.

class ReperesHtml:

    def __init__(self):
        self.actu = "<!--CaseActu-->"
        self.auteurs = "<!--AUTEURS-->"
        self.carotte = "<!--Carotte de conclusion-->"
        self.courrier = "<!--CaseCourrier-->"
        self.date = "<!--DATE-->"
        self.dev = "<!--DÉVELOPPEMENT-->"
        self.don = "<!--CaseDon-->"
        self.image = "<!--IMAGE-->"
        self.intro = "<!--INTRO-->"
        self.legende = "<!--LÉGENDE-->"
        self.logo = "<!--LOGO-->"
        self.outro = "<!--CONCLUSION-->"
        self.partage = "<!--PARTAGE-->"
        self.pied = "<!--PiedPage-->"
        self.quizz = "<!--CaseQuizz-->"
        self.titre = "<!--TITRE-->"
        self.spacer = "<!--SPACER-->"

reph = ReperesHtml()

## repères dans le texte de l'article

class ReperesTexte:

    def __init__(self):
        # définition des repères dans le fichier .txt
        self.intro = "INTRODUCTION"
        self.dev = "DÉVELOPPEMENT"
        self.outro = "CONCLUSION"
        self.fin = "FIN"
        # suite définition des repères :
        # les mots-clés en MOTCLEF{} qui contiennent les infos à extraire du doc
        self.actu = "ACTU"
        self.auteurs = "AUTEURS"
        self.ajout_image = "AJOUT-IMAGE"
        self.citation = "CITATION"
        self.code = "CODE"
        self.date = "DATE-ARTICLE"
        self.rtv = "RETROUVAILLES"
        self.jc = "JEUDICAROTTE"
        self.partage_description = "PARTAGE_DESCRIPTION"
        self.question = "QUESTION"
        self.reponse = "REPONSE"
        self.sous_titre = "SOUS-TITRE"
        self.titre = "TITRE-PAGE"
        self.titre_web = "TITRE-WEB"
        self.url_image = "URL-IMAGE"
        self.url_jc = "URL-JC"

rep = ReperesTexte()


# définition des variables "bloc" : variables qui représentent
# les blocs qu'on veut avoir dans le html final
logo = "logo"
titre = "titre"
date = "date"
image = "image"
intro = "intro"
dev = "dev"
outro = "outro"
auteurs = "auteurs"
partage = "partage"
quizz = "quizz"
don = "don"
actu = "actu"
courrier = "courrier"
pied = "pied"

####################################
####################################
