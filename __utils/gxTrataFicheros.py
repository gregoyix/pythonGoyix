#! /usr/bin/env python

"""
###############################################################################
gxTrataFicheros.py

v1.0 04-03-13 (Versión preliminar sacada de escaping.py)

Tiene 1 metodo:

gxAbre_file(name) 

Abre el fichero name en modo lectura y devuelve su contenido
Forma de uso:

contenido = gxAbre_file(name)
###############################################################################
"""


import os,sys


# Devuelve las lineas leidas del fichero

# Read mode opens a file for reading only.
def gxAbre_file(name):
    try:
       f = open(name, "r")
       try:
          # Read the entire contents of a file at once.
          string = f.read()
          # OR read one line at a time.
          line = f.readline()
       finally:
          f.close()
          return string
    except IOError:
       pass
       return ""
	        


