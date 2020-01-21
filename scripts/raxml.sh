#PBS -S /bin/bash
#PBS -q batch
#PBS -N Mbovis_RAxML
#PBS -l nodes=1:ppn=16:AMD
#PBS -l walltime=100:00:00
#PBS -l mem=50gb
#PBS -M noahaus@uga.edu
#PBS -m abe

#load modules


#load modules
ml add ml RAxML/8.2.11-foss-2016b-sse

#move to the working directory and start the assembly process
cd /scratch/noahaus/bTB_pangenome/full_MI_data/pangenome_analysis/contig_dir/roary_run/raxml_trees
raxmlHPC-SSE3 -f a -m GTRGAMMA -T 12 -p 124 -x 124 -N 100 -s core_gene_alignment.aln -n mbovis_core
