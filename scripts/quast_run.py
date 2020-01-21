import glob
import os
import re


###QUAST
#create a string of contigs to grab stats from
list_of_contigs = sorted(glob.glob("*.contigs.fa"))
contig_string = ""
for i in range(len(list_of_contigs)):
    contig_string = contig_string + "{} ".format(list_of_contigs[i])
os.system("quast.py -o assembly_stats {}".format(contig_string))
