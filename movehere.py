#python code env
#-*-coding:utf-8-*-
#

import os
import shutil
import sys


if __name__ == '__main__':

    s = 0
    e = 0
    if len(sys.argv) > 1:
        cpath = sys.argv[1]
    else:
        cpath = os.getcwd()
    for parent,dirnames,filenames in os.walk(cpath):
        if '__' in parent:
            continue

        for filename in filenames:
            if parent == cpath:
                continue
            else:
                s += 1
                try:
                    shutil.move(os.path.join(parent,filename),cpath)
                except:
                    e += 1

    t = input("move completed, {} files moved!".format(s - e))

