import glob
import os
import re
import sys

gbk = sys.argv[1]
###PROKKKA
#create a string of contigs to grab stats from
list_of_contigs = sorted(glob.glob("*.contigs.fa"))
for i in range(len(list_of_contigs)):
    name = re.sub("contigs.fa","",list_of_contigs[i])
    if os.path.isdir("{}_annot".format(name)):
        print("PROCESSED")
        continue
    os.system("prokka --proteins annot_dir/{} --outdir {}_annot --prefix {} {}".format(gbk,name,name,list_of_contigs[i]))
