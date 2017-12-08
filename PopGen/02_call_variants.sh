#!/usr/bin/bash
#SBATCH --nodes 1 --ntasks 8 --time 12:00:00 --mem 16G

module load bcftools
module load samtools

module load tabix

if [ ! -f Ecoli.vcf ]; then
 bcftools mpileup -Ou -f E_coli_K12.fa DnaK_42C.bam | bcftools call  --ploidy-file ploidy.txt -vmO z -o Ecoli.vcf.gz
fi

# This VCF file is the locations of the SNPs and INDELs
zcat Ecoli.vcf.gz > Ecoli.vcf
tabix -p vcf Ecoli.vcf.gz
