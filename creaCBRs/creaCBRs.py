#!/usr/bin/python
#!/usr/bin/env python

"""
###############################################################################
creaCBRspy

v1.0 18-12-12 (Versión con GUI)

Los ficheros de la BD FR Suele ser un rar con un monton de dirs con imagenes jpg
Una vez descomprimido el rar tenemos un monton de dirs

El progrma crea para cada uno de los subdirectorios un archivo rar y lo renombra a cbr

###############################################################################
"""

import sys
import rarfile
import tarfile

import os
import zipfile
import wx
#from wxPython.wx import *

_selectedDir = "SEL_DIR"
_userCancel  = "USER_CANCEL"
selectedDir =""

# Anyade contenido de un directorio recursivamente a archivo zip 
def addDirGzip(direc):
    nom = direc + ".zip"
    print "Nombre: " + nom
    zf = zipfile.ZipFile(nom, "w")
    for dirname, subdirs, files in os.walk(direc):
        print "DIR: " + dirname
        zf.write(dirname)
        for filename in files:
            print "FILE: " + filename
            zf.write(os.path.join(dirname, filename))
    zf.close()

# Dado un directorio que contiene subdirectorios con tebos en formato jpg
# crea para uno de los subdirectorios un archivo cbdr	
def creaCbrsDirs(direc):
    print "Directorio " + direc
    for dirname, subdirs, files in os.walk(direc):
        if dirname == direc:
            print "ESTE NO"
            continue
        print "DIR: " + dirname
        nom = dirname + ".zip"
        print "Nombre: " + nom
        nom2 = dirname + ".cbr"
        zf = zipfile.ZipFile(nom, "w")	
        for filename in files:
            print "FILE: " + filename
            zf.write(os.path.join(dirname, filename))
        zf.close()
        os.rename(nom, nom2)
	
# No funciona	   
def leeRarFile(file):   
   if rarfile.is_rarfile(file):
        rf = rarfile.RarFile(file)
        for f in rf.infolist():
            print f  .filename, f.file_size
            if f.filename == 'README':
                print rf.read(f)
   else:
    print "No es un fichero rar"

def dirchoose():
   'Gives the user selected path. Use: dirchoose()'
   global selectedDir, _selectedDir , _userCancel #you should define them before
   #userPath = 'c:/'
   userPath = 'C:\Users\gmr\Downloads\MODULO RARFILE PYTHON'
   app = wx.App()
   dialog = wx.DirDialog(None, "Please choose your project directory:",\
   style=1 ,defaultPath=userPath, pos = (10,10))
   if dialog.ShowModal() == wx.ID_OK:
      selectedDir = dialog.GetPath()
      print selectedDir
      return _selectedDir
   else:
      #app.Close()
      dialog.Destroy()
      return _userCancel
        
if __name__ == "__main__":
   ret = dirchoose()
   if ret == _selectedDir:
      os.chdir(selectedDir)
      creaCbrsDirs(selectedDir)



	  
      
