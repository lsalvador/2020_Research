import glob
import os
import re

list_of_R1 = sorted(glob.glob('*R1*.fastq'))
list_of_R2 = sorted(glob.glob('*R2*.fastq'))

for i in range(len(list_of_R1)):
    print("{} and {} preparing to trim".format(list_of_R1[i],list_of_R2[i]))
    r1_name = re.sub(".R1.*.fastq",".R1.trimmed.fastq",list_of_R1[i])
    r2_name = re.sub(".R2.*.fastq",".R2.trimmed.fastq",list_of_R2[i])
    single = re.sub(".R1.*.fastq","",list_of_R1[i])
    os.system("sickle pe -f {} -r {} -t sanger -o {} -p {} -s {} -q 30".format(list_of_R1[i],list_of_R2[i],r1_name,r2_name,single))

os.system("mkdir trimmed; mv *trimmed.fastq trimmed")
