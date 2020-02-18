import glob
import os
import re
import sys

#Parrallel processing
from multiprocessing import Pool

def prokka_run(contigs):
    name = re.sub("contigs.fa","",contigs)
    if os.path.isdir("{}_annot".format(name)):
        print("PROCESSED")
        return
    os.system("prokka --outdir {}_annot --prefix {} {}".format(name,name,contigs))

def implementation(x):
    p = Pool(10)
    p.map(prokka_run,x)

#create a string of contigs to grab stats from
list_of_contigs = sorted(glob.glob("*.contigs.fa"))
implementation(list_of_contigs)
