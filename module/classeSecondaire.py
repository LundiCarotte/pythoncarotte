# -*-coding:utf-8 -*
""" module définissant des repères textes pouvant être utiles à plusieurs blocs."""

class ReperesTexte:

    def __init__(self):
        # définition des repères dans le fichier .txt
        # suite définition des repères :
        # les mots-clés en MOTCLEF{} qui contiennent les infos à extraire du doc
        self.ajout_image = "AJOUT-IMAGE"
        self.citation = "CITATION"
        self.partage_description = "PARTAGE_DESCRIPTION"
        self.sous_titre = "SOUS-TITRE"

class ReperesHtml:

    def __init__(self):
        self.carotte = "<!--Carotte de conclusion-->"
        self.spacer = "<!--SPACER-->"
