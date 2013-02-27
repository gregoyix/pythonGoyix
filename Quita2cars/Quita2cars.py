"""
###############################################################################
Quita2cars.py

v1.1 11-7-11

###############################################################################

"""

import os
import sys

def quita2Cars(fN) :
   i = 1
   f = open(fN, 'r')
   g = open("kk.kk",'w')
   sal = f.readlines()
   for linea in sal:
      s1 = linea.find("#")
      if s1!= -1:
		sLin = linea[s1+1:]
		g.write(sLin)
      else:
        print "Error al leer la linea" + linea 
   f.close()
   g.close()

# test the function/module
#

if __name__ == "__main__":
   print sys.argv[1]
   quita2Cars(sys.argv[1])
  
