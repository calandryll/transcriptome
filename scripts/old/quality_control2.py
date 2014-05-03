#!/usr/bin/python -tt
# Updated version of clipping adapters from sequences
# Used fastx_clipper on combined sequences to examine differen between that and cutadapt
# Website: https://code.google.com/p/cutadapt/
# Updated on: 09/26/2013

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/original/"
output_dir = "/home/chris/transcriptome/fastq/qc/"
reports_dir = "/home/chris/transcriptome/reports/"

adapters = ["GATCGGAAGAGCACACGTCTGAACTCCAGTCACCGATGTATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTGACCAATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACGCCAATATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCAGATCATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACCTTGTAATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACATCACGATCTCGTATGCCGTCTTCTGCTTG", "GATCGGAAGAGCACACGTCTGAACTCCAGTCACTTAGGCATCTCGTATGCCGTCTTCTGCTTG"]

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

	if fastq_orig[files] == "Control_1.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[0], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Control_2.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[1], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Control_3.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[2], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Control_4.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[3], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Treat_1.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[4], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Treat_2.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[5], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Treat_3.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[6], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	elif fastq_orig[files] == "Treat_4.fastq":
		os.system("fastx_clipper -v -Q 32 -a %s -l 51 -i %s -o %s > %s" % (adapters[7], fastqfile_in, fastq_tmp, log_out))
		print "Removing first 13 bases from %s..." % (fastq_orig[files])
		os.system("fastx_trimmer -v -Q 32 -f 13 -i %s -o %s >> %s" % (fastq_tmp, fastq_out, log_out))
		os.system("rm %s" % (fastq_tmp))
	else:
		print "No files found..."



