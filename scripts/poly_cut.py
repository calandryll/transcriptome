#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Remove poly-a and poly-t from shortened samples
# Uses fastx_clipper to remove poly-a and poly-t
# Website: http://hannonlab.cshl.edu/fastx_toolkit/commandline.html#fastx_clipper_usage

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run fastx_clipper on all of the files

# Adapter listing
polya = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
polyt = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"

fastq_indir = "/home/chris/transcriptome/fastq/shorten"
fastq_outdir = "/home/chris/transcriptome/fastq/poly"

# keep a minimum length of 20 and quality score of 20 (probably redundant), remove poly-a and t sequences. Times = 2 should do both poly-a and t
# modified -a (3' cutting) to -b (anywhere)

# Sample 1
print "Analyzing Sample 1...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_1_L001_temp.fastq -i %s/Sample_1_L001_shorten.fastq > %s/Sample_1_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 1...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_1_L001_poly_any.fastq -i %s/Sample_1_L001_temp.fastq > %s/Sample_1_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_1_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 1_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_1_L002_temp.fastq -i %s/Sample_1_L002_shorten.fastq > %s/Sample_1_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 1...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_1_L002_poly_any.fastq -i %s/Sample_1_L002_temp.fastq > %s/Sample_1_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_1_L002_temp.fastq" % (fastq_outdir))

# Sample 2
print "Analyzing Sample 2...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_2_L001_temp.fastq -i %s/Sample_2_L001_shorten.fastq > %s/Sample_2_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 2...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_2_L001_poly_any.fastq -i %s/Sample_2_L001_temp.fastq > %s/Sample_2_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_2_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 2_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_2_L002_temp.fastq -i %s/Sample_2_L002_shorten.fastq > %s/Sample_2_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 2...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_2_L002_poly_any.fastq -i %s/Sample_2_L002_temp.fastq > %s/Sample_2_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_2_L002_temp.fastq" % (fastq_outdir))

# Sample 3
print "Analyzing Sample 3...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_3_L001_temp.fastq -i %s/Sample_3_L001_shorten.fastq > %s/Sample_3_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 3...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_3_L001_poly_any.fastq -i %s/Sample_3_L001_temp.fastq > %s/Sample_3_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_3_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 3_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_3_L002_temp.fastq -i %s/Sample_3_L002_shorten.fastq > %s/Sample_3_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 3...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_3_L002_poly_any.fastq -i %s/Sample_3_L002_temp.fastq > %s/Sample_3_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_3_L002_temp.fastq" % (fastq_outdir))

# Sample 4
print "Analyzing Sample 4...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_4_L001_temp.fastq -i %s/Sample_4_L001_shorten.fastq > %s/Sample_4_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 4...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_4_L001_poly_any.fastq -i %s/Sample_4_L001_temp.fastq > %s/Sample_4_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_4_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 4_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_4_L002_temp.fastq -i %s/Sample_4_L002_shorten.fastq > %s/Sample_4_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 4...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_4_L002_poly_any.fastq -i %s/Sample_4_L002_temp.fastq > %s/Sample_4_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_4_L002_temp.fastq" % (fastq_outdir))

# Sample 5
print "Analyzing Sample 5...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_5_L001_temp.fastq -i %s/Sample_5_L001_shorten.fastq > %s/Sample_5_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 5...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_5_L001_poly_any.fastq -i %s/Sample_5_L001_temp.fastq > %s/Sample_5_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_5_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 5_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_5_L002_temp.fastq -i %s/Sample_5_L002_shorten.fastq > %s/Sample_5_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 5...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_5_L002_poly_any.fastq -i %s/Sample_5_L002_temp.fastq > %s/Sample_5_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_5_L002_temp.fastq" % (fastq_outdir))

# Sample 6
print "Analyzing Sample 6...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_6_L001_temp.fastq -i %s/Sample_6_L001_shorten.fastq > %s/Sample_6_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 6...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_6_L001_poly_any.fastq -i %s/Sample_6_L001_temp.fastq > %s/Sample_6_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_6_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 6_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_6_L002_temp.fastq -i %s/Sample_6_L002_shorten.fastq > %s/Sample_6_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 6...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_6_L002_poly_any.fastq -i %s/Sample_6_L002_temp.fastq > %s/Sample_6_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_6_L002_temp.fastq" % (fastq_outdir))

# Sample 7
print "Analyzing Sample 7...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_7_L001_temp.fastq -i %s/Sample_7_L001_shorten.fastq > %s/Sample_7_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 7...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_7_L001_poly_any.fastq -i %s/Sample_7_L001_temp.fastq > %s/Sample_7_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_7_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 7_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_7_L002_temp.fastq -i %s/Sample_7_L002_shorten.fastq > %s/Sample_7_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 7...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_7_L002_poly_any.fastq -i %s/Sample_7_L002_temp.fastq > %s/Sample_7_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_7_L002_temp.fastq" % (fastq_outdir))

# Sample 8
print "Analyzing Sample 8...Removing poly-a..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_8_L001_temp.fastq -i %s/Sample_8_L001_shorten.fastq > %s/Sample_8_L001_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 8...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_8_L001_poly_any.fastq -i %s/Sample_8_L001_temp.fastq > %s/Sample_8_L001_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_8_L001_temp.fastq" % (fastq_outdir))
print "Analyzing Sample 8_2...Removing poly-a"
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_8_L002_temp.fastq -i %s/Sample_8_L002_shorten.fastq > %s/Sample_8_L002_temp.log" % (polya, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 8...Removing poly-t..."
os.system("fastx_clipper -v -Q 32 -l 20 -a %s -o %s/Sample_8_L002_poly_any.fastq -i %s/Sample_8_L002_temp.fastq > %s/Sample_8_L002_poly_any.log" % (polyt, fastq_outdir, fastq_outdir, fastq_outdir))
print "Removing temporary file..."
os.system("rm %s/Sample_8_L002_temp.fastq" % (fastq_outdir))
