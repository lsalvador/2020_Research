#These packages are vital for working on scripts
import glob
import os
import re

#Parrallel processing
from multiprocessing import Pool
import time

#assembly program to use
def spades_run(tuple):
     assemble_dir = re.sub(".R1.*.fastq","_assembly",tuple[0])
     os.system("spades.py -1 {} -2 {} -o {}".format(tuple[0],tuple[1],assemble_dir))
     os.chdir(assemble_dir)
     os.system("mv contigs.fasta {}".format(contig_file))
     os.chdir("..")

print("No. of CPUs: {}".format(multiprocessing.cpu_count()))

#get all the pair read files together
dir_path = os.path.dirname(os.path.realpath(__file__))
list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))
work_list = zip(list_of_R1,list_of_R2)

#initiate the processing pool
p = Pool(10)
p.map(spades_run,work_list)
