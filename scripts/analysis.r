library("cummeRbund")
setwd("~/GitHub/transcriptome/fastq/diff")

# Load data
lane1 <- readCufflinks('lane1')
lane2 <- readCufflinks('lane2')

csDensity(genes(lane1))
csDensity(genes(lane2))

png("lane1_scatter.png")
csScatter(genes(lane1), 'Control', 'Vibrio')
dev.off()
png("lane2_scatter.png")
csScatter(genes(lane2), 'Control', 'Vibrio')
dev.off()

# Plot Transcripts
png("lane1_volcano.png")
csVolcano(genes(lane1), 'Control', 'Vibrio')
dev.off()
png("lane2_volcano.png")
csVolcano(genes(lane2), 'Control', 'Vibrio')
dev.off()

lane1_diff <- diffData(genes(lane1))
sig_lane1 <- subset(lane1_diff, (significant=='yes'))

lane2_diff <- diffData(genes(lane2))
sig_lane2 <- subset(lane2_diff, (significant=='yes'))

write.table(sig_lane1, 'sig_lane1_092413.txt', sep = '\t', row.names = F, col.names = T, quote = F)
write.table(sig_lane2, 'sig_lane2_092413.txt', sep = '\t', row.names = F, col.names = T, quote = F)