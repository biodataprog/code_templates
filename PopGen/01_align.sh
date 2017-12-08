#!/usr/bin/bash
#SBATCH --nodes 1 --ntasks 8 --mem 8G --time 12:00:00

module load bwa
module load samtools
if [ ! -f E_coli_K12.fa.amb ]; then
 bwa index E_coli_K12.fa
fi

# SRR3477089  is "DnaK- evolved line 42C"
# https://www.ebi.ac.uk/ena/data/view/SRX1743471&display=html

if [ ! -f DnaK_42C.sam ]; then
 bwa mem -t 8 -R '@RG\tID:DnaK42C\tSM:DnaK_42C' E_coli_K12.fa SRR3477089_1.fastq.gz SRR3477089_2.fastq.gz > DnaK_42C.sam
fi

if [ ! -f DnaK_42C.bam ]; then 
 samtools fixmate -O bam DnaK_42C.sam DnaK_42C.unsrt.bam
 samtools sort -O bam  --threads 8 -T /scratch/DnaK42 -o DnaK_42C.bam DnaK_42C.unsrt.bam
 samtools index DnaK_42C.bam
fi
