#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Removes basepairs below a certain threshold, based on Phred score
# Uses cutadapt to remove basepairs that are low quality and remove sequences that are less that 20 bp


# Import OS features to run external programs
import os
import glob

v = "Version 0.3"
# Versions:
#	0.1 - Read in files for directory
#	0.2 - Export and run cutadapt
#	0.3 - Get all of it working properly
#	0.4 - 
#	0.5 - 
#	0.6 - 

print "Quality trimmer %s\n" % (v)

fastq_indir = "/home/chris/transcriptome/fastq/original/"
fastq_outdir = "/home/chris/transcriptome/fastq/trimmed/"

print "Input Directory: %s\n" % (fastq_indir)
print "Output Directory: %s\n" % (fastq_outdir)
print "Scanning Input Directory..."
fastq_raw = glob.glob1(fastq_indir, "*.fastq")
#fastq_raw = glob.glob1(fastq_indir, "Sample_1_L001.fastq")
raw = len(list(fastq_raw))
for files in range(raw):
	print fastq_raw[files]
	fastqfile_in = fastq_indir + fastq_raw[files]

	# Quality control for Phred score of 20
	fastq_20 = fastq_outdir + fastq_raw[files] + '_20.fastq'
	log_20 = fastq_outdir + fastq_raw[files] + '_20.log'
	os.system("cutadapt -m 20 -q 20 -o %s %s > %s" % (fastq_20, fastqfile_in, log_20))

	# Quality control for a Phred score of 30
	fastq_30 = fastq_outdir + fastq_raw[files] + '_30.fastq'
	log_30 = fastq_outdir + fastq_raw[files] + '_30.log'
	os.system("cutadapt -m 30 -q 30 -o %s %s > %s" % (fastq_30, fastqfile_in, log_30))


