#! /usr/bin/env python

"""
###############################################################################
renombra.py

v1.1 23-2-09

Renombra todos los ficheros de un directorio

renombra.py dir_origen extension_antigua extension_nueva

renombra.py . txt log => Renombra todo lo que hay en este directorio txt a log
###############################################################################
"""


import os
import sys
import shutil

#ant = ".rar"
#nue = ".cbr"

def renamer(target) :
   os.chdir(target)
   for filename in os.listdir('.') :
      #print filename
      if filename.endswith(ant):
         i = filename.split(".")
         print i
         newfilename = i[0] + nue
         print newfilename
         os.rename(filename, newfilename)

# test the function/module
#

if __name__ == "__main__":
   print sys.argv[1]
   ant = "." + sys.argv[2]
   print "ant " + ant
   nue = "." + sys.argv[3]
   print "nue " + nue
   renamer(sys.argv[1])
"""
#########################################################################################
   G:\almacen tebeos\dvd tebeos 33\Coleccion Batallas Decisivas [completa][by Alkib
ian]>python renombra.py .
.
['Batallas Decisivas-15 (Vicksburg) [by Alkibian]', 'rar']
Batallas Decisivas-15 (Vicksburg) [by Alkibian].cbr
['Batallas Decisivas-16 (Guadalete) [by Alkibian]', 'rar']
Batallas Decisivas-16 (Guadalete) [by Alkibian].cbr
['Batallas Decisivas-17 (Dardanelos) [by Alkibian]', 'rar']
Batallas Decisivas-17 (Dardanelos) [by Alkibian].cbr
['Batallas Decisivas-18 (Lepanto) [by Alkibian]', 'rar']
Batallas Decisivas-18 (Lepanto) [by Alkibian].cbr
['Batallas Decisivas-19 (Stalingrado) [by Alkibian]', 'rar']
Batallas Decisivas-19 (Stalingrado) [by Alkibian].cbr
['Batallas Decisivas-20 (Inglaterra) [by Alkibian]', 'rar']
Batallas Decisivas-20 (Inglaterra) [by Alkibian].cbr
['Batallas Decisivas-00 (Portadas) [by Alkibian]', 'rar']
Batallas Decisivas-00 (Portadas) [by Alkibian].cbr

G:\almacen tebeos\dvd tebeos 33\Coleccion Batallas Decisivas [completa][by Alkib
ian]>

#########################################################################################

"""
