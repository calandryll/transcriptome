#!/usr/bin/python -tt
# Run tophat on each sample and compare to the reference genome H_akashiwo.fa (Originally High_exp.fasta)
# Website: http://tophat.cbcb.umd.edu/
# Update on: 09/27/2013

# Import OS features to run external programs
import os
import glob

# Directories for input and output
#input_dir = "/home/chris/transcriptome/fastq/qc"
#output_dir = "/home/chris/transcriptome/fastq/align"
#reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"

input_dir = "/home/chris/transcriptome/fastq/qc"
output_dir = "/home/chris/transcriptome/fastq/align"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"

ha_gff = reference + ".gff3"


#print "Raw Directory: %s\n" % (fastq_raw)
print "Directory: %s\n" % (input_dir)
#print "Using %s as a reference..." % (ha_gff)
print "Scanning Directory..."

# Pull files from directory
fastq_files = sorted(glob.glob(input_dir + "/*.fastq"))

trim = len(list(fastq_files))
for files in range(trim):
	#print fastq_files[files]
	sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
	print "Analyzing %s..." % (sample_name)
	#print sample_name
	samdir = output_dir + "/" + sample_name
	#print samdir
	#print fastq_files[files]	

	# Create directory for output
	os.system("mkdir %s" % (samdir))

	# Run tophat using H_akashiwo index
	# -p 4 threads
	
	os.system("tophat -p 4 -o %s %s %s" % (samdir, reference, fastq_files[files]))
