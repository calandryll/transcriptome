#!/bin/bash
# Removes basepairs below a certain threshold, based on Phred score
# Uses cutadapt to remove basepairs that are 

# Usage:
# quality_trimmer.sh [original file] [name of trimmed file]


FASTQ_IDIR=~/transcriptome/fastq/original
FASTQ_ODIR=~/transcriptome/fastq/trimmed

find $FASTQ_IDIR -name "Sample_1_L001.fastq" -print0 | xargs -0 -I basename | xargs -0 -I file cutadapt -m 20 -q 20 -o $FASTQ_ODIR/file_20 file > $FASTQ_ODIR/file_20.log


#cutadapt -m 20 -q 20 -o $FASTQ_ODIR/${2}_20.fastq $1 > $FASTQ_ODIR/${2}_20.log
#cutadapt -m 20 -q 30 -o $FASTQ_ODIR/${2}_30.fastq $1 > $FASTQ_ODIR/${2}_30.log
