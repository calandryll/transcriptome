library("cummeRbund")
setwd("~/GitHub/transcriptome/fastq/diff")

# Load data
lane1 <- readCufflinks('lane1')
lane2 <- readCufflinks('lane2')

csDensity(genes(lane1))
csDensity(genes(lane2))

csScatter(genes(lane1), 'Control', 'Vibrio')
csScatter(genes(lane2), 'Control', 'Vibrio')

# Plot Transcripts
csVolcano(genes(lane1), 'Control', 'Vibrio')
csVolcano(genes(lane2), 'Control', 'Vibrio')

lane1_diff <- diffData(genes(lane1))
sig_lane1 <- subset(lane1_diff, (significant=='yes'))

lane2_diff <- diffData(genes(lane2))
sig_lane2 <- subset(lane2_diff, (significant=='yes'))