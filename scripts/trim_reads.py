import glob #use for grabbing file names using regular expressions
import os #use to work with the operating system of the machine you are working on
import re #a library to add extra functionality to regex
from multiprocessing import Pool #Parrallel processing

print(""" GENOME TRIMMING SCRIPT
Noah A. Legall, Salvador Lab
Purpose: A Script to trim paired end reads. Automatically runs in parallel.
I personally allocate 10 processors to this job, so make sure to give 10 processors in sapelo2.
*********
""")

# define functions for parallel computing
def trim_parallel(tuple):
    print("{} and {} preparing to trim".format(tuple[0],tuple[1]))
    r1_name = re.sub(".R1.*.fastq",".R1.trimmed.fastq",tuple[0])
    r2_name = re.sub(".R2.*.fastq",".R2.trimmed.fastq",tuple[1])
    single = re.sub(".R1.*.fastq","",tuple[0])
    os.system("sickle pe -f {} -r {} -t sanger -o {} -p {} -s {} -q 30".format(tuple[0],tuple[1],r1_name,r2_name,single))
    print("{} and {} trimming complete".format(r1_name,r2_name))

# 2. initiate pool executors
def implementation(x):
    p = Pool(10)
    p.map(trim_parallel,x)

list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))
work_list = list(zip(list_of_R1,list_of_R2))
implementation(work_list)
