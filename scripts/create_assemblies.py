# -*- coding: utf-8 -*-

import glob
import os
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))

for i in range(len(list_of_R1)):
    print("{} and {} submitted".format(list_of_R1[i],list_of_R2[i]))
    list_of_R1[i] = list_of_R1[i].replace("‐","-")
    list_of_R2[i] = list_of_R2[i].replace("‐","-")
    name = re.sub(".R1.*.fastq","",list_of_R1[i])
    assemble_dir = re.sub(".R1.*.fastq","_assembly",list_of_R1[i])
    if os.path.isdir(assemble_dir.strip()):
        print("PROCESSED")
        continue
    else:
        contig_file = re.sub(".R1.*.fastq",".contigs.fa",list_of_R1[i])
        os.system("spades.py -1 {} -2 {} -o {}".format(list_of_R1[i],list_of_R2[i],assemble_dir))
        os.chdir(assemble_dir)
        os.system("mv contigs.fasta {}".format(contig_file))
        os.chdir(dir_path)
