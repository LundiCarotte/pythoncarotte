import requests

def getTemplates(credentials):
  url = 'https://api.mailjet.com/v3/REST/template'
  response = requests.get(url, auth=credentials)
  return response.json()['Data']

def createTemplate(credentials, name, author, locale):
  body = {
    "Name": name,
    "Author": author,
    "Locale": locale,
    "LocaleList": [locale],
    "Purposes": ["marketing"]
  }
  url = 'https://api.mailjet.com/v3/REST/template'
  response = requests.post(url, auth=credentials, json=body)
  return response

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
  url = "https://api.mailjet.com/v3/REST/template/{}/detailcontent".format(id)
  response = requests.post(url, auth=credentials, json=body)
  return response