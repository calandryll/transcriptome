#!/bin/bash
# Count the number of sequences in each fastq file
# Grep from RNA Abundance Analysis (pg 210)

FASTQ_DIR=~/transcriptome/fastq/

grep -rc -P "^\@[\w:-]+?\:\w+?\s[12]\:.+" $FASTQ_DIR > sequence_count.txt
grep -rc -P "^\+([\w:-]+?\:\w+?\s[12]\:.+|\n)" $FASTQ_DIR > quality_lines.txt
