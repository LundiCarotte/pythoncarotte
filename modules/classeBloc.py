# -*-coding:utf-8 -*
""" module contenant les classes secondaires nécessaires à la génération du template html"""

class Bloc:
    """contient les différents types de données qui définissent un bloc de la newsletter """
    def __init__(self):
        self.nom = ""
        self.a = True
        self.repereHtml = ""
        self.codeAvant = ""
        self.codeApres = ""
