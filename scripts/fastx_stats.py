#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses fastx_quality_stats
# Website: http://hannonlab.cshl.edu/fastx_toolkit/commandline.html#fastq_statistics_usage

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run fastq_quality_trimmer on all of the files

fastq_indir = "/home/chris/transcriptome/fastq/fastx/trimmed/"
fastq_outdir = "/home/chris/transcriptome/fastq/fastx/reports/"

# The *NEW* output format:
# cycle (previously called 'column') = cycle number
# max-count
# For each nucleotide in the cycle (ALL/A/C/G/T/N):
# count   = number of bases found in this column.
# min     = Lowest quality score value found in this column.
# max     = Highest quality score value found in this column.
# sum     = Sum of quality score values for this column.
# mean    = Mean quality score value for this column.
# Q1      = 1st quartile quality score.
# med     = Median quality score.
# Q3      = 3rd quartile quality score.
# IQR     = Inter-Quartile range (Q3-Q1).
# lW      = 'Left-Whisker' value (for boxplotting).
# rW      = 'Right-Whisker' value (for boxplotting).


# Sample 1
print "Analyzing Sample 1..."
os.system("fastx_quality_stats -N -o %s/Sample_1_L001_trimmed.txt -i %s/Sample_1_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 1_2..."
os.system("fastx_quality_stats -N -o %s/Sample_1_L002_trimmed.txt -i %s/Sample_1_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 2
print "Analyzing Sample 2..."
os.system("fastx_quality_stats -N -o %s/Sample_2_L001_trimmed.txt -i %s/Sample_2_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 2_2..."
os.system("fastx_quality_stats -N -o %s/Sample_2_L002_trimmed.txt -i %s/Sample_2_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 3
print "Analyzing Sample 3..."
os.system("fastx_quality_stats -N -o %s/Sample_3_L001_trimmed.txt -i %s/Sample_3_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 3_2..."
os.system("fastx_quality_stats -N -o %s/Sample_3_L002_trimmed.txt -i %s/Sample_3_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 4
print "Analyzing Sample 4..."
os.system("fastx_quality_stats -N -o %s/Sample_4_L001_trimmed.txt -i %s/Sample_4_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 4_2..."
os.system("fastx_quality_stats -N -o %s/Sample_4_L002_trimmed.txt -i %s/Sample_4_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 5
print "Analyzing Sample 5..."
os.system("fastx_quality_stats -N -o %s/Sample_5_L001_trimmed.txt -i %s/Sample_5_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 5_2..."
os.system("fastx_quality_stats -N -o %s/Sample_5_L002_trimmed.txt -i %s/Sample_5_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 6
print "Analyzing Sample 6..."
os.system("fastx_quality_stats -N -o %s/Sample_6_L001_trimmed.txt -i %s/Sample_6_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 6_2..."
os.system("fastx_quality_stats -N -o %s/Sample_6_L002_trimmed.txt -i %s/Sample_6_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 7
print "Analyzing Sample 7..."
os.system("fastx_quality_stats -N -o %s/Sample_7_L001_trimmed.txt -i %s/Sample_7_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 7_2..."
os.system("fastx_quality_stats -N -o %s/Sample_7_L002_trimmed.txt -i %s/Sample_7_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))

# Sample 8
print "Analyzing Sample 8..."
os.system("fastx_quality_stats -N -o %s/Sample_8_L001_trimmed.txt -i %s/Sample_8_L001_trimmed.fastq" % (fastq_outdir, fastq_indir))
print "Analyzing Sample 8_2..."
os.system("fastx_quality_stats -N -o %s/Sample_8_L002_trimmed.txt -i %s/Sample_8_L002_trimmed.fastq" % (fastq_outdir, fastq_indir))