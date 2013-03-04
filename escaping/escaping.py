#! /usr/bin/env python

"""
###############################################################################
escaping.py

v1.1 27-2-13
v2.0 28-2-13 (Versión con GUI)
v2.1 04-03-13 (Paso la parte de wxPython y de ficheros en un modulo aparte
(gxWxPython y gxTrataFicheros.py en __utils)

###############################################################################
"""

import sys
sys.path.append("../__utils")
from gxWxPython import gxWxDameFichero
from gxTrataFicheros import gxAbre_file

import json
 
# Modulo que escapa las comillas de un json y saca un string (para Java)
def escaping(f):
    # Abrimos el fichero
    ss = gxAbre_file(f)
    print ss
    j = 0
    sal = '"'
    # Quitamos los espacios y fines de linea
    for i in ss:
        if i != '\n' and i != ' ':
           sal += i
    sal += '"'
    #print sal
    print json.dumps(sal)

if __name__ == "__main__":        
    ret, file = gxWxDameFichero ()    
    if ret == 0:
        escaping(file)
        # Espero a que el usuario apriete una tecla (Para que no se muera el programa
        var = raw_input("Apriete una tecla para terminar")        
    else :
        print "Error en la aplicacion"
        


