#!/usr/bin/python -tt
# Run Trimmomatic to remove Illumina adapter sequences
# Update on: 043014

# Import OS to run external programs
import os
import glob

orig_dir = "/home/chris/transcriptome/fastq/original"
qc_outdir = "/home/chris/transcriptome/fastq/qc"
adapters = "/home/chris/transcriptome/fastq/adapters.fasta"


print "Scanning directory %s..." % (orig_dir)
# Pull in files
fastq_files = sorted(glob.glob(orig_dir + "/*.fastq"))

trim = len(list(fastq_files))

for files in range(trim):
	sample_name = os.path.splitext(os.path.basename(fastq_files[files]))[0]
	print "Analyzing %s..." % (sample_name)
	#samdir = orig_dir + "/" + fastq_files[files]
	outdir = qc_outdir + "/" + sample_name + "_trimmed.fastq"
	# Remove Illumina Sequences and then keep any sequence that is longer than 35 bp
	os.system("java -jar /home/chris/transcriptome/programs/trimmomatic-0.32.jar SE %s %s ILLUMINACLIP:%s:2:30:10 MINLEN:35" % (fastq_files[files], outdir, adapters))
