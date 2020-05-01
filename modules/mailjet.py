import requests

def callMailjet(credentials, urlSuffix, body):
  url = 'https://api.mailjet.com/v3/REST/' + urlSuffix
  response = requests.post(url, auth=credentials, json=body)

  if (response.status_code != 201):
    errorMessage = response.json()["ErrorMessage"]
    raise Exception(errorMessage)

  return response

def createTemplate(credentials, name, author, locale):
  body = {
    "Name": name,
    "Author": author,
    "Locale": locale,
    "LocaleList": [locale],
    "Purposes": ["marketing"]
  }
  return callMailjet(credentials, "template", body)

def addTemplateContent(credentials, id, title, senderName, senderEmail, replyEmail, fromField, replyTo, html):
  body = {
    "Headers": {
      "Subject": title,
      "SenderName": senderName,
      "SenderEmail": senderEmail,
      "ReplyEmail": replyEmail,
      "From": fromField,
      "Reply-To": replyTo
    },
    "Html-part": html
  }
  return callMailjet(credentials, "template/{}/detailcontent".format(id), body)

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
  return callMailjet(credentials, "campaigndraft", body)

def addCampaignContent(credentials, id, html):
  body = {
    "Html-part": html
  }
  return callMailjet(credentials, "campaigndraft/{}/detailcontent".format(id), body)

def scheduleCampaign(credentials, id, date):
  body = {
    "Date": date
  }
  return callMailjet(credentials, "campaigndraft/{}/schedule".format(id), body)