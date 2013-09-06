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

# Sample 1
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_1_L001_trimmed.fastq %s/Sample_1_L001.fastq > %s/Sample_1_L001_trimmed.log" % (index_2, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_1_L002_trimmed.fastq %s/Sample_1_L002.fastq > %s/Sample_1_L002_trimmed.log" % (index_2, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 2
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_2_L001_trimmed.fastq %s/Sample_2_L001.fastq > %s/Sample_2_L001_trimmed.log" % (index_4, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_2_L002_trimmed.fastq %s/Sample_2_L002.fastq > %s/Sample_2_L002_trimmed.log" % (index_4, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 3
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_3_L001_trimmed.fastq %s/Sample_3_L001.fastq > %s/Sample_3_L001_trimmed.log" % (index_5, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_3_L002_trimmed.fastq %s/Sample_3_L002.fastq > %s/Sample_3_L002_trimmed.log" % (index_5, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 4
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_4_L001_trimmed.fastq %s/Sample_4_L001.fastq > %s/Sample_4_L001_trimmed.log" % (index_6, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_4_L002_trimmed.fastq %s/Sample_4_L002.fastq > %s/Sample_4_L002_trimmed.log" % (index_6, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 5
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_5_L001_trimmed.fastq %s/Sample_5_L001.fastq > %s/Sample_5_L001_trimmed.log" % (index_7, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_5_L002_trimmed.fastq %s/Sample_5_L002.fastq > %s/Sample_5_L002_trimmed.log" % (index_7, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 6
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_6_L001_trimmed.fastq %s/Sample_6_L001.fastq > %s/Sample_6_L001_trimmed.log" % (index_12, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_6_L002_trimmed.fastq %s/Sample_6_L002.fastq > %s/Sample_6_L002_trimmed.log" % (index_12, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 7
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_7_L001_trimmed.fastq %s/Sample_7_L001.fastq > %s/Sample_7_L001_trimmed.log" % (index_1, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_7_L002_trimmed.fastq %s/Sample_7_L002.fastq > %s/Sample_7_L002_trimmed.log" % (index_1, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 8
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_8_L001_trimmed.fastq %s/Sample_8_L001.fastq > %s/Sample_8_L001_trimmed.log" % (index_3, fastq_outdir, fastq_indir, fastq_outdir))
os.system("cutadapt -m 20 -q 20 -b %s -o %s/Sample_8_L002_trimmed.fastq %s/Sample_8_L002.fastq > %s/Sample_8_L002_trimmed.log" % (index_3, fastq_outdir, fastq_indir, fastq_outdir))