import json
import os.path
import requests
import sys

import modules.mailjet as mailjet

CACHE_FILE = "mailjet-apikey.json"

def getCredentials():
  if os.path.isfile(CACHE_FILE):
    with open(CACHE_FILE) as jsonFile:
      credentials = json.load(jsonFile)
    return (credentials["APIKey"], credentials["SecretKey"])
  else:
    print("C'est la première fois que vous utilisez ce script, merci de rentrer la clé d'API, disponible à l'url suivant :")
    print("https://app.mailjet.com/account/api_keys")

    apiKey = input("Clé d'API : ")
    secretKey = input("Clé Secrète : ")
    credentials = {
      "APIKey": apiKey,
      "SecretKey": secretKey
    }

    credentialsJson = json.dumps(credentials)
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
    		f.write(credentialsJson)
    return (apiKey, secretKey)

def getHtml(fileName):
  with open(fileName, "r", encoding="utf-8") as f:
    html = f.read()
  return html

def createTemplate(credentials, date, sujet):
  templateName = "Newsletter " + date + " - " + sujet
  author = "Lundi Carotte"
  locale = "fr_FR"
  
  try:
    response = mailjet.createTemplate(credentials, templateName, author, locale)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

  id = response.json()["Data"][0]["ID"]
  return id

def addTemplateContent(credentials, id, htmlFile):
  html = getHtml(htmlFile)

  senderName = "Lundi Carotte"
  senderEmail = "hello@lundicarotte.fr"
  replyEmail = ""
  fromField = "Lundi Carotte <hello@lundicarotte.fr>"
  replyTo = ""

  try:
    mailjet.addTemplateContent(credentials, id, title, senderName, senderEmail, replyEmail, fromField, replyTo, html)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

def main(sujet, date, title, htmlFile):
  credentials = getCredentials()

  print("Création du template...")
  id = createTemplate(credentials, date, sujet)
  print("Template créé")

  print("Ajout du contenu...")
  addTemplateContent(credentials, id, htmlFile)
  hyperlink = "https://app.mailjet.com/template/" + format(id) + "/html"
  print("Contenu du template ajouté, merci de le vérifier manuellement: " + hyperlink)

sujet = "test avalery"
date = "2020-05-04"
title = "À l’assaut du livre"
htmlFile = "C:/dev/pythoncarotte/livre/mail-lundicarotte-livre.html"

main(sujet, date, title, htmlFile)