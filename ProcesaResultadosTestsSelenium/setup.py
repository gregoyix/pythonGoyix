from distutils.core import setup
import py2exe
import sys
sys.path.append("C:\Program Files (x86)\\Calibre2\\Microsoft.VC90.CRT")
sys.path.append("../__utils")
setup(console=['ProcesaResultadosTestsSelenium.py'])
