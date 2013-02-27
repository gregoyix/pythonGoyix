#! /usr/bin/env python

import sys
import json

programa = 'multi.exe'

# Read mode opens a file for reading only.
def abre_file(name):

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
 
# Modulo que escapa las comillas de un json y saca un string (para Java)
def escaping(f):

    # Abrimos el fichero
    ss = abre_file(f)
    print ss
    j = 0
    sal = '"'
    # Quitamos los espacios y fines de linea
    for i in ss:
        if i != '\n' and i != ' ':
           sal += i
    sal += '"'
    print sal
    #print json.dumps(f)
    
if __name__ == "__main__":

    if len(sys.argv) >= 2:
        print "Fichero original " + sys.argv[1]
    else:
        print "Este programa necesita un parámetros";
        sys.exit(-1)

    escaping(sys.argv[1])
    



