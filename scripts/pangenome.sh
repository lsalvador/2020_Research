#PBS -S /bin/bash
#PBS -q batch
#PBS -N Mbovis_Pangenome
#PBS -l nodes=1:ppn=16:AMD
#PBS -l walltime=100:00:00
#PBS -l mem=50gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules
ml add Roary/3.12.0

#move to the working directory and start the pangenome analysis
cd /scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis/contig_dir/roary_run
roary -e --mafft -p 12 *.gff 
