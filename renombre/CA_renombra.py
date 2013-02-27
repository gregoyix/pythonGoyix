"""
###############################################################################
CA_renombra.py

v1.1 17-2-10

Nota: Hay que tener cuidado de no poner TABs y de dejar una linea 
despues de la ultima (EOF).
###############################################################################

"""

import os
import sys

def renamer(fN) :
   i = 1
   cad1 = "Track No"
   cad2 = ".mp3"
   f = open(fN, 'r')
   sal = f.readlines()
   for linea in sal:
      s1 = linea.find(". ")
      s2 = linea.rfind("-")
      if s1!= -1 and s2!= -1 :
         # Quitamos los caracteres raros
         linea = linea.replace(":"," ")
         sLin = linea[s1+2:s2]      
         cadOri = cad1 + '%02d' % i + cad2
         print cadOri
         cadDes = '%02d' % i + ".-" + sLin[:s2].rstrip() + cad2
         print cadDes
         i = i +1
         try:
            os.rename(cadOri, cadDes)
         except:
            print "Unexpected error:", sys.exc_info()[0]
            print cadDes
            pass
      else:
        print "Error al leer la linea" + linea 
   f.close()

# test the function/module
#

if __name__ == "__main__":
   print sys.argv[1]
   renamer(sys.argv[1])
  
