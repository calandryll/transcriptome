#!/usr/bin/python -tt
# Uses cuffmerge to merge samples together for further processing

# Import OS features to run external programs
import os
import glob

# Directories for input and output
#input_dir = "/home/chris/transcriptome/fastq/assemble"
#output_dir = "/home/chris/transcriptome/fastq/merged"
#reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"

input_dir = "/home/chris/transcriptome/fastq/vchl/assemble"
output_dir = "/home/chris/transcriptome/fastq/vchl/merged"
reference = "/home/chris/transcriptome/fastq/reference/V_chl"


ha_gff = reference + ".gff3"

os.system("cuffmerge -o %s %s/gtf.txt" % (output_dir, input_dir))
#os.system("cuffmerge -o %s/lane2 %s/lane2.txt" % (output_dir, input_dir))
