#!/usr/bin/bash
#SBATCH --nodes 1 --ntasks 1 --mem 2G --time 2:00:00

if [ ! -f E_coli_K12.fa ]; then
curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-37/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz

curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-37/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.chromosome.Chromosome.gff3.gz

mv Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz E_coli_K12.fa.gz
mv Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.chromosome.Chromosome.gff3.gz E_coli_K12.gff3.gz
gunzip E_coli*.gz
fi

# no need to unzip these
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR347/009/SRR3477089/SRR3477089_1.fastq.gz
curl -O ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR347/009/SRR3477089/SRR3477089_2.fastq.gz

