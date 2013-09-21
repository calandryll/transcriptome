#!/usr/bin/python -tt
# Uses cuffdiff to measure differences between controls and treatments
# Samples 1 - 4 - Controls (No Vibrio, 1uM Iron)
# Samples 5 - 8 - Treatments (Vibrio, 1uM Iron)
# Website:  http://cufflinks.cbcb.umd.edu/manual.html#cuffdiff

# Import OS features to run external programs
import os
import glob

# Directories
merge_lane1 = "/home/chris/transcriptome/fastq/merged/lane1/merged.gtf"
merge_lane2 = "/home/chris/transcriptome/fastq/merged/lane2/merged.gtf"
output_dir = "/home/chris/transcriptome/fastq/diff/"
input_dir = "/home/chris/transcriptome/fastq/align/"


#cuffdiff merged_asm/merged.gtf liver1.bam,liver2.bam brain1.bam,brain2.bam
# Pull files from directory
control_lane1 = input_dir + "lane1/controls"
treat_lane1 = input_dir + "lane1/treat"
control_lane2 = input_dir + "lane2/controls"
treat_lane2 = input_dir + "lane2/treat"

print control_lane1
print treat_lane1
print control_lane2
print treat_lane2

print "Analyzing Lane 1..."
os.system("cuffdiff -p 4 -o %s/lane1 %s %s/control_1.bam,%s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_3.bam,%s/treat_3.bam,%s/treat_4.bam" % (output_dir, merge_lane1, control_lane1, control_lane1, control_lane1, control_lane1, treat_lane1, treat_lane1, treat_lane1, treat_lane1))
print "Analyzing Lane 2..."
#os.system("cuffdiff -p 4 -o %s/lane2 %s %s %s" % (output_dir, merge_lane2, control_lane2, treat_lane2))
