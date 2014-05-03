#!/usr/bin/python -tt
# Automated BLAST search of a FASTA file. Search defaults to blastx (Protein) search,
# blast type, database, e-value threshold and number of hits can be changed with 
# commandline inputs.
# Any inputs with - or -- are optional and will default to certain values.
# Blast will be done locally for quicker responses
# Written by: Christopher R. Main, University of Delaware
# Last Updated: 09/26/13

# Versions:
#	0.1 - Open Cluster file and begin searching internet blast
#	0.2 - Search and send output to screen of top result
#	0.3 - Output BLAST results with GI, Length, E-Value, Query Start, Subject Start, Score and Bits
#	0.4 - Setup of for loop to run multiple queries, and output to separate files
#	0.5 - Append data to the file with added sequence name to first column
#	0.6 - Change way of doing inputs
#	Future versions:
#	0.7 - Write for local database search, for use on BioHen

# Allow manipulating of FASTA file
from Bio import SeqIO
# Allows for internet blast search
from Bio.Blast.Applications import NcbiblastxCommandline
# Parsing of BLAST results
from Bio.Blast import NCBIXML

# Ready arguments from the commandline
import argparse

# Read and parse the arguments from the command line
parser =  argparse.ArgumentParser()
parser.add_argument("-v", "--version", action="version", version='Version 0.6')
parser.add_argument("filename", help="location of FASTA file")
#parser.add_argument("out_file", help="filename for output of BLAST search results")
parser.add_argument("-b", "--blast", help="what type of blast to use (Defaults to blastx)", default='blastx')
parser.add_argument("-t", "--thres", help="e-value threshold, ignores any numbers above this number (Defaults to 0.005)", type=int, default=0.005)
parser.add_argument("-hl", "--hitlist", help="how many alignments do you want parsed into the file (Defaults to 10)", default=10)
parser.add_argument("-d", "--database", help="what database to search against (nr or swissprot) (Defaults to nr)", default='nr')
args = parser.parse_args()


# Open file
handle = open(args.filename, "rU")

# BLAST first sequence of file
records = list(SeqIO.parse(handle, format="fasta"))
print args.blast
print args.database
print args.thres
print "Blasting %s..." % (records[0].id)
blarg = NcbiblastxCommandline(query = records[0].seq, db = args.database, evalue = args.thres, out = 'blarg.xml')
print blarg
stdout, stderr = blarg()

# Take Search and output to file
#blast_records = NCBIXML.parse(blarg)
#print blast_records

#wfile.close()
#print "Writing of %s complete, closing file..." % (args.out_file)
