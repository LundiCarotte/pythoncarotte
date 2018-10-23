# pythoncarotte

Le programme txtenhtml.py transforme un fichier word ou texte en fichiers html (entre autres).

L'intérêt principal du programme est de génerer plusieurs fichiers :

- un fichier html qui constituera le corps du mail envoyé aux abonnés
- un fichier html destiné à être uploadé sur le site internet de LundiCarotte
- un fichier .json destiné à être uploadé dans la partie "Social Media" de la base de donnée du site internet de LundiCarotte, et qui permet d'améliorer l'affichage des posts sur Facebook

1) Type de fichiers acceptés par le programme :

Si le fichier est un .docx ou .odt, il est d'abord converti en fichier .txt (je ne sais pas si cela fonctionne sur système d'exploitation autre que linux). 
Ce fichier .txt est généré dans le dossier où le programme python est présent.

On peut également fournir directement un fichier .txt

2) Options

Si l'on fournit comme unique argument le nom d'un fichier .doc/.docx/.odt/.txt, alors l'on obtient les trois fichiers listés plus haut.

Exemple : txtenhtml.py internet.doc

On peut également fournir des arguments (optionnels) supplémentaires :

- l'option "artsup" génèrera un fichier html conçu pour être uploadé sur le site dans la catégorie "article"

Exemple : txtenhtml.py interview2.doc artsup

- l'option "minimail" génèrera un fichier html conçu pour être envoyé aux abonnés. Il s'agit plus précisément de mails courts qui ne sont pas associés à un article publié sur le site de LundiCarotte (tels que ceux envoyés pendant les vacances d'été 2018)
