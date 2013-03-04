#! /usr/bin/env python

"""
###############################################################################
gxTrataFicheros.py

v1.0 04-03-13 (Versión preliminar sacada de escaping.py)

Tiene 2 metodos:

fileChoose (interno) Abre el dialogo y elige el fichero
gxWxDameFichero()    Interfaz de fileChoose

# Selecciona un fichero y se cambia al directorio donde esta el fichero
# Devuelve 2 valores:
#		Resul: 0 OK y -1 ERROR
#		fichero seleccionado o "" en caso de error
# Forma de uso:
#
# ret, file = gxWxDameFichero ()
#
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


# Interfaz de fileChoose
#
# Selecciona un fichero y se cambia al directorio donde esta el fichero
# Devuelve 2 valores:
#		Resul: 0 OK y -1 ERROR
#		fichero seleccionado o "" en caso de error
	        


