import httplib

import urllib2

URL_MP3_RAIZ = "http://www.u-historia.com/uhistoria/biblioteca/gramofono/tocata_files/"

def pr0():
    for i in range (1,36): # Varia de 1 a 35
       urlFile = URL_MP3_RAIZ + str(i) + ".mp3"
       print urlFile
       mp3file = urllib2.urlopen(urlFile)
       output = open(str(i) + ".mp3",'wb')
       output.write(mp3file.read())
       output.close()

# Prueba ejemplo de conexion a pagina
# Source: http://docs.python.org/library/httplib.html

def pr1():
   conn = httplib.HTTPConnection("www.python.org")
   # Peticion que existe
   conn.request("GET", "/index.html")
   r1 = conn.getresponse()
   print r1.status, r1.reason
   data1 = r1.read()
   print data1
   # Peticion que NO existe
   conn.request("GET", "/parrot.spam")
   r2 = conn.getresponse()
   print r2.status, r2.reason
   data2 = r2.read()
   conn.close()

if __name__ == "__main__":
   # pr1()
   pr0()
