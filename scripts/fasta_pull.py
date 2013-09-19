#!/usr/bin/python -tt
# Pulls out sequences with organismal name (based on CAMERA Microbial Eukaryotic Transcriptome)
# Any inputs with - or -- are optional and will default to certain values.
# Written by: Christopher R. Main, University of Delaware
# Last Updated: 09/19/2013

# Versions:
#	0.1 - Open fasta file correctly
#	0.2 - Pull record names and parse them
#	0.3 - Print out cluster range that is wanted
#	0.4 - Write wanted sequences to file
#	0.5 - Comestic interactions
#	0.6 - Changes to argument handling

# Allow opening of FASTA file
from Bio import SeqIO

# Ready arguments from the commandline
import argparse

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='Version 0.6')
parser.add_argument("filename", help="location of FASTA file")
parser.add_argument("out_file", help="filename for output of BLAST search results")
parser.add_argument("strain", help="Strain of Heterosigma")
args = parser.parse_args()

print "Loading %s to memory..." % (args.filename)
handle = open(args.filename, "rU")

# Parse the data file
fasta_parse = list(SeqIO.parse(handle, "fasta"))

# Use taxon ID instead 
# Heterosigma = 536047

taxon = "536047"

# Search FASTA file with tab delimited file
print "Searching %s for Heterosigma..." % (args.filename)	

# 2 will give you taxon ID, 6 will give you the Strain Name (Based on CAMERA fasta)
records = (r for r in fasta_parse if taxon in r.description.split()[2])
print "Searching for %s..." % (args.strain)
strain = (r for r in records if args.strain in r.description.split()[6])
count = SeqIO.write(strain, args.out_file, "fasta")
print "Saved %i records to %s" % (count, args.out_file)

# Begin for loop to write several files
# for i in range(len_file):
	#Write
	# output_handle = open(args.out_file + i, "w")
	#Write sequences to file
	# for i in range(int(args.first), int(args.last) + 1):
		# SeqIO.write(records[i], output_handle, "fasta")
		# print "Writing %s to file" % (records[i].id)
	# output_handle.close()
	# print "Writing of %s complete, closing file..." % (args.out_file)

handle.close()