#!/usr/bin/python -tt
# Run tophat on each sample and compare to the reference genome H_akashiwo.fa (Originally High_exp.fasta)
# Website: http://tophat.cbcb.umd.edu/

# Import OS features to run external programs
import os

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/poly"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
output_dir = "/home/chris/transcriptome/fastq/align"

# Run tophat with 4 threads, should be slightly faster than the default 1 thread
os.system("tophat -p 4 -o %s/lane\ 1/Sample_1 %s %s/lane\ 1/Sample_1_L001_poly_any.fastq" % (output_dir, reference, input_dir))