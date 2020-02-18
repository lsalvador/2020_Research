#PBS -S /bin/bash
#PBS -q bahl_salv_q
#PBS -N Mbovis_Assembly
#PBS -l nodes=1:ppn=15:AMD
#PBS -l walltime=10:00:00
#PBS -l mem=125gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml add spades/3.12.0-k_245

#move to the working directory and start the assembly process
cd $PBS_O_WORKDIR
python assembly_parallel.py
