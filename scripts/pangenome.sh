#PBS -S /bin/bash
#PBS -q bahl_salv_q
#PBS -N Mbovis_Pangenome
#PBS -l nodes=1:ppn=15:AMD
#PBS -l walltime=10:00:00
#PBS -l mem=20gb
#PBS -M noahaus@uga.edu
#PBS -m abe

cd $PBS_O_WORKDIR

ml Roary/3.12.0
roary -e --mafft -p 8 *.gff
