#!/usr/bin/python -tt
# Uses cuffmerge to merge samples together for further processing

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/assemble"
output_dir = "/home/chris/transcriptome/fastq/merged"

os.system("cuffmerge -o %s/lane1 %s/lane1.txt" % (output_dir, input_dir))
os.system("cuffmerge -o %s/lane2 %s/lane2.txt" % (output_dir, input_dir))
