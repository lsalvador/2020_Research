#PBS -S /bin/bash
#PBS -q batch
#PBS -N Mbovis_Annotate
#PBS -l nodes=1:ppn=4:AMD
#PBS -l walltime=12:00:00
#PBS -l mem=20gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml add prokka/1.13-foss-2016b-BioPerl-1.7.1

#move to the working directory and start the assembly process
cd /scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis/contig_dir
python prokka_run.py mbovis_annot.gb
