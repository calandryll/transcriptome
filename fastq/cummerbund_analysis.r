library(cummeRbund)

cuff <- readCufflinks("diff")

png("diff/density.png", width=1200, height=1200)
csDensity(genes(cuff))
dev.off()

png("diff/density_rep.png", width=1200, height=1200)
csDensity(genes(cuff),replicates=T)
dev.off()

png("diff/boxplot_rep.png", width=1200, height=1200)
csBoxplot(genes(cuff),replicates=T)
dev.off()

png("diff/boxplot.png", width=1200, height=1200)
csBoxplot(genes(cuff))
dev.off()

png("diff/volcano.png", width=1200, height=1200)
csVolcano(genes(cuff))
dev.off()