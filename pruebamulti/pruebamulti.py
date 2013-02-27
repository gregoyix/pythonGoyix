# -*- coding: iso-8859-15

import sys, os

programa = 'multi.exe'

if __name__ == "__main__":

    if len(sys.argv) >= 3:
        print "Numeros a multiplicar " + sys.argv[1] + " y " + sys.argv[2]
    else:
        print "Este programa necesita dos parámetros";
        sys.exit(-1)

    cur =  "Current working dir : %s" % os.getcwd()
    #print cur
    # Me cambio al subdirectorio donde esta el programa 
    mypath = 'd:' + os.sep + 'pruebamulti' + os.sep + 'dist'
    #print "PATH " + mypath
    os.chdir(mypath)	

    print "Ejecuto multi ......."    
    res = os.system(programa + " " + sys.argv[1] + " " + sys.argv[2])
    #print res
    mul = int(sys.argv[1]) * int(sys.argv[2])
    print "Resul = " + str(mul)
    if res == mul:
        print "Prueba => OK"
    else:
        print "Prueba => ERROR"
