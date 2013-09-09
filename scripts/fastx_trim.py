#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses fastq_quality_filter
# Website: http://hannonlab.cshl.edu/fastx_toolkit/commandline.html#fastq_quality_filter_usage

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run fastq_quality_trimmer on all of the files

fastq_indir = "/home/chris/transcriptome/fastq/fastx/clipped/"
fastq_outdir = "/home/chris/transcriptome/fastq/fastx/trimmed/"

# -v = verbose, -q 20 (phred of 20), -p 90 (keep # above this), -i = input file, -o = output file, -Q 32 (needed for reading files)

# Sample 1
print "Analyzing Sample 1..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_1_L001_trimmed.fastq -i %s/Sample_1_L001_clipped.fastq > %s/Sample_1_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 1_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_1_L002_trimmed.fastq -i %s/Sample_1_L002_clipped.fastq > %s/Sample_1_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 2
print "Analyzing Sample 2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_2_L001_trimmed.fastq -i %s/Sample_2_L001_clipped.fastq > %s/Sample_2_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 2_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_2_L002_trimmed.fastq -i %s/Sample_2_L002_clipped.fastq > %s/Sample_2_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 3
print "Analyzing Sample 3..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_3_L001_trimmed.fastq -i %s/Sample_3_L001_clipped.fastq > %s/Sample_3_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 3_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_3_L002_trimmed.fastq -i %s/Sample_3_L002_clipped.fastq > %s/Sample_3_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 4
print "Analyzing Sample 4..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_4_L001_trimmed.fastq -i %s/Sample_4_L001_clipped.fastq > %s/Sample_4_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 4_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_4_L002_trimmed.fastq -i %s/Sample_4_L002_clipped.fastq > %s/Sample_4_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 5
print "Analyzing Sample 5..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_5_L001_trimmed.fastq -i %s/Sample_5_L001_clipped.fastq > %s/Sample_5_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 5_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_5_L002_trimmed.fastq -i %s/Sample_5_L002_clipped.fastq > %s/Sample_5_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 6
print "Analyzing Sample 6..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_6_L001_trimmed.fastq -i %s/Sample_6_L001_clipped.fastq > %s/Sample_6_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 6_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_6_L002_trimmed.fastq -i %s/Sample_6_L002_clipped.fastq > %s/Sample_6_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 7
print "Analyzing Sample 7..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_7_L001_trimmed.fastq -i %s/Sample_7_L001_clipped.fastq > %s/Sample_7_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 7_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_7_L002_trimmed.fastq -i %s/Sample_7_L002_clipped.fastq > %s/Sample_7_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))

# Sample 8
print "Analyzing Sample 8..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_8_L001_trimmed.fastq -i %s/Sample_8_L001_clipped.fastq > %s/Sample_8_L001_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 8_2..."
os.system("fastq_quality_filter -v -Q 32  -q 20 -p 90 -o %s/Sample_8_L002_trimmed.fastq -i %s/Sample_8_L002_clipped.fastq > %s/Sample_8_L002_trimmed.log" % (fastq_outdir, fastq_indir, fastq_outdir))