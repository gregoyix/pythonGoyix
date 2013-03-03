#!/usr/bin/python
import os, sys
from stat import *


def walktree(top):
   '''recursively descend the directory tree rooted at top,
      calling the callback function for each regular file'''
 
   for f in os.listdir(top):
       pathname = os.path.join(top, f)
       mode = os.stat(pathname)[ST_MODE]
       if S_ISDIR(mode):
           # It's a directory, recurse into it
           walktree(pathname)
       elif S_ISREG(mode):
           # It's a file
           print pathname
           if pathname.endswith(ant):
              i = pathname.split(".")
              print i
              newfilename = pathname[0:len(pathname)-len(ant)] + nue
              print newfilename
              os.rename(pathname, newfilename)
       else:
           # Unknown file type, print a message
           print 'Skipping %s' % pathname
 
if __name__ == "__main__":
   print sys.argv[1]
   ant = "." + sys.argv[2]
   print "ant " + ant
   nue = "." + sys.argv[3]
   print "nue " + nue
   walktree (sys.argv[1])