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
control_lane1 = sorted(glob.glob(input_dir + "/*/lane1/controls/*"))

print control_lane1


#os.system("cuffdiff -p 4 -o %s %s %s %s" % (output_dir, merge_lane1, controls, treat))