Le programme main.py produit un fichier html à partir d'un fichier texte.

Ce programme est capable de générer plusieurs fichiers :

- un fichier texte qui ne contient que les informations nécessaires à la génération des fichiers listés ci-dessous,
- un fichier html qui constituera le corps du mail envoyé aux abonnés,
- un fichier html destiné à être uploadé sur le site internet de LundiCarotte,
- un fichier .json destiné à être uploadé dans la partie "Social Media" de la base de donnée du site internet de LundiCarotte, et qui permet d'améliorer l'affichage des posts sur Facebook.

Le programme prend comme argument le nom d'un fichier texte.

exemple de ce que l'on entrerait dans le terminal :
`python3 main.py biocarburant.txt`

Le fichier texte doit contenir les balises nécessaires à l'obtention des sections souhaitées dans les fichiers html.

Une balise est définie par un repère suivi de crochets.
Exemple : `SOUS-TITRE{}`
Une balise est nécessairement seule sur sa ligne, et ne doit pas contenir de crochets (exception faite pour la balise `CODE{}`)


Le fichier texte devrait toujours contenir la balise suivante :
`TITRE-WEB{titre-web}`

#Pour générer un article publié sur le site :

Balises requises :

```
TITRE-PAGE{Titre de l'article}
DATE-ARTICLE{Le 7 janvier 2018}
URL-IMAGE{https://lundicarotte.fr/api/admin/media/img/biocarburant.png}
AUTEURS{Auteur : Georges Brassens}
PARTAGE_DESCRIPTION{Courte description de l'article pour les réseaux sociaux}

INTRODUCTION
DÉVELOPPEMENT
CONCLUSION
FIN
```
Balises optionnelles :

```
ACTU{} (une actualité de LundiCarotte)
QUESTION{} (question d'un lecteur)
REPONSE{} (réponse de la rédaction)
```

#Pour générer un mail aux abonnés :

Balises requises :

```
TITRE-PAGE{Titre de l'article}
DATE-ARTICLE{Le 7 janvier 2018}
URL-IMAGE{https://lundicarotte.fr/api/admin/media/img/biocarburant.png}
AUTEURS{Georges Brassens}
PARTAGE_DESCRIPTION{Courte description de l'article pour les réseaux sociaux}
JEUDICAROTTE{Gagnant,(M ou F),url_du_jeudicarotte,texte optionnel}
```

##Remarques sur ces balises :
Si l'on insère dans le fichier texte la balise `TITRE-WEB{titre-web}`, l'url de l'article (telle qu'indiquée dans les liens de partage) sera https://lundicarotte.fr/titre-web

Mis à part les balises, le texte présent avant le repère `INTRODUCTION` et après le repère `FIN` est ignoré.

On peut ajouter plusieurs `AUTEURS{}`, qui ajoutent des lignes supplémentaires dans le bloc de signature.

Si les balises concernant l'actu, le jeudicarotte ou les questions des lecteurs sont laissées vides, les sections correspondantes n'apparaîtront pas dans le fichier html.


#Options supplémentaire

##Options d'édition du texte

On peut ajouter des liens hyperref.
Exemple : LundiCarotte est [une infolettre incroyable https://lundicarotte.fr]

On peut ajouter des bullet points avec le repère `LISTE`.

On peut ajouter des sous-titres, citations, images, légendes avec les balises suivantes :
```
SOUS-TITRE{}
CITATION{}
AJOUT-IMAGE{url_de_l_image,[largeur en pixels],[Légende]}
```
(les arguments entre [crochets] sont optionnels)


On peut ajuster la largeur des images en précisant la largeur en pixels comme deuxième argument.
Exemple :
`AJOUT-IMAGE{url_de_l_image,500}`

On peut aussi ajouter une légende.
Si on ajoute une légende sans modifier la largeur, laisser vide le deuxième argument.
`AJOUT-IMAGE{url_de_l_image, ,Ceci est une légende}`

Si la balise `SOUS-TITRE` est présente mais vide (c'est-à-dire : `SOUS-TITRE{}`), `~` sera inséré comme sous-titre.


Lorsqu'une balise de type `AJOUT-IMAGE`,`SOUS-TITRE` ou `CITATION` est présente dans le fichier, le texte présent sur la même ligne après les crochets {} est ignoré (permet de commenter facilement, par exemple pour indiquer le nombre de mots d'une sous-partie).

Les lignes débutant par // sont ignorées.

Du texte contenu dans une balise `CODE{}` ne sera pas modifié et sera inséré tel quel dans le fichier html (par exemple pour insérer des tableaux dont le code html a été généré indépendamment).




##Génerer un fichier html pour la catégorie /articles de la base de donnée

l'option "artsup" génèrera un fichier html conçu pour être uploadé sur le site dans la catégorie "article"

exemple :
`python3 txtenhtml.py interview2.txt artsup`




##Génerer un mail très court

L'option "minimail" génèrera un fichier html conçu pour être envoyé aux abonnés.
Il s'agit plus précisément de mails courts qui ne sont pas associés à un article publié sur le site de LundiCarotte
(tels que ceux envoyés pendant les vacances d'été 2018)

exemple :
`python3 txtenhtml.py 28juillet.txt minimail`
