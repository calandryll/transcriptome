#!/usr/bin/python -tt
# Run all of the steps in a single script
# Update on: 

# Import OS features to run external programs
import os
import glob

qc_dir = "/home/chris/transcriptome/fastq/qc"
align_dir = "/home/chris/transcriptome/fastq/align"
reference = "/home/chris/transcriptome/fastq/reference/H_akashiwo"
assem_dir = "/home/chris/transcriptome/fastq/assemble"
merge_dir = "/home/chris/transcriptome/fastq/merged"
merged = "/home/chris/transcriptome/fastq/merged/merged.gtf"
ha_gff = reference + ".gff3"

def ref_align():
	# Directories for input and output
	
	#print "Raw Directory: %s\n" % (fastq_raw)
	print "Directory: %s\n" % (qc_dir)
	#print "Using %s as a reference..." % (ha_gff)
	print "Scanning Directory..."

	# Pull files from directory
	fastq_files = sorted(glob.glob(qc_dir + "/*.fastq"))

	trim = len(list(fastq_files))
	for files in range(trim):
		#print fastq_files[files]
		sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
		print "Analyzing %s..." % (sample_name)
		#print sample_name
		samdir = align_dir + "/" + sample_name
		#print samdir
		#print fastq_files[files]	

		# Create directory for output
		os.system("mkdir %s" % (samdir))

		# run tophat using H_akashiwo index
		# -p 4 threads
		os.system("tophat -p 4 -o %s %s %s" % (samdir, reference, fastq_files[files]))

def assemble():
	#print "Raw Directory: %s\n" % (fastq_raw)
	print "Directory: %s\n" % (align_dir)
	print "Scanning Directory..."

	# Pull files from directory
	fastq_files = sorted(glob.glob(align_dir + "/*/accepted_hits.bam"))
	fastq_dir = sorted(glob.glob(align_dir + "/*"))

	trim = len(list(fastq_files))
	for files in range(trim):
		#print fastq_files[files]
		sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
		dir_name = os.path.splitext(os.path.basename(fastq_dir[files]))[0]
		print "Analyzing %s..." % (dir_name)
		
		samdir = assem_dir + "/" + dir_name
		#print samdir
		
		# Create directory for output
		os.system("mkdir %s" % (samdir))

		# Run tophat using H_akashiwo index
		# -p 4 threads
		# try -G
		os.system("cufflinks -p 4 -o %s %s " % (samdir, fastq_files[files]))

def merge():
	os.system("cuffmerge -o %s %s/gtf.txt" % (merge_dir, assem_dir))

#def diff():
#	control_lane = input_dir + "/controls"
#	treat_lane = input_dir + "/treat"

#	print control_lane
#	print treat_lane
#	os.system("cuffdiff --max-bundle-frags 2000000 -p 4 -L Control,Vibrio -o %s %s %s/control_2.bam,%s/control_3.bam,%s/control_4.bam %s/treat_1.bam,%s/treat_2.bam,%s/treat_3.bam" % (output_dir, merged, control_lane, control_lane, control_lane, treat_lane, treat_lane, treat_lane))
# Hey idiot double check that shit!
# Removed treat_4.bam - maybe a bit off
# HIDATA means too many fragments, will add --max-bundle-frags 2000000
ref_align()
assemble()
merge()