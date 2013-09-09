#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses fastx_collapser
# Website: http://hannonlab.cshl.edu/fastx_toolkit/commandline.html#fastx_collapser_usage

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run fastx_collapser on all of the files

fastq_indir = "/home/chris/transcriptome/fastq/fastx/trimmed/"
fastq_outdir = "/home/chris/transcriptome/fastq/fastx/collapsed/"

# Sample 1
print "Analyzing Sample 1..."
os.system("fastx_collapser -v -o %s/Sample_1_L001_collapsed.fastq -i %s/Sample_1_L001_trimmed.fastq > %s/Sample_1_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 1_2..."
os.system("fastx_collapser -v -o %s/Sample_1_L002_collapsed.fastq -i %s/Sample_1_L002_trimmed.fastq > %s/Sample_1_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 2
print "Analyzing Sample 2..."
os.system("fastx_collapser -v -o %s/Sample_2_L001_collapsed.fastq -i %s/Sample_2_L001_trimmed.fastq > %s/Sample_2_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 2_2..."
os.system("fastx_collapser -v -o %s/Sample_2_L002_collapsed.fastq -i %s/Sample_2_L002_trimmed.fastq > %s/Sample_2_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 3
print "Analyzing Sample 3..."
os.system("fastx_collapser -v -o %s/Sample_3_L001_collapsed.fastq -i %s/Sample_3_L001_trimmed.fastq > %s/Sample_3_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 3_2..."
os.system("fastx_collapser -v -o %s/Sample_3_L002_collapsed.fastq -i %s/Sample_3_L002_trimmed.fastq > %s/Sample_3_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 4
print "Analyzing Sample 4..."
os.system("fastx_collapser -v -o %s/Sample_4_L001_collapsed.fastq -i %s/Sample_4_L001_trimmed.fastq > %s/Sample_4_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 4_2..."
os.system("fastx_collapser -v -o %s/Sample_4_L002_collapsed.fastq -i %s/Sample_4_L002_trimmed.fastq > %s/Sample_4_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 5
print "Analyzing Sample 5..."
os.system("fastx_collapser -v -o %s/Sample_5_L001_collapsed.fastq -i %s/Sample_5_L001_trimmed.fastq > %s/Sample_5_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 5_2..."
os.system("fastx_collapser -v -o %s/Sample_5_L002_collapsed.fastq -i %s/Sample_5_L002_trimmed.fastq > %s/Sample_5_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 6
print "Analyzing Sample 6..."
os.system("fastx_collapser -v -o %s/Sample_6_L001_collapsed.fastq -i %s/Sample_6_L001_trimmed.fastq > %s/Sample_6_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 6_2..."
os.system("fastx_collapser -v -o %s/Sample_6_L002_collapsed.fastq -i %s/Sample_6_L002_trimmed.fastq > %s/Sample_6_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 7
print "Analyzing Sample 7..."
os.system("fastx_collapser -v -o %s/Sample_7_L001_collapsed.fastq -i %s/Sample_7_L001_trimmed.fastq > %s/Sample_7_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 7_2..."
os.system("fastx_collapser -v -o %s/Sample_7_L002_collapsed.fastq -i %s/Sample_7_L002_trimmed.fastq > %s/Sample_7_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 8
print "Analyzing Sample 8..."
os.system("fastx_collapser -v -o %s/Sample_8_L001_collapsed.fastq -i %s/Sample_8_L001_trimmed.fastq > %s/Sample_8_L001_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 8_2..."
os.system("fastx_collapser -v -o %s/Sample_8_L002_collapsed.fastq -i %s/Sample_8_L002_trimmed.fastq > %s/Sample_8_L002_collapsed.log" % (fastq_outdir, fastq_indir, fastq_outdir))