"""
###############################################################################
CA_renombra.py

v1.1 17-2-10
v2.0 5-7-12 (Versión con GUI)

Nota: Hay que tener cuidado de no poner TABs y de dejar una linea 
despues de la ultima (EOF).
###############################################################################

"""

import os
import sys

from wxPython.wx import *

_selectedFile = "SEL_FILE"
_userCancel  = "USER_CANCEL"
selectedFile =""

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

def fileChoose():
   global selectedFile, _selectedFile , _userCancel #you should define them before
   application = wxPySimpleApp()
   
   # Create a list of filters
   # This should be fairly simple to follow, so no explanation is necessary
   filters = 'All files (*.*)|*.*|Text files (*.txt)|*.txt'

   dialog = wxFileDialog ( None, message = 'Open something....', wildcard = filters, style = wxOPEN | wxMULTIPLE )
   if dialog.ShowModal() == wxID_OK:

      # We'll have to make room for multiple files here
      selected = dialog.GetPaths()

      for selection in selected:
           selectedFile = selection
           print 'Selected:', selection
           return _selectedFile
   else:
       print 'Nothing was selected.'
       dialog.Destroy()
       return _userCancel

# test the function/module
#

if __name__ == "__main__":
   ret = fileChoose ()
   if ret == _selectedFile:
       print selectedFile
       os.chdir(os.path.dirname(selectedFile))
       renamer(selectedFile)
