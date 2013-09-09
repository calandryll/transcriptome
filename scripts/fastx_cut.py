#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses fastx_clipper to remove adaptors
# Website: https://code.google.com/p/fastx_clipper/

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run fastx_clipper on all of the files

# Adapter listing
index_2 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCGATGTATCTCGTATGCCGTCTTCTGCTTG"	# Sample 1
index_4 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTGACCAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 2
index_5 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 3
index_6 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACGCCAATATCTCGTATGCCGTCTTCTGCTTG"	# Sample 4
index_7 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATCATCTCGTATGCCGTCTTCTGCTTG" # Sample 5
index_12 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCTTGTAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 6
index_1 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 7
index_3 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTTAGGCATCTCGTATGCCGTCTTCTGCTTG"	# Sample 8

# Clipped means removal of adaptor
fastq_indir = "/home/chris/transcriptome/fastq/original/"
fastq_outdir = "/home/chris/transcriptome/fastq/fastx/clipped/"

# fastx_clipper -v -i BC54.fa -a CTGTAGGCACCATCAATTCGTA -o BC54.clipped.fa
# -v = verbose, -a = adaptor, -i = input file, -o = output file

# Sample 1
print "Analyzing Sample 1..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_1_L001_clipped.fastq -i %s/Sample_1_L001.fastq > %s/Sample_1_L001_clipped.log" % (index_2, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_1_L002_clipped.fastq -i %s/Sample_1_L002.fastq > %s/Sample_1_L002_clipped.log" % (index_2, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 2
print "Analyzing Sample 2..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_2_L001_clipped.fastq -i %s/Sample_2_L001.fastq > %s/Sample_2_L001_clipped.log" % (index_4, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_2_L002_clipped.fastq -i %s/Sample_2_L002.fastq > %s/Sample_2_L002_clipped.log" % (index_4, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 3
print "Analyzing Sample 3..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_3_L001_clipped.fastq -i %s/Sample_3_L001.fastq > %s/Sample_3_L001_clipped.log" % (index_5, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_3_L002_clipped.fastq -i %s/Sample_3_L002.fastq > %s/Sample_3_L002_clipped.log" % (index_5, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 4
print "Analyzing Sample 4..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_4_L001_clipped.fastq -i %s/Sample_4_L001.fastq > %s/Sample_4_L001_clipped.log" % (index_6, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_4_L002_clipped.fastq -i %s/Sample_4_L002.fastq > %s/Sample_4_L002_clipped.log" % (index_6, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 5
print "Analyzing Sample 5..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_5_L001_clipped.fastq -i %s/Sample_5_L001.fastq > %s/Sample_5_L001_clipped.log" % (index_7, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_5_L002_clipped.fastq -i %s/Sample_5_L002.fastq > %s/Sample_5_L002_clipped.log" % (index_7, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 6
print "Analyzing Sample 6..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_6_L001_clipped.fastq -i %s/Sample_6_L001.fastq > %s/Sample_6_L001_clipped.log" % (index_12, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_6_L002_clipped.fastq -i %s/Sample_6_L002.fastq > %s/Sample_6_L002_clipped.log" % (index_12, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 7
print "Analyzing Sample 7..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_7_L001_clipped.fastq -i %s/Sample_7_L001.fastq > %s/Sample_7_L001_clipped.log" % (index_1, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_7_L002_clipped.fastq -i %s/Sample_7_L002.fastq > %s/Sample_7_L002_clipped.log" % (index_1, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 8
print "Analyzing Sample 8..."
os.system("fastx_clipper -v  -a %s -o %s/Sample_8_L001_clipped.fastq -i %s/Sample_8_L001.fastq > %s/Sample_8_L001_clipped.log" % (index_3, fastq_outdir, fastq_indir, fastq_outdir))
os.system("fastx_clipper -v  -a %s -o %s/Sample_8_L002_clipped.fastq -i %s/Sample_8_L002.fastq > %s/Sample_8_L002_clipped.log" % (index_3, fastq_outdir, fastq_indir, fastq_outdir))