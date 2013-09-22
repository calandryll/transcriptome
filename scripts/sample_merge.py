#!/usr/bin/python -tt
# Uses cuffmerge to merge samples together for further processing

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/assemble"
output_dir = "/home/chris/transcriptome/fastq/merged"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
ha_gff = reference + ".fa"

os.system("cuffmerge -s %s -o %s/lane1 %s/lane1.txt" % (ha_gff, output_dir, input_dir))
os.system("cuffmerge -s %s -o %s/lane2 %s/lane2.txt" % (ha_gff, output_dir, input_dir))
