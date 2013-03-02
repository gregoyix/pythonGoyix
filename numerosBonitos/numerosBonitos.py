#!/usr/bin/python
#!/usr/bin/env python

import sys

from array import *

import os

LIMMAX = 99999

a = array( 'I')    
b = array( 'I')    
c = array( 'I')    


def arrMultiplos5():
    global a
    for i in range (5, LIMMAX+1,5):
        # print "Numero : " + str(i)
        a.append(i)
    #print a
    print "Longitud Array a " + str(len(a))

# Multiplos 9
def arrMultiplos9():
    global b
    for i in range (9, LIMMAX+1,9):
        # print "Numero : " + str(i)
        b.append(i)
    #print b
    print "Longitud Array b " + str(len(b))

def arrDiv7Mod2():
    global c
    for i in range (3, LIMMAX+1):
        if (i%7) == 2:
           # print "Numero : " + str(i)
           c.append(i)
    #print c
    print "Longitud Array c " + str(len(c))

def eliminaRepetidos():

    abo = array( 'I')
    aco = array( 'I')
    bco = array( 'I')
     
    # Comparo a y b
    for i in range (0, len(a)):
        for j in range (0, len(b)):
            if a[i] == b [j]:
                #print "Repes " + str(a[i]) + " " + str(b[j])
                abo.append(a[i])

    print abo
    for i in abo:
        a.remove(i)
        b.remove(i)
        if c.count(i) != 0: # Quito los que estan en los 3
            c.remove(i)
    print "Longitud Array a " + str(len(a))
    print "Longitud Array b " + str(len(b))

    # Comparo a y c
    for i in range (0, len(a)):
        for j in range (0, len(c)):
            if a[i] == c [j]:
                #print "Repes " + str(a[i]) + " " + str(c[j])
                aco.append(a[i])
    print aco
    for i in aco:
        a.remove(i)
        c.remove(i)
        if b.count(i) != 0: # Quito los que estan en los 3
            b.remove(i)
    print "Longitud Array a " + str(len(a))
    print "Longitud Array b " + str(len(c))

    # Comparo b y c
    for i in range (0, len(b)):
        for j in range (0, len(c)):
            if b[i] == c [j]:
                #print "Repes " + str(b[i]) + " " + str(c[j])
                bco.append(b[i])
    print bco
    for i in bco:
        b.remove(i)
        c.remove(i)
        if b.count(i) != 0: # Quito los que estan en los 3
            b.remove(i)
    print "Longitud Array b " + str(len(b))
    print "Longitud Array c " + str(len(c))


def juntaArraysOrdenados(a1, a2):
     nueva = array( 'I')
     i = 0
     j = 0
     while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                nueva.append(a1[i])
                #print "a1 " + str(a1[i])
                i=i+1
            else:
                nueva.append(a2[j])
                #print "a2 " + str(a2[j])
                j=j+1
     print i, j
     if i == len(a1):
         for k in range (j, len(a2)):
             nueva.append(a2[k])
     else:
         for k in range (i, len(a1)):
             nueva.append(a1[k])         
     return nueva

def imprimeBonito(a2):
 for i in range (0, len(a2),10):
       if i+10 > len(a2):
           for k in range (i, len(a2)):
               print str(a2[k]),
           print
           break
       print str(a2[i]) + " " + str(a2[i+1]) + " " + str(a2[i+2]) + " " + str(a2[i+3]) + " " + str(a2[i+4])\
       + " " + str(a2[i+5]) + " " + str(a2[i+6]) + " " + str(a2[i+7]) + " " + str(a2[i+8]) + " " + str(a2[i+9])
       
            
                
def suma9(i):
    num = str(i)
    if sum(int(i) for i in num) == 9:
       print "OK " + str(i)
       return '0'
    #else:
    # print "FAILED"

    
def arrSuman9():
    global b
    for i in range (0, 99999):
        if suma9(i) == '0':
           b.append(i)
    print "Longitud Array " + str(len(b))
	        
if __name__ == "__main__":
   arrMultiplos5()
   arrMultiplos9()
   arrDiv7Mod2()
   eliminaRepetidos()
   #print a
   print "Longitud Array a " + str(len(a))
   #print b
   print "Longitud Array b " + str(len(b))
   #print c
   print "Longitud Array c " + str(len(c))
   print "TOTAL " + str(len(a) + len(b) + len(c))
   a1 = array( 'I')
   a2 = array( 'I')
   a1 = juntaArraysOrdenados(a,b)
   a2 = juntaArraysOrdenados(a1,c)
   print a2
   # arrSuman9()



	  
      
