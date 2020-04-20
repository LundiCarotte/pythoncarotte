# -*-coding:utf-8 -*
""" module définissant les blocs présents dans les différents types de fichiers HTML."""

from .variables import *

listeblocs = [logo,titre,date,intro,image,dev,outro,auteurs,partage,don,actu,courrier,quizz,pied]

listeblocs_web = [titre,date,intro,image,dev,outro,auteurs,partage,quizz]

listeblocs_mail = [logo,titre,date,intro, image,dev, outro,auteurs,partage,don,actu,courrier,quizz,pied]

listeblocs_artsup = [titre,intro,dev,outro,auteurs,partage]
