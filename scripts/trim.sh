#PBS -S /bin/bash
#PBS -q batch
#PBS -N Mbovis_Trim
#PBS -l nodes=1:ppn=15:AMD
#PBS -l walltime=10:00:00
#PBS -l mem=50gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml add sickle/1.33-foss-2016b

#move to the working directory and start the assembly process
cd /work/lslab/noah_pangenome_analysis
python trim_reads.py
