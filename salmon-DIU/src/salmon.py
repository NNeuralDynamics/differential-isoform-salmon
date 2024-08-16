import json
import subprocess
from pathlib import Path
import argparse


def get_cli_args():
    """Get args arguments
    Just get the command line options using argparse
    @return: Instance of argparse arguments
    """

    parser = argparse.ArgumentParser(description='Get the killers and non_killers')

    parser.add_argument('infile1',
                        type=str,
                        help='Provide a file name from FASTQ folder with name _1')
    parser.add_argument('outfile',
                        type=str,
                        help='Provide the name of Donor')
    return parser.parse_args()

def salmon_run(transcriptome,bam_files, output_directory):
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    salmon_command = [
        'salmon', 'quant',
        '-t', transcriptome,
        '-l', 'A',
        "-a", bam_files,
        "-o", output_directory
    ]
    subprocess.run(salmon_command, check=True, capture_output=True, text=True)
    print("salmon run completed")
    # try:
    #     result = subprocess.run(salmon_command, check=True, capture_output=True, text=True)
    #     print("salmon Run Output:", result.stdout)
    #     print("salmon Run Errors:", result.stderr)
    # except subprocess.CalledProcessError as e:
    #     print("salmon Run failed:", e.stderr)

    # print("salmon run completed")


def input():
    args = get_cli_args()
    bam_file = args.infile1
    output_f = args.outfile
    return bam_file, output_f

def main():
    bam_file,output_f = input()
    transcriptome_file = "/work/talisman/sthakur/genome_transcripts.fa"
    salmon_run(transcriptome=transcriptome_file,bam_files=bam_file,output_directory=output_f)

main()
