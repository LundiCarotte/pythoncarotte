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