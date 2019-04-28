#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys, os


# on s'assure que 'pythoncarotte' est dans le PATH
dossier = os.path.dirname(os.path.abspath(__file__))
while not dossier.endswith('pythoncarotte'):
    dossier = os.path.dirname(dossier)
if dossier not in sys.path:
    sys.path.append(dossier)

from module.mainfunc import *

# data = getData('tests/gdoc.txt')[0]

# x = data.txt

y = """

SOUS-TITRE{Ni rive gauche, ni rive droite} OK

Le champignon de Paris, de son vrai nom <i>Agaric Bisporus</i>, est la variété de champignons [la plus cultivée https://www.researchgate.net/publication/262179448_Mushroom_Production] (anglais) au monde et en France. [Seul un quart https://www.businesscoot.com/fr/page/le-marche-des-champignons] de la production de champignons française, hors exportations, est destinée à être vendue sous forme entière, le reste va au marché des surgelés, conserves et des préparations alimentaires. La France est actuellement nette importatrice de champignons de Paris, d’après la FAO.

D’abord cultivé dans les catacombes de Paris et en banlieue (d’où son nom lui vient), le champignon de couche (son autre petit nom) déménage en province après la construction du métro en 1895. On utilise alors [des anciennes carrières http://www.champignonidee.fr/histoire/] de pierre où il fait froid et humide. Brrr !

Dans les années 1950, les pays de l’Est et l’Asie appuient sur le champignon, et la France embraye également, en utilisant des hangars frigorifiques pour une culture de masse. Comble de la mondialisation, en 2013, [70% https://magazine.laruchequiditoui.fr/bruno-zamblera-la-culture-du-vrai-champignon-de-paris/] des champignons “de Paris” étaient produits ... en Chine ! La France reste cependant dans le top 5 des producteurs avec les États-Unis (où ils portent le nom de champignons <i>Portobello</i>, ou <i>Cremini</i>) et la Hollande (là-bas on les appelle simplement <i>Champignons</i>, à la française).

CITATION{En 2013, 70% des champignons de Paris étaient produits en Chine.}

Ni animal, ni végétal, on vous l’a dit, mais qu'est ce qu'on mange exactement ? Et bien, ce qu'on appelle "champignon" n'est en fait que la partie émergée de l'iceberg, ou plutôt sa partie reproductrice ! Le "corps du champignon" est en effet souterrain et filamenteux, c’est le mycélium. Celui-ci fonctionne souvent en symbiose avec les racines des grands arbres ce qui crée nos fameux coins à champignons.

SOUS-TITRE{Un gros fumier !} 240

Plusieurs étapes sont nécessaires pour récolter les meilleurs champignons dans les [champignonnières https://fr.wikipedia.org/wiki/Champignonnière] françaises qui se trouvent principalement dans les Pays de la Loire.

LISTE Le compostage :  on réalise un compost avec trois quarts de fumier de cheval et un quart de paille
LISTE La pasteurisation : on stérilise le compost
LISTE L’ensemencement : on y répand des graines germées sur lesquelles est attaché du [mycélium https://fr.wikipedia.org/wiki/Mycélium] (filaments qui donneront ensuite naissance aux pieds et chapeaux que nous connaissons) d’Agaric Bisporus
LISTE Le gobetage : on recouvre le compost ensemencé avec de la terre humide qui servira de premier aliment au mycélium
LISTE  L’installation : on stocke le compost ensemencé dans des boîtes dans des zones sombres et humides
LISTE La fructification : on attend tranquillement que les champignons poussent par vagues, appelées “volées” (une volée tous les huit jours).
LISTE La récolte : les champignons sont récoltés manuellement (pour ceux vendus entiers) ou mécaniquement pour ceux allant dans des préparations agroalimentaires.


AJOUT-IMAGE{, , Pendant la fructification, les champignons de couche peuvent doubler de volume en 24 heures – Photo Sud-Ouest ©LAURENT JAHIER }

À noter que comme on le cultive sous terre ou dans des hangars, sa production est indépendante des saisons. On peut donc le manger toute l'année !

En revanche même si les champignons poussent à l’écart d’autres cultures, ils n’en sont pas pour autant exempts de pesticides. On les retrouve cependant généralement dans les catégories d’aliments cultivés les moins exposés. Dans certaines régions, il est d’ailleurs possible que des champignons sauvages ramassés dans la forêt soient plus riches en pesticides que des champignons de culture.

Ces dernières années, plusieurs projets d’agriculture urbaine tentent de se réapproprier les sous-sols des villes pour la culture de champignons.

Envie de se lancer dans la culture à la maison ? Certains proposent des kits pour faire pousser ses champignons chez soi, avec un bac et du terreau. Si vous vous sentez l’âme d’un champignonniste, c’est par ici.

SOUS-TITRE{Les éboueurs des forêts} 260

Les champignons de Paris ont donc abandonné la forêt pour pousser dans des hangars réfrigérés. Cette information nous a fait hausser les sourcils : l’utilisation massive de hangars froids aurait-elle pour conséquence une empreinte écologique énorme pour ces petits chapeaux blancs ?

"""

mise_en_forme(y,'mail','mail')
