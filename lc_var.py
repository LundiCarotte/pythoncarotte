# -*-coding:utf-8 -*

# FICHIER DÉFINISSANT LA QUASI TOTALITÉ DES VARIABLES DU CODE

# définissons l'encodage des templates
encodage = "utf-8"

# noms de fichiers
fichier_original = "fichier-original.txt"


# définition des repères dans le fichier .txt
repintro = "#INTRODUCTION\n"
repdev = "\n#DÉVELOPPEMENT\n"
repoutro = "\n#CONCLUSION\n"
repfin = "#FIN"
# suite définition des repères :
# les mots-clés en MOTCLEF{} qui contiennent les infos à extraire du doc
rep_actu = "ACTU"
rep_auteurs = "AUTEURS"
rep_date = "DATE-ARTICLE"
rep_date_rtv = "DATE-RTV"
rep_jc_option = "JC-OPTION"
rep_gagnant_jc = "GAGNANT-JC"
rep_partage_description = "PARTAGE_DESCRIPTION"
rep_question = "QUESTION"
rep_reponse = "REPONSE"
rep_rtv_option = "RTV-OPTION"
rep_sexe_gagnant = "SEXE-GAGNANT"
rep_titre = "TITRE-PAGE"
rep_titre_web = "TITRE-WEB"
rep_url_image = "URL-IMAGE"
rep_url_jc = "URL-JC"

rep_cit = "#CITATION"
rep_sstitre = "#SOUS-TITRE"
rep_image_supp = "#AJOUT-IMAGE"


# emplacement des templates
template_actu = "lc-templates/Template_Actu.html"
template_citation = "lc-templates/Template_Citation.html"
template_courrier = "lc-templates/Template_Courrier.html"
template_don = "lc-templates/Template_Don.html"
template_html_artsup = "lc-templates/lundicarottetemplate-articles.html"
template_html_lundicarotte = "lc-templates/lundicarottetemplate.html"
template_image = "lc-templates/Template_Image.html"
template_image_supp = "lc-templates/Template_Image_Supp.html"
template_json = "lc-templates/Template_Json.json"
template_liste = "lc-templates/Template_Liste.html"
template_logo = "lc-templates/Template_Logo.html"
template_partage = "lc-templates/Template_Partage.html"
template_pied = "lc-templates/Template_PiedPage.html"
template_quizz = "lc-templates/Template_Quizz.html"
template_soustitre = "lc-templates/Template_Soustitre.html"
template_texte_actu = "lc-templates/Template_TexteActu.html"
template_texte_jc = "lc-templates/Template_TexteJC.html"
template_texte_retrouvailles = "lc-templates/Template_Retrouvailles.html"
template_texte_qr = "lc-templates/Template_TexteQR.html"


# définition des repères dans le html : les emplacements où sont insérés le titre etc.
# reph veut dire "repère html"
reph_logo = "<!--VBA_Logo--><!--VBA_Logo-->"
reph_titre = "<!--VBA_Titre-->Titre<!--VBA_Titre-->"
reph_date = "<!--VBA_Date-->Date<!--VBA_Date-->"
reph_intro = "<!--VBA_Intro--><!--VBA_Intro-->"
reph_dev = "<!--VBA_Article-->Article<!--VBA_Article-->"
reph_outro = "<!--VBA_Conclu--><!--VBA_Conclu-->"
reph_image = "<!--VBA_CaseImage-->Image<!--VBA_CaseImage-->"
reph_auteurs = "VBA_signature"
reph_partage = "<!--VBA_partage--><!--VBA_partage-->"
reph_partage_description = "VBA_partage_description"
reph_partage_image = "VBA_partage_image"
reph_quizz = "<!--VBA_CaseQuizz--><!--VBA_CaseQuizz-->"
reph_actu = "<!--VBA_CaseActu--><!--VBA_CaseActu-->"
reph_don = "<!--VBA_CaseDon--><!--VBA_CaseDon-->"
reph_courrier = "<!--VBA_CaseCourrier--><!--VBA_CaseCourrier-->"
reph_pied = "<!--VBA_PiedPage--><!--VBA_PiedPage-->"


# définition des variables "bloc" : variables qui représentent
# les blocs qu'on veut avoir dans le html final
logo = "logo"
titre = "titre"
date = "date"
image = "image"
intro = "intro"
dev = "dev"
outro = "outro"
auteurs = "auteurs"
partage = "partage"
quizz = "quizz"
don = "don"
actu = "actu"
courrier = "courrier"
pied = "pied"
