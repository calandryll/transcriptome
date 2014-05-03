#!/usr/bin/python -tt
# Run assemble genes and transcripts for each sample
# Website: http://cufflinks.cbcb.umd.edu/

# Import OS features to run external programs
import os
import glob

# Directories for input and output
input_dir = "/home/chris/transcriptome/fastq/align"
output_dir = "/home/chris/transcriptome/fastq/assemble"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"

#input_dir = "/home/chris/transcriptome/fastq/vchl/align"
#output_dir = "/home/chris/transcriptome/fastq/vchl/assemble"
#reference = "/home/chris/transcriptome/fastq/reference/V_chl"

ha_gff = reference + ".gff3"

#print "Raw Directory: %s\n" % (fastq_raw)
print "Directory: %s\n" % (input_dir)
print "Scanning Directory..."

# Pull files from directory
fastq_files = sorted(glob.glob(input_dir + "/*/accepted_hits.bam"))
fastq_dir = sorted(glob.glob(input_dir + "/*"))

trim = len(list(fastq_files))
for files in range(trim):
	#print fastq_files[files]
	sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
	dir_name = os.path.splitext(os.path.basename(fastq_dir[files]))[0]
	print "Analyzing %s..." % (dir_name)
	
	samdir = output_dir + "/" + dir_name
	#print samdir
	
	# Create directory for output
	os.system("mkdir %s" % (samdir))

	# Run tophat using H_akashiwo index
	# -p 4 threads
	# try -G
	os.system("cufflinks -p 4 -o %s %s " % (samdir, fastq_files[files]))
