
genomestat = read.csv("fungi_genome_stats.csv",header=T,sep=",")
pdf("genome_size.pdf")
plot(genomestat$GENOME_SIZE,genomestat$mRNA_exons.mean)
plot(genomestat$GENOME_SIZE,genomestat$REPEAT)
plot(genomestat$GENOME_SIZE,genomestat$REPEAT,col=genomestat$TAX.phyla)

# more options
