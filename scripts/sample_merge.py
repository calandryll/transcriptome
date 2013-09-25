#!/usr/bin/python -tt
# Uses cuffmerge to merge samples together for further processing

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/combined/assemble"
output_dir = "/home/chris/transcriptome/fastq/combined/merged"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
ha_gff = reference + ".gff3"

os.system("cuffmerge -o %s %s/gtf.txt" % (output_dir, input_dir))
#os.system("cuffmerge -o %s/lane2 %s/lane2.txt" % (output_dir, input_dir))
