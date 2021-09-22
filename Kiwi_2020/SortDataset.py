import os
from os import path
import glob
import random

Dirs = ["Test","Train"]
Sets = ["b1_", "b2_","k1_","k2_","k3_","k4_","k5_"]
TestPercentage = 0.2


for d in Dirs:
    if path.exists(d):
        os.system("rm -r {}".format(d))
        os.system("mkdir {}".format(d))
    else:
        os.system("mkdir {}".format(d))

for s in Sets:
    files = glob.glob(s+"*.png")
    #Move all the Test images
    numTestImgs = int(len(files)*TestPercentage)
    for i in range(0,numTestImgs):
        filename = random.choice(files)
        os.system("cp -v {} {}".format(filename,Dirs[0]))
        os.system("cp -v {} {}".format(filename[:-4] + ".xml",Dirs[0]))
        files.remove(filename)
    for remaining in files:
        os.system("cp -v {} {}".format(remaining,Dirs[1]))
        os.system("cp -v {} {}".format(remaining[:-4] + ".xml",Dirs[1]))
