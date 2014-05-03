#!/usr/bin/python -tt
# Updated version of clipping adapters from sequences
# Used cutadapt on combined sequences and removes first 13 bases with fastx_clipper
# Website: https://code.google.com/p/cutadapt/
# Updated on: 09/26/2013

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/qc/fastx/"
output_dir = "/home/chris/transcriptome/fastq/qc/fastx/"


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
	sample_name = os.path.splitext(os.path.basename(fastq_orig[files]))[0]
	# Remove adapters from sequences and keep score above 30, with a min length of 51
	# Any other sequences will be discarded.  This may be modified in future to see what the impact
	# of removal of lower sequences yields.

	fastq_tmp = output_dir + fastq_orig[files] + '_temp.fastq'
	log_out = output_dir + "logs/" + fastq_orig[files] + '.log'
	fastq_out = output_dir + sample_name + "_filtered.fastq"
	print "Running quality filter of 20 score, 100%..."
	os.system("fastq_quality_filter -v -Q 32 -q 20 -p 100 -i %s -o %s >> %s" % (fastqfile_in, fastq_tmp, log_out))
	print "Removing artifacts..."
	os.system("fastx_artifacts_filter -v -Q 32 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
	os.system("rm %s" % (fastq_tmp))
