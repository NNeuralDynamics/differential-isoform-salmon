# """this script is to test working of Salmon on BAM files"""
# # def salmon(ref):
#     """runs in two phases"""
#     # phase 1: use a ref genome for indexing
#     # build index on transcriptome
#     # bam files

import subprocess

def create_quant(transcriptome_fa,bam_file,salmon_quant):
    """this function is the get the index for the reference file
    Args: path to the transcriptome file
    Returns: the index of transcriptome"""
    subprocess.run(["salmon","quant",
                    "-t", transcriptome_fa,
                    "-l", "A",
                    "-a", bam_file,
                    "-o", salmon_quant])

create_quant(transcriptome_fa = '../REF/genome_gene.fa',
    bam_file = '../bispecific/BAM/D1killers.bam', 
    salmon_quant = '../salmon_test/salmon_quant')

# def main():
#     create_index(transcriptome_fa='../REF/genome_gene.fa',index_dir="../salmon_output_files",salmon_index="../salmon_output_files/salmon_index")

# if __name__ == "__main__":
#     main()

