#!/usr/bin/env python3
# -*-coding:utf-8 -*

import sys
from module.mainfunc import *

if len(sys.argv) <= 1:
    print("\nutilisation : '$ ./main.py nom_du_fichier [arguments optionnels]'\n")
else:
    x = ' '.join(sys.argv[1:])
    txtenhtml(x)
