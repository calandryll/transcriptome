#!/usr/bin/python -tt
# Updated version of clipping adapters from sequences
# Used cutadapt on combined sequences and removes first 13 bases with fastx_clipper
# Website: https://code.google.com/p/cutadapt/
# Updated on: 09/26/2013

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/original/"
output_dir = "/home/chris/transcriptome/fastq/qc/"
reports_dir = "/home/chris/transcriptome/reports/"

# Adapter listing
index_2 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCGATGTATCTCGTATGCCGTCTTCTGCTTG"	# Sample 1 (Control 1)
index_4 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTGACCAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 2 (Control 2)
index_5 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 3 (Control 3)
index_6 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACGCCAATATCTCGTATGCCGTCTTCTGCTTG"	# Sample 4 (Control 4)
index_7 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATCATCTCGTATGCCGTCTTCTGCTTG"	# Sample 5 (Treat 1)
index_12 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCTTGTAATCTCGTATGCCGTCTTCTGCTTG"	# Sample 6 (Treat 2)
index_1 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG"	# Sample 7 (Treat 3)
index_3 = "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTTAGGCATCTCGTATGCCGTCTTCTGCTTG"	# Sample 8 (Treat 4)

fastq_orig = sorted(glob.glob1(input_dir, "*.fastq"))
orig = len(list(fastq_orig))

print "Input Directory: %s" % (input_dir)
print "Output Directory: %s" % (output_dir)
print "Scanning Input Directory..."
print "Found %s fastq files..." % (orig)
print "Fastq files: %s" % (fastq_orig)

for files in range(orig):
	print "Analyzing %s..." % (fastq_orig[files])
	fastqfile_in = input_dir + fastq_orig[files]

	# Remove adapters from sequences and keep score above 30, with a min length of 51
	# Any other sequences will be discarded.  This may be modified in future to see what the impact
	# of removal of lower sequences yields.

	fastq_tmp = output_dir + fastq_orig[files] + '_temp.fastq'
	log_out = output_dir + "logs/" + fastq_orig[files] + '.log'
	fastq_out = output_dir + fastq_orig[files]
	print "Cleaning %s..." % (fastq_orig[files])
	# -m min-len of 51, -q min quality of 30, -a [adapters], -o output input > [log]
	os.system("cutadapt -m 51 -q 30 -a %s -a %s -a %s -a %s -a %s -a %s -a %s -a %s -o %s %s > %s" % (index_2, index_4, index_5, index_6, index_7, index_12, index_1, index_3, fastq_tmp, fastqfile_in, log_out))
	print "Removing first 13 bases from %s..." % (fastq_orig[files])
	os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
	os.system("rm %s" % (fastq_tmp))
