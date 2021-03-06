#!/usr/bin/python -tt
# Uses cuffdiff to measure differences between controls and treatments
# Samples 1 - 4 - Controls (No Vibrio, 1uM Iron)
# Samples 5 - 8 - Treatments (Vibrio, 1uM Iron)
# Website:  http://cufflinks.cbcb.umd.edu/manual.html#cuffdiff

# Import OS features to run external programs
import os
import glob

# Directories
merged = "/home/chris/transcriptome/fastq/merged/merged.gtf"
output_dir = "/home/chris/transcriptome/fastq/diff/"
input_dir = "/home/chris/transcriptome/fastq/align"

#cuffdiff merged_asm/merged.gtf liver1.bam,liver2.bam brain1.bam,brain2.bam
# Pull files from directory
control_lane = input_dir + "/controls"
treat_lane = input_dir + "/treat"

print control_lane
print treat_lane

#print "Analyzing Lane 1..."
#os.system("cuffdiff -p 4 -L Control,Vibrio -o %s/lane1 %s %s/control_1.bam,%s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_3.bam,%s/treat_3.bam,%s/treat_4.bam" % (output_dir, merge_lane1, control_lane1, control_lane1, control_lane1, control_lane1, treat_lane1, treat_lane1, treat_lane1, treat_lane1))
#print "Analyzing Lane 2..."
#os.system("cuffdiff -p 4 -L Control,Vibrio -o %s/lane2 %s %s/control_1.bam,%s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_3.bam,%s/treat_3.bam,%s/treat_4.bam" % (output_dir, merge_lane2, control_lane2, control_lane2, control_lane2, control_lane2, treat_lane2, treat_lane2, treat_lane2, treat_lane2))
os.system("cuffdiff --max-bundle-frags 2000000 -p 4 -L Control,Vibrio -o %s %s %s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_2.bam,%s/treat_3.bam" % (output_dir, merged, control_lane, control_lane, control_lane, treat_lane, treat_lane, treat_lane))
# Hey idiot double check that shit!
# Removed treat_4.bam - maybe a bit off
# HIDATA means too many fragments, will add --max-bundle-frags 2000000
