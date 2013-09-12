#!/usr/bin/python -tt
# Run tophat on each sample and compare to the reference genome H_akashiwo.fa (Originally High_exp.fasta)
# Website: http://tophat.cbcb.umd.edu/

# Import OS features to run external programs
import os
import glob
import fnmatch

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/poly"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
output_dir = "/home/chris/transcriptome/fastq/align"

# Setup directories to the data
#fastq_raw = "/home/chris/transcriptome/fastq/original/"
#fastq_trimmed = "/home/chris/transcriptome/fastq/poly/"
#fastq_routput = "/home/chris/transcriptome/fastq/reports/raw"
#fastq_toutput = "/home/chris/transcriptome/fastq/reports/poly/"

#print "Raw Directory: %s\n" % (fastq_raw)
print "Directory: %s\n" % (input_dir)
print "Scanning Directory..."

# Pull files from directory
blarg = glob.iglob(input_dir + "/*/*.fastq")
print blarg