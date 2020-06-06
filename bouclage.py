import dateparser
import json
import os.path
import re
import requests
import sys

import modules.mailjet as mailjet
from modules.AuthenticationException import AuthenticationException

######### VARIABLES #########

CACHE_CREDENTIALS_FILE = "mailjet-apikey.json"
MAILJET_CONTACT_LIST_ID = 18435

######### FUNCTIONS #########

def askUntilNotEmpty(question):
  answer = None
  while (not answer):
    answer = input(question)
  return answer

def getCredentials():
  if os.path.isfile(CACHE_CREDENTIALS_FILE):
    with open(CACHE_CREDENTIALS_FILE) as jsonFile:
      credentials = json.load(jsonFile)
    return (credentials["APIKey"], credentials["SecretKey"])
  else:
    print("C'est la première fois que vous utilisez ce script, merci de rentrer la clé d'API, disponible à l'url suivant :")
    print("https://app.mailjet.com/account/api_keys")

    credentials = None
    while (not credentials):
      apiKey = askUntilNotEmpty("Clé d'API : ")
      secretKey = askUntilNotEmpty("Clé Secrète : ")
      
      credentials = {
        "APIKey": apiKey,
        "SecretKey": secretKey
      }

      # Make a simple call to check if credentials are valid, before saving them
      try:
        mailjet.getContactsList(credentials)
      except AuthenticationException:
        print("ERREUR : la clé d'API n'est pas correcte. Rééessayez.")
        credentials = None

    credentialsJson = json.dumps(credentials)
    with open(CACHE_CREDENTIALS_FILE, 'w', encoding='utf-8') as f:
    		f.write(credentialsJson)
    return (apiKey, secretKey)

def getFieldFromTxtContent(txtContent, field):
  regex = ".*" + field + "{([^}]*)}.*"
  match = re.match(regex, txtContent, re.DOTALL)
  if match:
    fieldContent = match.group(1)
    return fieldContent
  else:
    return None

def getDateFromTxtContent(txtContent):
  dateToParse = getFieldFromTxtContent(txtContent, "DATE-ARTICLE")
  if not dateToParse:
    print("ERREUR : le fichier txt ne contient pas de balise DATE-ARTICLE")
    exit()

  try:
    date = dateparser.parse(dateToParse).date()
  except AttributeError:
    print("ERREUR : la date n'a pas pu être déduite, la balise DATE-ARTICLE dans le fichier txt (valeur : {0}) est probablement mal écrite.".format(dateToParse))
    exit()

  dateAsString = date.strftime("%Y-%m-%d")
  return dateAsString

def getTitleFromTxtContent(txtContent):
  titre = getFieldFromTxtContent(txtContent, "TITRE-PAGE")
  if not titre:
    print("ERREUR : le fichier txt ne contient pas de balise TITRE-PAGE")
    exit()
  return titre

def callMailjet(function, params):
  try:
    return function(*params)
  except Exception as exception:
    print("Erreur mailjet:", exception.args[0])
    sys.exit()

def createCampaign(credentials, date, topic, title):
  locale = "fr_FR"
  senderId = "1321967"
  senderEmail = "hello@lundicarotte.fr"
  senderName = "Lundi Carotte"
  subject = title
  contactsListID = MAILJET_CONTACT_LIST_ID
  title = "Newsletter " + date + " - " + topic

  params = [credentials, locale, senderId, senderEmail, senderName, subject, contactsListID, title]
  response = callMailjet(mailjet.createCampaign, params)

  id = response.json()["Data"][0]["ID"]
  return id

def addCampaignContent(credentials, id, htmlFile):
  with open(htmlFile, "r", encoding="utf-8") as f:
    html = f.read()

  params = [credentials, id, html]
  response = callMailjet(mailjet.addCampaignContent, params)

def testCampaign(credentials, id, email):
  params = [credentials, id, email]
  response = callMailjet(mailjet.testCampaign, params)

def scheduleCampaign(credentials, id, date):
  params = [credentials, id, date + "T04:30:00"]
  response = callMailjet(mailjet.scheduleCampaign, params)

def archiveCampaign(credentials, id):
  params = [credentials, id]
  response = callMailjet(mailjet.archiveCampaign, params)

def validateEmails(emailAddresses):
  for email in emailAddresses:
    if not re.match(".+@.+\..+", email):
      print("ERREUR : {0} ne ressemble pas à une adresse mail".format(email))
      exit()

def validateFile(path):
  if not os.path.isfile(path):
    print("Erreur : le fichier {0} n'existe pas.".format(path))
    sys.exit()

def main(topic, testEmailAddresses):
  validateEmails(testEmailAddresses)

  credentials = getCredentials()

  txtFile = "articles/{0}/{0}.txt".format(topic)
  htmlFile = "articles/{0}/mail-lundicarotte-{0}.html".format(topic)

  validateFile(txtFile)
  validateFile(htmlFile)

  with open(txtFile, "r", encoding="utf-8") as f:
    txtContent = f.read()

  date = getDateFromTxtContent(txtContent)
  title = getTitleFromTxtContent(txtContent)

  id = createCampaign(credentials, date, topic, title)

  addCampaignContent(credentials, id, htmlFile)
  print("Campagne créée")

  hyperlink = "https://app.mailjet.com/campaigns/creation/" + format(id)

  print("Merci de générer la version texte du mail :")
  print("     - Ouvrir la campagne : " + hyperlink)
  print("       (si besoin, le mot de passe est sur LastPass)")
  print("     - Cliquer sur 'Modifier l'email'")
  print("     - En haut à droite, cliquer sur 'Texte'")
  print("     - Cliquer sur 'Générer une version texte à partir du HTML', 'Confirmer'")
  print("     - Cliquer sur 'Récapitulatif et Envoi'")

  answer = None
  while answer != "oui":
    answer = input("Est-ce que c'est fait ? (oui) ")

  for email in testEmailAddresses:
    testCampaign(credentials, id, email)
    print("Email de test envoyé à " + email)

  answer = None
  while not answer in ["oui", "non"]:
    print("Ouvrez le mail de test, et vérifiez si tout vous semble correct.")
    print("Si oui, la campagne sera planifiée. Si non, elle sera archivée et le script s'arrêtera.")
    answer = input("Est-ce que tout vous semble correct? (oui/non) ")

  if answer == "oui":
    scheduleCampaign(credentials, id, date)
    print("Campagne programmée.")
  else:
    archiveCampaign(credentials, id)
    print("Campagne archivée.")
  
######### SCRIPT #########

# To avoid errors, change the current directory to the parent directory of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))

arguments = sys.argv[1:]
if len(arguments) != 2:
    print("ERREUR : paramètres manquants.")
    print("Essayez plutôt : 'python bouclage.py livre aurelie.valery@lundicarotte.fr,servane.courtaux@lundicarotte.fr")
else:
  topic = arguments[0]
  testEmailAddresses = arguments[1].split(",")
  main(topic, testEmailAddresses)