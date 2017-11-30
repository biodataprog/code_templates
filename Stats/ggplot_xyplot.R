library(ggplot2)

# see http://ggplot2.org/ and http://docs.ggplot2.org/current/ for more info
genes <- read.table("xyplot_example_ggplot.dat",header=T,sep="\t")
summary(genes)
plot <- ggplot() + geom_point(data=genes,aes(x=GC.A,y=GC.B,size=PCTID))
ggsave("xyplot_ggplot.pdf",plot)

