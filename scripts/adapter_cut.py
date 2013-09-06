#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses cutadapt to remove adaptors
# Website: https://code.google.com/p/cutadapt/

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run cutadapt on all of the files

# Adapter listing
index_2 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCGATGTATCTCGTATGCCGTCTTCTGCTTG"	# Sample 1
index_4 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTGACCAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 2
index_5 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 3
index_6 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACGCCAATATCTCGTATGCCGTCTTCTGCTTG"	# Sample 4
index_7 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATCATCTCGTATGCCGTCTTCTGCTTG" # Sample 5
index_12 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCTTGTAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 6
index_1 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 7
index_3 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTTAGGCATCTCGTATGCCGTCTTCTGCTTG"	# Sample 8

fastq_indir = "/home/chris/transcriptome/fastq/original/"
fastq_outdir = "/home/chris/transcriptome/fastq/trimmed/"

os.system("cutadapt -b %s -o %s/Sample_1_L001_trimmed.fastq %s/Sample_1_L001.fastq > %s/Sample_1_L001_trimmed.log" % (index_2, fastq_outdir, fastq_indir, fastq_outdir))
