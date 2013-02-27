# -*- coding: cp1252 -*-
"""
###############################################################################
Obten_Canciones_CD.py

v1.0 12-1-12 (Viene de una version anterior en C++)

Nota: Hay que tener cuidado de no poner TABs y de dejar una linea 
despues de la ultima (EOF).
###############################################################################

"""

import os
import sys

def obten(fN, fS) :
   f = open(fN, 'r')
   g  = open(fS, 'w')
   sal = f.readlines()
   cuenta = 1
   estado = 0
   #Quito la extension del fichero
   print fN[:len(fN)-4]
   print("=============\n")
   g.write(fN[:len(fN)-4]+"\n")
   g.write("=============\n")
   for linea in sal:      
      s1 = linea.find("FOLDER\t") # Primero leo el folder
      if s1!= -1 :
         estado = 1         
         continue
      s2 = linea.find("TOTAL\t") # Luego el total      
      if s2!= -1:         
          if estado == 1:             
             (nomAlbum, numCanciones) = procesaAlbum(linea)             
             print "(" + str(cuenta).zfill(3) + ") " + nomAlbum + " " + str(numCanciones)
             g.write("(" + str(cuenta).zfill(3) + ") " + nomAlbum + " " + str(numCanciones)+"\n")
             cuenta = cuenta + numCanciones
             estado = 0
   print"\nNUMERO DE CANCIONES DEL DVD : " + str(cuenta)
   g.write("\nNUMERO DE CANCIONES DEL DVD : " + str(cuenta)+"\n")
   f.close()
   g.close()

def procesaAlbum(s) :
   # print linea
   # Busca los nombres de los albumes entre E: \ y \
   nomAlbum = ""
   numCanciones = 0
   s1 = s.find("E:\\")
   s2 = s.rfind("\\\t")
   if s1!= -1 and s2!= -1 :      
      nomAlbum = s[s1+3:s2]
      resto = s [s2+1:]      
      # Tambien hay que buscar el numero de canciones
      for i in range (1,4):
         s1 = resto.find("\t")      
         resto = resto[s1+1:]       
      s1 = resto.find("\t")
      resto = resto[:s1]
      if resto.isdigit():
         numCanciones = int(resto)
      #print nomAlbum + " " + str(numCanciones)
   return (nomAlbum, numCanciones)   

# test the function/module
#

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print "Obten_Canciones_CD"
        print "Listado dvd" + sys.argv[1]
        print "Fichero salida " + sys.argv[2]
    else:
        print "(Uso): Obten_Canciones_CD.py listado_dvd fichero_salida"
        sys.exit(-1)   
    obten(sys.argv[1],sys.argv[2])
  
