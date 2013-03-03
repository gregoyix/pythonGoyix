#!/usr/bin/env python

"""
 				cambia_substitulos.py


Se le pasa como argumento el fichero de substitulos y a mano al crear un elemento
de la clase linSubs se le pasa la nueva hora de comienzo:

      estr = linSubs(0,0,2,234)
      
El programa compara esta hora con la primera del fichero de substitulos y ve si hay
que adelantar o atrasar.

Después adelanta o atrasa todos los tiempos la diferencia.


      
(C) GOYIX 30-Marzo-2009

"""

import os
import sys
from optparse import OptionParser

class linSubs:

   def __init__ (self, h, m, s, c):
      self.H0 = [h, m, s, c ] # primera hora del fichero
      self.vez = 0

   def display(self):
      print "Primera hora fichero", self.H0
      
   # Dado un string de la forma "HH:MM:SS,CCC" devuelve una Tupla [ HH MM SS CCC ]
   def str2tup(self, ss):
      # Trato la primera parte
      self.tt = ss.split(':')
      # tt0] son hor tt[1] son min y tt2] son seg,mil_seg
      # Ahora separamos los campos de seg y mil_seg
      self.gg = self.tt[2].split(',')
      return  [int(self.tt[0]), int(self.tt[1]), int(self.gg[0]), int(self.gg[1])]
   
   # Dada una Tupla [ HH MM SS CCC ] devuelve un string de la forma "HH:MM:SS,CCC"
   def tup2str(self, aaa):
       sal = ""
       sal = sal + str(aaa[0]).zfill(2) + ":" + str(aaa[1]).zfill(2) + ":"   
       sal = sal + str(aaa[2]).zfill(2) + "," + str(aaa[3]).zfill(3) 
       #print sal
       return sal

   def calcDif(self, H1):
      self.vez = 1
      # vemos si H0 es > H1
      #print "H0 ", self.H0
      #print "H1 ", H1
      if (self.H0[0] > H1[0]) or \
         (self.H0[0] == H1[0] and self.H0[1]  > H1[1]) or \
         (self.H0[0] == H1[0] and self.H0[1] == H1[1] and self.H0[2]  > H1[2]) or \
         (self.H0[0] == H1[0] and self.H0[1] == H1[1] and self.H0[2] == H1[2] and self.H0[3] > H1[3]):
         print " (Hay que adelantar): H0 mayor que H1"
         self.dif = 0
         self.ori = self.restaHR(self.H0, H1)
      else:
         print " (Hay que retrasar): H1 mayor que H0"
         self.dif = 1
         self.ori = self.restaHR(H1,self.H0)
      print "ORIGEN",  self.ori

   def sumaHR(self,h1, ti):
      if h1[3] + ti[3] >= 1000:
     	  h1[2] = h1[2] + 1
    	  s3 = h1[3] + ti[3] - 1000
      else:
     	  s3 = h1[3] + ti[3]  
      
      if h1[2] + ti[2] >= 60:
          h1[1] = h1[1] + 1
     	  s2 = h1[2] + ti[2] - 60
      else: 
          s2 = h1[2] + ti[2]
     
      if h1[1] + ti[1] >= 60:
     	  h1[0] = h1[0] + 1
     	  s1 = h1[1] + ti[1] - 60
      else:
      	  s1 = h1[1] + ti[1]
      
      s0 = h1[0] + ti[0]
        
      return [s0, s1, s2, s3]  

   def restaHR(self,h1, ti):
     	if h1[3] - ti[3] < 0:
     	   h1[2] = h1[2] + 1
     	   s3 = h1[3] + 1000 - ti[3]
     	else:
     	   s3 = h1[3] - ti[3]
       
     	if h1[2] - ti[2] < 0:
     	   h1[1] = h1[1] + 1
     	   s2 = h1[2] + 60 - ti[2]
        else:
      	  s2 = h1[2] - ti[2]
      
        if h1[1] + ti[1] < 0:
     	  h1[0] = h1[0] + 1
     	  s1 = h1[1] + 60 - ti[1]
        else:
          s1 = h1[1] - ti[1]
      
        s0 = h1[0] - ti[0]
        
        return [s0, s1, s2, s3]  
   
   
   def restaHoras(self, HH):
      if self.dif == 0:
         aa = self.sumaHR(HH, self.ori) 
      else:
         aa = self.restaHR(HH, self.ori)
      return aa
      
   # 00:00:25,501 --> 00:00:28,713
   #Devuelvo HOR MIN SEG y MIL.SEG del primer tiempo   
   def cambiaTiempo(self, lin):
   
      sal = ""
      
      # Separo las dos partes
      ss = lin.split(' --> ')

      # Paso la 1a a una tupla, le resto el ori y lo paso a str otra vez
      H1 = self.str2tup(ss[0])
      #print f.H1
  
      if self.vez == 0:
         self.calcDif(H1)
      
      aaa1 = self.restaHoras(H1)
      sal = self.tup2str(aaa1)

      # Paso la 1a a una tupla, le resto el ori y lo paso a str otra vez
      H2 = self.str2tup(ss[1])
      #print H2
      aaa2 = self.restaHoras(H2)
      sal = sal + " --> " + self.tup2str(aaa2) + "\n"
      print "C: " + sal 
      return sal 
         
if __name__ == "__main__":


   op = OptionParser(usage="%prog [options] arg1")
   op.add_option("-f", "--filename", help="Fichero de substitulos a procesar", metavar="Fichero")
   options, args = op.parse_args()
   
   if len (args) == 1:

      print "Fichero de susbstitulos: ", sys.argv[1]

      # creo un elemento de la clase linea de substitulos y le paso la hora nueva
      estr = linSubs(0,0,2,234)
      estr.display()
   
      # Abro el fichero de substitulos   
      fichEnt = open(sys.argv[1], "r")
      fichSal = open("a.srt", "w")
      # Leo el fichero
      fileList = fichEnt.readlines()
      for line in fileList:      
         if line.find("-->") != -1:
            print "F: " + line
            lica = estr.cambiaTiempo(line)
            fichSal.write(lica)
         else:
            fichSal.write(line)
      fichEnt.close() 
      fichSal.close() 

   else:
      print op.print_help()
