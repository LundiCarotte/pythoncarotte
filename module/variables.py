# définition des variables globales

from .styleTexte import *
from .classeSecondaire import *

# emplacement du template
template_article = "templates/lundicarottetemplate.html"

# définition des variables "bloc" : variables qui représentent
# les blocs qu'on veut avoir dans le html final
logo = "logo"
titre = "titre"
date = "date"
intro = "intro"
image = "image"
dev = "dev"
outro = "outro"
auteurs = "auteurs"
contributeurs = "contributeurs"
actu = "actu"
courrier = "courrier"
don = "don"
partage = "partage"
quizz = "quizz"
pied = "pied"

mail = 'mail'
web = 'web'
artsup = 'artsup'
all = 'all'

# définition de quelques repères texte
repere_titre_web = "TITRE-WEB"
tag = Tag() # classe définie dans le module styleTexte
rep = ReperesTexte() # classe définie dans le module classeSecondaire
reph = ReperesHtml() # classe définie dans le module classeSecondaire

repTexteCode = "CODE"
repTexteListe = "LISTE"
htmlListe = "&bull;"
