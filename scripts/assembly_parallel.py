#These packages are vital for working on scripts
import glob
import os
import re

#Parrallel processing
from multiprocessing import Pool

#assembly program to use
def spades_run(tuple):
    assemble_dir = re.sub(".R1.*.fastq","_assembly",tuple[0])
    if os.path.isdir(assemble_dir.strip()):
        print("These reads Have been assembled, continuing now")
        return
    else:
        contig_file = re.sub(".R1.*.fastq",".contigs.fa",tuple[0])
        os.system("spades.py -1 {} -2 {} -o {} ".format(tuple[0],tuple[1],assemble_dir))
        os.chdir(assemble_dir)
        os.system("mv contigs.fasta {}".format(contig_file))
        os.chdir("../")

def implementation(x):
    p = Pool(10)
    p.map(spades_run,x)
#get all the pair read files together
list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))
work_list = zip(list_of_R1,list_of_R2)

#initiate the processing pool
implementation(work_list)
