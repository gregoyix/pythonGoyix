"""
###############################################################################
ProcesaResultadosTestsSelenium.py

v1.1 7-3-13
v2.1 04-03-13 (Importo la parte de wxPython de un modulo aparte (gxWxPython)
y anyado que el usuario apriete una tecla para que no se cierra la pantalla
###############################################################################

"""

import os
import sys
sys.path.append("../__utils")
from gxWxPython import gxWxDameFichero

def dime_resultados(fN) :
   i = 1
   cad1 = "The test has succeeded"
   cad2 = "The test has failed"
   cad3 = 'selenium2.tests'
   cad4 = 'Tests run:'
   cad5 = 'Time elapsed'
   
   f = open(fN, 'r')
   fS = fN[:len(fN)-4] + '.sal'
   g = open(fS,'w')
   print fS
   g  = open(fS, 'w')
   sal = f.readlines()
   for linea in sal:
      s1 = linea.find(cad1)
      s2 = linea.rfind(cad2)
      s4 = linea.rfind(cad4)
      s5 = linea.rfind(cad5)
      if s1!= -1 or s2!=-1:
         # Corto hasta el nombre del test
         s3 = linea.find(cad3)
         kk = linea[s3+len(cad3)+1:]
         print kk,
         g.write(kk)
      else:
         if s4 != -1 and s5 == -1:
            print linea[s4:],
            g.write(linea[s4:])            
   f.close()
   g.close()
   
# test the function/module
#

if __name__ == "__main__":
    ret, file = gxWxDameFichero ()    
    if ret == 0:
       os.chdir(os.path.dirname(file))
       dime_resultados(file)
       # Espero a que el usuario apriete una tecla (Para que no se muera el programa
       var = raw_input("Apriete una tecla para terminar")        
    else :
       print "Error en la aplicacion"
        


