import dateparser
import json
import os.path
import re
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

def getFieldFromTxtContent(txtContent, field):
  regex = ".*" + field + "{([^}]*)}.*"
  match = re.match(regex, txtContent, re.DOTALL)
  fieldContent = match.group(1)
  return fieldContent

def getDateFromTxtContent(txtContent):
  dateToParse = getFieldFromTxtContent(txtContent, "DATE-ARTICLE")
  date = dateparser.parse(dateToParse).date()
  dateAsString = date.strftime("%Y-%m-%d")
  return dateAsString

def getTitleFromTxtContent(txtContent):
  return getFieldFromTxtContent(txtContent, "TITRE-PAGE")

def createCampaign(credentials, date, sujet, title):
  locale = "fr_FR"
  senderId = "1321967"
  senderEmail = "hello@lundicarotte.fr"
  senderName = "Lundi Carotte"
  subject = title
  contactsListID = 18435
  title = "Newsletter " + date + " - " + sujet

  try:
    response = mailjet.createCampaign(credentials, locale, senderId, senderEmail, senderName, subject, contactsListID, title)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

  id = response.json()["Data"][0]["ID"]
  return id

def addCampaignContent(credentials, id, htmlFile):
  html = getHtml(htmlFile)

  try:
    mailjet.addCampaignContent(credentials, id, html)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

def testCampaign(credentials, id, email):
  try:
    mailjet.testCampaign(credentials, id, email)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

def scheduleCampaign(credentials, id, date):
  try:
    mailjet.scheduleCampaign(credentials, id, date + "T04:30:00")
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

def main(subject, testEmailAddress):
  credentials = getCredentials()

  txtFile = "{0}/{0}.txt".format(subject)
  htmlFile = "{0}/mail-lundicarotte-{0}.html".format(subject)

  if not os.path.isfile(txtFile):
    print("Erreur : le fichier {0} n'existe pas.".format(txtFile))
    sys.exit()

  if not os.path.isfile(htmlFile):
    print("Erreur : le fichier {0} n'existe pas.".format(htmlFile))
    sys.exit()

  with open(txtFile, "r", encoding="utf-8") as file:
    txtContent = file.read()

  date = getDateFromTxtContent(txtContent)
  title = getTitleFromTxtContent(txtContent)

  id = createCampaign(credentials, date, subject, title)
  print("Campagne créée")

  addCampaignContent(credentials, id, htmlFile)
  print("Contenu de la campagne ajouté")

  scheduleCampaign(credentials, id, date)
  print("Campagne programmée")

  testCampaign(credentials, id, testEmailAddress)
  print("Email de test envoyé à " + testEmailAddress)
  
  hyperlink = "https://app.mailjet.com/campaigns/creation/" + format(id)
  print("Url de la campagne : " + hyperlink)

main("livre", "aurelie.valery@gmail.com")