import requests

from .AuthenticationException import AuthenticationException

BASE_URL = "https://api.mailjet.com/v3/REST/"

def checkErrors(response):
  if (response.status_code != 201 and response.status_code != 200):
    try:
      errorMessage = response.json()["ErrorMessage"]
      raise Exception(errorMessage)
    except ValueError:
      raise AuthenticationException()

def postMailjet(credentials, urlSuffix, body):
  url = BASE_URL + urlSuffix
  response = requests.post(url, auth=credentials, json=body)
  checkErrors(response)
  return response

def putMailjet(credentials, urlSuffix, body):
  url = BASE_URL + urlSuffix
  response = requests.put(url, auth=credentials, json=body)
  checkErrors(response)
  return response

def getMailjet(credentials, urlSuffix):
  url = BASE_URL + urlSuffix
  response = requests.get(url, auth=(credentials["APIKey"], credentials["SecretKey"]))
  checkErrors(response)
  return response

def getContactsList(credentials):
  return getMailjet(credentials, "contactslist")

def createCampaign(credentials, locale, senderID, senderEmail, senderName, subject, contactsListID, title):
  body = {
    "EditMode": "html2",
    "IsTextPartIncluded": True,
    "Locale": locale,
    "Sender": senderID,
    "SenderEmail": senderEmail,
    "SenderName": senderName,
    "Subject": subject,
    "ContactsListID": contactsListID,
    "Title": title,
  }
  return postMailjet(credentials, "campaigndraft", body)

def archiveCampaign(credentials, id):
  body = {
    "Status": -1
  }
  return putMailjet(credentials, "campaigndraft/{}".format(id), body)

def addCampaignContent(credentials, id, html):
  body = {
    "Html-part": html
  }
  return postMailjet(credentials, "campaigndraft/{}/detailcontent".format(id), body)

def scheduleCampaign(credentials, id, date):
  body = {
    "Date": date
  }
  return postMailjet(credentials, "campaigndraft/{}/schedule".format(id), body)

def testCampaign(credentials, id, email):
  body = {
    "Recipients": [
      {
        "Email": email
      }
    ]
  }
  return postMailjet(credentials, "campaigndraft/{}/test".format(id), body)