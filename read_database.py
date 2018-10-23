# Tentative de fichier qui prend en input le l'export de django sur newsletter lc et qui ressort des graphes pertinents

import sys
import csv

# vérifier si argv[1] existe
if (len(sys.argv)<2):
	print("entrée incorrecte : spécifier nom fichier csv en argument")
	# mettre fin au programme python

# On récupère le nom du fichier csv
nftclavier =  sys.argv[1]

with open(nftclavier+'.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print ', '.join(row)
