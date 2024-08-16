#!/bin/bash

# D1 killers and untr_killers
D1_bam="/work/talisman/sthakur/star_output/D2_nonkillers/Aligned.sortedByCoord.out.bam"  #change
Untr_bam="/work/talisman/sthakur/star_output/Untr_nonkillers/Aligned.sortedByCoord.out.bam" # change

# output file
mkdir -p /work/talisman/sthakur/rmat_output/Combined_Analysis/D2_Untr_nokill
mkdir -p /work/talisman/sthakur/rmat_output/Combined_Analysis/D2_Untr_nokill/rmats


b1_file="/work/talisman/sthakur/rmat_output/Combined_Analysis/D2_Untr_nokill/rmats/b1.txt"  #Change
b2_file="/work/talisman/sthakur/rmat_output/Combined_Analysis/D2_Untr_nokill/rmats/b2.txt"  #Change

# bam to txt
echo "$D1_bam" > "$b1_file"
echo "$Untr_bam" > "$b2_file"

#comment
echo "bam to txt - executed"


# index directory
genome_dir="/work/talisman/sthakur/index"
# path to gtf
gtf_file="/work/talisman/sthakur/bispecific/REF/genome.gtf" #Change
# Output directory
output_directory="/work/talisman/sthakur/rmat_output/Combined_Analysis/D2_Untr_nokill/rmats" #Change

#comment
echo "Starting rmats run"

#rmats
python /work/talisman/sthakur/rmats-turbo/rmats.py \
--b1 $b1_file \
--b2 $b2_file \
--gtf $gtf_file \
--od "$output_directory/post" \
--tmp "$output_directory/prep" \
--nthread 32 \
--readLength 100 \
--libType fr-firststrand \
--variable-read-length \
--allow-clipping \
-t paired


#comment
echo "rmats run end"