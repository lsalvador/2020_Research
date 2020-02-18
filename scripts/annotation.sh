#PBS -S /bin/bash
#PBS -q bahl_salv_q
#PBS -N Mbovis_Annotation
#PBS -l nodes=1:ppn=15:AMD
#PBS -l walltime=10:00:00
#PBS -l mem=20gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml prokka/1.13-foss-2016b-BioPerl-1.7.1

#move to the working directory and start the assembly process
cd $PBS_O_WORKDIR
python prokka_parallel.py
