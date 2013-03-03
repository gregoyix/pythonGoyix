#!/usr/bin/env python

"""
###############################################################################
acortaPath.py

v1.1 18-12-12

Intento de cortar el final de los ficheros para que al grabarlos con Nero no lo corte el
y cueste mucho comparar los fichero uno a uno

Ahora se hace con 97 pero no esta claro que funcione bien (REVISAR)

###############################################################################
"""
import os
import wx

#Parece que Nero corta a partir de que L >= 100 aunque a veces corta con 99
MAX_LEN = 99

_selectedDir = "SEL_DIR"
_userCancel  = "USER_CANCEL"
selectedDir =""

def listado(direc, numDirs):
    i = 0
    for (path, dirs, files) in os.walk(direc):
        print path
        print dirs
        print files
        print "----"
        i += 1
        if i >= numDirs:
           break

def acortaFiles(direc):
    print "Directorio " + direc
    for dirname, subdirs, files in os.walk(direc):
        #print dirname
        for file in files:                    
            if len(file) > MAX_LEN:
               print file + " L: " + str(len(file))
               #Cortamos a 97              
               fileName, fileExtension = os.path.splitext(file)
               nueName = fileName[:97] + fileExtension
               print "NUE " + nueName
               os.rename(os.path.join(dirname,file), os.path.join(dirname,nueName))
	
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
      #print selectedDir
      return _selectedDir
   else:
      #app.Close()
      dialog.Destroy()
      return _userCancel
        
if __name__ == "__main__":
   ret = dirchoose()
   if ret == _selectedDir:
      os.chdir(selectedDir)
      #listado(selectedDir,6)
      acortaFiles(selectedDir)

	  
      
