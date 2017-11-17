mRNA <- read.csv("mRNA.lengths",sep="\t",header=T)
TE <- read.csv("transposon.lengths",sep="\t",header=T)
summary(TE)

pdf("lengths_hist.pdf")
hist(TE$Length)
hist(TE$Length,100,main="TE length distribution")
hist(mRNA$Length,100,main="mRNA length distribution")

short = subset(mRNA,mRNA$Length < 10000)
hist(short$Length,100,main="shorter mRNA length distribution")
big_transcripts = subset(mRNA,mRNA$Length > 50000)
big_transcripts$Name
big_transcripts
