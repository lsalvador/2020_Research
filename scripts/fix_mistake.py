import os # use in order to call commands from terminal script is called in
import re

R1 = open("/scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis/R1.txt","r")
R2 = open("/scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis/R2.txt","r")

r1_list = []
r2_list = []



for line in R1:
    r1_list.append(line.strip())

for line in R2:
    r2_list.append(line.strip())

R1.close()
R2.close()

result = set(sorted(r1_list)) ^ set(sorted(r2_list))
os.chdir("/project/lslab/lab_shared/DATA/Michigan_WGS")

for i in result:
    print("copying {}".format(i))
    os.system("cp -a /Michigan_WGS/*/{}* /scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis".format(i))
