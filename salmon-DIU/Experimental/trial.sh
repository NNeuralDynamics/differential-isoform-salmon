#!/bin/bash

# module load
module load star/2.7.11a

# Input files
forward="/work/talisman/sthakur/bispecific/FASTQ/D1killers_1.fq"  # change
reverse="/work/talisman/sthakur/bispecific/FASTQ/D1killers_2.fq"  # change

# Output directory
output_directory="/work/talisman/sthakur/dummy"  # change

# index directory
genome_dir="/work/talisman/sthakur/index"

# config file
config_file="config.json"

# path to gtf
gtf_file="/work/talisman/sthakur/bispecific/REF/genome.gtf"

# Run STAR alignment
STAR \
--genomeDir $genome_dir \
--readFilesIn $forward $reverse \
--runThreadN 32 \
--twopassMode Basic \
--alignEndsType Local \
--alignSJoverhangMin 5 \
--alignSJDBoverhangMin 1 \
--outFilterMismatchNmax 4 \
--alignIntronMin 20 \
--alignIntronMax 1000000 \
--outFilterType BySJout \
--outSAMtype BAM SortedByCoordinate \
--outFileNamePrefix $output_directory \
--outSAMattributes All \
--sjdbGTFfile $gtf_file \
--outSAMstrandField intronMotif    

#message
echo "STAR Run completed"