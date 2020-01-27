# 1. Read in both files (done)
# 2. Split based on '_'
# 3. find which isolates I have that are in Liliana's dataset
# 4. those that aren't, put the names in a list.

import sys # use to access arguments
import os # use in order to call commands from terminal script is called in
import re # regular expressions

#1
my_data = open("../analysis/bTB_pangenome/full_data.txt","r")
lili_data = open("../analysis/bTB_pangenome/Lili_full_data.txt","r")

my_list = []
lili_list = []

#2
for my_line in my_data:
    my_list.append(my_line)
for lili_line in lili_data:
    lili_list.append(lili_line)

#3
ID_set = []
data_we_have = set([])

for item in my_list:
    elem = item.split("_")
    ID = "{}{}".format(elem[0],elem[1])
    ID_set.append(ID)

#for i in ID_set:
#    print(i)

for elem in lili_list:
    for id in ID_set:
        if id == elem.split("_")[1]:
            data_we_have.add(elem.strip())
        else:
            continue

data_we_have = list(dict.fromkeys(data_we_have))
#4
for j in sorted(data_we_have):
    print(j)
