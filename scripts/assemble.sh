#PBS -S /bin/bash
#PBS -q batch
#PBS -N Mbovis_Assembly
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=100:00:00
#PBS -l mem=125gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml add spades/3.12.0-k_245

#move to the working directory and start the assembly process
cd /scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis
python create_assemblies.py
