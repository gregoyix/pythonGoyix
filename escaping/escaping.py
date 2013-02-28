#! /usr/bin/env python

"""
###############################################################################
escaping.py

v1.1 27-2-13
v2.0 28-2-13 (Versión con GUI)

###############################################################################
"""

from wxPython.wx import *

import os,sys
import json

_selectedFile = "SEL_FILE"
_userCancel  = "USER_CANCEL"
selectedFile =""

# Read mode opens a file for reading only.
def abre_file(name):

    try:
       f = open(name, "r")
       try:
          # Read the entire contents of a file at once.
          string = f.read()
          # OR read one line at a time.
          line = f.readline()
       finally:
          f.close()
          return string
    except IOError:
       pass
       return ""
 
# Modulo que escapa las comillas de un json y saca un string (para Java)
def escaping(f):

    # Abrimos el fichero
    ss = abre_file(f)
    print ss
    j = 0
    sal = '"'
    # Quitamos los espacios y fines de linea
    for i in ss:
        if i != '\n' and i != ' ':
           sal += i
    sal += '"'
    print sal
    #print json.dumps(f)
    
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

if __name__ == "__main__":        
    ret = fileChoose ()
    if ret == _selectedFile:
        print selectedFile
        os.chdir(os.path.dirname(selectedFile))
        escaping(selectedFile)

        # Espero a que el usuario apriete una tecla (Para que no se muera el programa
        var = raw_input("Apriete una tecla para terminar")
        sys.exit(1)
        


