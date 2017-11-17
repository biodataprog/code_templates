mRNA = read.csv("mRNA.lengths",sep="\t",header=T,row.names=1)
TE = read.csv("transposon.lengths",sep="\t",header=T,row.names=1)
pdf("lengths_boxplot.pdf")

nm = c("mRNA","TE")
boxplot(mRNA$Length,TE$Length,main="Boxplot of seq type lengths",
	names=c("mRNA","TE"))

boxplot(mRNA$Length,TE$Length,main="Boxplot of seq type lengths",
	col=c("red","blue"),names=nm)
	
boxplot(subset(mRNA$Length,mRNA$Length < 10000),TE$Length,
	main="Boxplot of shorter seqtype lengths",names=nm,
	col=c("red","blue"),las=2)
