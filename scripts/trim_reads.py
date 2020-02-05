import glob #use for grabbing file names using regular expressions
import os #use to work with the operating system of the machine you are working on
import re #a library to add extra functionality to regex
from multiprocessing import Pool #Parrallel processing

# define functions for parallel computing
def trim_parallel(tuple):
    for i in range(len(tuple[0])):
        print("{} and {} preparing to trim".format(tuple[0],tuple[1]))
        r1_name = re.sub(".R1.*.fastq",".R1.trimmed.fastq",tuple[0])
        r2_name = re.sub(".R2.*.fastq",".R2.trimmed.fastq",tuple[1])
        single = re.sub(".R1.*.fastq","",tuple[0])
        os.system("sickle pe -f {} -r {} -t sanger -o {} -p {} -s {} -q 30".format(tuple[0],tuple[1],r1_name,r2_name,single))

# 1. group the files
list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))
work_list = zip(list_of_R1,list_of_R2)

# 2. initiate pool executors
p = Pool(10)
p.map(trim_parallel,work_list)
