#!/usr/bin/python -tt
# Quality scores from fastx
# Website: http://hannonlab.cshl.edu/fastx_toolkit/

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run cutadapt on all of the files

fastq_indir = "/home/chris/transcriptome/fastq/trimmed/"
fastq_outdir = "/home/chris/transcriptome/fastq/reports/quality stats"

# Sample 1
print "Analyzing Sample 1..."
os.system("fastx_quality_stats  -i %s/Sample_1_L001_trimmed.fastq %s/Sample_1_L001_trimmed.txt" % (fastq_indir, fastq_outdir))
os.system("fastx_quality_stats  -i %s/Sample_1_L002_trimmed.fastq %s/Sample_1_L002_trimmed.txt" % (fastq_indir, fastq_outdir))
