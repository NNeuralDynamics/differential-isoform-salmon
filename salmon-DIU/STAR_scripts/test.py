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
    parser.add_argument('infile2',
                        type=str,
                        help='Provide a file name from FASTQ folder with name _2')
    parser.add_argument('outfile',
                        type=str,
                        help='Provide the name of Donor')
    return parser.parse_args()

def input():
    args = get_cli_args()
    donor_name1 = args.infile1
    donor_name2 = args.infile2
    output_f = args.outfile
    return donor_name1, donor_name2, output_f



def output(donor_name1, donor_name2, output_f):
    forward = f"../bispecific/FASTQ/{donor_name1}.fq"
    reverse = f"../bispecific/FASTQ/{donor_name2}.fq"
    output_directory = f"../star_output/{output_f}"
    config_file = "../config.json"  
    genome_dir = "../index"
    print("All files read correctly")

def main():
    donor_name1,donor_name2,output_f = input()
    output(donor_name1=donor_name1,donor_name2=donor_name2,output_f=output_f)

main()
