# 1. Read in both files (done)
# 2. Split based on '_'
# 3. find which isolates I have that are in availana's dataset
# 4. those that aren't, put the names in a list.

import sys # use to access arguments
import os # use in order to call commands from terminal script is called in
import re # regular expressions


from fuzzywuzzy import fuzz
#1
subset_data = open("../analysis/bTB_pangenome/data_to_match.txt","r")
avail_data = open("../analysis/bTB_pangenome/available_MI_data.csv","r")

subset_list = []
avail_list = []

#2
for subset_line in subset_data:
    subset_list.append(subset_line.strip())
for avail_line in avail_data:
    avail_list.append(avail_line.strip())

#3
ID_set = []
data_we_have = set([])

for item in subset_list:
    elem = item.split("_")
    ID = "{}{}".format(elem[0],elem[1])
    ID_set.append(ID)

sequence_dict = dict(zip(ID_set,subset_list))
#for i in ID_set:
#    print(i)

for elem in avail_list:
    for id,name in sequence_dict.items():
        if fuzz.ratio(id, elem.split(",")[1]) > 93.99:
            data_we_have.add("{},{}".format(elem,name))
        else:
            continue

data_we_have = list(dict.fromkeys(data_we_have))
#4
for j in sorted(data_we_have):
    print(j)
