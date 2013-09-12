#!/usr/bin/python -tt
# Run tophat on each sample and compare to the reference genome H_akashiwo.fa (Originally High_exp.fasta)
# Website: http://tophat.cbcb.umd.edu/

# Import OS features to run external programs
import os
import glob
import fnmatch

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/poly"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
output_dir = "/home/chris/transcriptome/fastq/align"

# Setup directories to the data
#fastq_raw = "/home/chris/transcriptome/fastq/original/"
#fastq_trimmed = "/home/chris/transcriptome/fastq/poly/"
#fastq_routput = "/home/chris/transcriptome/fastq/reports/raw"
#fastq_toutput = "/home/chris/transcriptome/fastq/reports/poly/"

#print "Raw Directory: %s\n" % (fastq_raw)
print "Directory: %s\n" % (input_dir)
print "Scanning Directory..."

# Pull file names from raw
#fastq_files = sorted(glob.glob(input_dir + "/*/*.fastq"))
#print fastq_files
#fastq_names = sorted(glob.glob1(fastq_files, "*.fastq"))
#print fastq_names

for r,d,f in os.walk(input_dir):
    for files in f:
        if files.endswith(".fastq"):
             print files


#trim = len(list(fastq_files))
#for files in range(trim):
	#print fastq_files[files]
	#print os.path.splitext(fastq_files[files])[0]
	#tophat_run = input_dir + fastq_files[files]
	
	# Run fastqc
	#os.system("fastqc -o %s %s" % (fastq_toutput, fastqc_trun))
	# Run tophat with 4 threads, should be slightly faster than the default 1 thread
	#os.system("tophat -p 4 -o %s/lane 1/Sample_1 %s %s" % (output_dir, reference, input_dir))
