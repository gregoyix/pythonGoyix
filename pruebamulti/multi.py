# -*- coding: iso-8859-15

import sys

if __name__ == "__main__":

    if len(sys.argv) >= 3:
        print sys.argv[0] + " : " + sys.argv[1] + " " + sys.argv[2]
    else:
        print "Este programa necesita dos parámetros";
        sys.exit(-1)

    res = int(sys.argv[1])*int(sys.argv[2])
    print sys.argv[0] + " acaba ....."
    sys.exit(res)

