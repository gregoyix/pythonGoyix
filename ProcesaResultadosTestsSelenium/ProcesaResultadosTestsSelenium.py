"""
###############################################################################
ProcesaResultadosTestsSelenium.py

v1.1 7-3-13
###############################################################################

"""

import os
import sys

from wxPython.wx import *

_selectedFile = "SEL_FILE"
_userCancel  = "USER_CANCEL"
selectedFile =""

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
       dime_resultados(selectedFile)
