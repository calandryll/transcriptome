#!/usr/bin/python -tt
# Uses fastqc to examine quality of raw and trimmed data

# Import OS features to run external programs
import os
import glob

#v = "Version 0.3"
# Versions:
#       0.1 - Read in files for directory
#       0.2 - 
#       0.3 - Get all of it working properly
#       0.4 -
#       0.5 -
#       0.6 -

print "Fastqc %s\n" % (v)

# Setup directories to the data
fastq_raw = "/home/chris/transcriptome/fastq/original/"
fastq_trimmed = "/home/chris/transcriptome/fastq/trimmed/"
fastq_routput = "/home/chris/transcriptome/fastq/reports/raw"
fastq_toutput = "/home/chris/transcriptome/fastq/reports/trimmed"

print "Raw Directory: %s\n" % (fastq_raw)
print "Trimmed Directory: %s\n" % (fastq_trimmed)
print "Scanning Raw Directory..."

# Pull file names from raw
fastq_rfiles = glob.glob1(fastq_raw, "*.fastq")
fastq_tfiles = glob.glob1(fastq_trimmed, "*.fastq")

raw = len(list(fastq_rfiles))
for files in range(raw):
        print fastq_rfiles[files]

		fastqc_rrun = fastq_raw + fastq_rfiles[files]
        # Run fastqc
        os.system("fastqc -o %s %s" % (fastq_routput, fastqc_rrun))

trim = len(list(fastq_tfiles))
for files in range(trim):
        print fastq_tfiles[files]

        fastqc_trun = fastq_trimmed + fastq_tfiles[files]
        # Run fastqc
        os.system("fastqc -o %s %s" % (fastq_toutput, fastqc_trun))
