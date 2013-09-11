#!/usr/bin/python -tt
# Can't do this with bash why not python!
# Remove poly-a and poly-t from shortened samples
# Uses cutadapt to remove adaptors
# Website: https://code.google.com/p/cutadapt/

# Import OS features to run external programs
import os
import glob

v = "Version 0.1"
# Versions:
#	0.1 - Simple script to run cutadapt on all of the files

# Adapter listing
polya = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
polyt = "TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"

fastq_indir = "/home/chris/transcriptome/fastq/shorten"
fastq_outdir = "/home/chris/transcriptome/fastq/poly_any"

# keep a minimum length of 20 and quality score of 20 (probably redundant), remove poly-a and t sequences. Times = 2 should do both poly-a and t
# modified -a (3' cutting) to -b (anywhere)

# Sample 1
print "Analyzing Sample 1..."
os.system("cutadapt -m 20 -q 20 -b %s -b %s --times=2 -o %s/Sample_1_L001_poly_any.fastq %s/Sample_1_L001_shorten.fastq > %s/Sample_1_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 1..."
os.system("cutadapt -m 20 -q 20 -b %s -b %s --times=2 -o %s/Sample_1_L002_poly_any.fastq %s/Sample_1_L002_shorten.fastq > %s/Sample_1_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 2
print "Analyzing Sample 2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_2_L001_poly_any.fastq %s/Sample_2_L001_shorten.fastq > %s/Sample_2_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 2_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_2_L002_poly_any.fastq %s/Sample_2_L002_shorten.fastq > %s/Sample_2_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 3
print "Analyzing Sample 3..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_3_L001_poly_any.fastq %s/Sample_3_L001_shorten.fastq > %s/Sample_3_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 3_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_3_L002_poly_any.fastq %s/Sample_3_L002_shorten.fastq > %s/Sample_3_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 4
print "Analyzing Sample 4..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_4_L001_poly_any.fastq %s/Sample_4_L001_shorten.fastq > %s/Sample_4_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 4_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_4_L002_poly_any.fastq %s/Sample_4_L002_shorten.fastq > %s/Sample_4_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 5
print "Analyzing Sample 5..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_5_L001_poly_any.fastq %s/Sample_5_L001_shorten.fastq > %s/Sample_5_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 5_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_5_L002_poly_any.fastq %s/Sample_5_L002_shorten.fastq > %s/Sample_5_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 6
print "Analyzing Sample 6..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_6_L001_poly_any.fastq %s/Sample_6_L001_shorten.fastq > %s/Sample_6_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 6_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_6_L002_poly_any.fastq %s/Sample_6_L002_shorten.fastq > %s/Sample_6_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 7
print "Analyzing Sample 7..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_7_L001_poly_any.fastq %s/Sample_7_L001_shorten.fastq > %s/Sample_7_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 7_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_7_L002_poly_any.fastq %s/Sample_7_L002_shorten.fastq > %s/Sample_7_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))

# Sample 8
print "Analyzing Sample 8..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_8_L001_poly_any.fastq %s/Sample_8_L001_shorten.fastq > %s/Sample_8_L001_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
print "Analyzing Sample 8_2..."
os.system("cutadapt -m 20 -q 20  -b %s -b %s  --times=2 -o %s/Sample_8_L002_poly_any.fastq %s/Sample_8_L002_shorten.fastq > %s/Sample_8_L002_poly_any.log" % (polya, polyt, fastq_outdir, fastq_indir, fastq_outdir))
