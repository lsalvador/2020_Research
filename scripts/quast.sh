#PBS -S /bin/bash
#PBS -q bahl_salv_q
#PBS -N Mbovis_Stats
#PBS -l nodes=1:ppn=15:AMD
#PBS -l walltime=10:00:00
#PBS -l mem=20gb
#PBS -M noahaus@uga.edu
#PBS -m abe

cd $PBS_O_WORKDIR

ml QUAST/5.0.2-foss-2018a-Python-2.7.14
python quast_run.py
