#! /usr/bin/env python

"""
###############################################################################
gxWxPython.py

v1.0 04-03-13 (Versión preliminar sacada de escaping.py)

Tiene 2 metodos:

fileChoose (interno) Abre el dialogo y elige el fichero
gxWxDameFichero()    Interfaz de fileChoose

# Selecciona un fichero y se cambia al directorio donde esta el fichero
# Devuelve 2 valores:
#		Resul: 0 OK y -1 ERROR
#		fichero seleccionado o "" en caso de error
# Forma de uso:
#
# ret, file = gxWxDameFichero ()
#
###############################################################################
"""

from wxPython.wx import *
import os

_selectedFile = "SEL_FILE"
_userCancel  = "USER_CANCEL"
selectedFile =""

# Abre un dialogo y el usuario elige el fichero que desea
#
# Devuelve 2 strings distintos:
#		_selectedFile (si el fichero ha sido elegido)    
#		_userCancel (Si el usuario ha cancelado la operacion)
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

# Interfaz de fileChoose
#
# Selecciona un fichero y se cambia al directorio donde esta el fichero
# Devuelve 2 valores:
#		Resul: 0 OK y -1 ERROR
#		fichero seleccionado o "" en caso de error
def gxWxDameFichero():
    ret = fileChoose ()
    if ret == _selectedFile:
        print selectedFile
        os.chdir(os.path.dirname(selectedFile))
        return 0, selectedFile
    else:
        return -1, ""
	        


