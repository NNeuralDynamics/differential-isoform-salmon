import json
import subprocess
from pathlib import Path

def run_star(forward, reverse, output_directory, config_file, genome_dir):
    with open('config.json') as conf:
        config = json.load(conf)
    print("hi")    
    
    # Access STAR configuration
    star_config = config.get('STAR', {})
    outSAMtype_args = star_config.get("outSAMtype", ["BAM", "SortedByCoordinate"])
    outSAMtype_args = outSAMtype_args if isinstance(outSAMtype_args, list) else [outSAMtype_args]
    outSAMattributes = star_config.get("outSAMattributes", "NH HI AS NM MD").split()
    
    print("star run")
    
    star_command = [
        "STAR",
        "--readFilesIn", forward, reverse,
        "--genomeDir", genome_dir,
        "--readFilesCommand", star_config.get("readFilesCommand", "zcat"),
        "--runThreadN", str(star_config.get("runThreadN", 32)),
        "--twopassMode", star_config.get("twopassMode", "Basic"),
        "--alignEndsType", star_config.get("alignEndsType", "EndToEnd"),
        "--alignSJoverhangMin", str(star_config.get("alignSJoverhangMin", 8)),
        "--alignSJDBoverhangMin", str(star_config.get("alignSJDBoverhangMin", 1)),
        "--outFilterMismatchNmax", str(star_config.get("outFilterMismatchNmax", 4)),
        "--alignIntronMin", str(star_config.get("alignIntronMin", 20)),
        "--alignIntronMax", str(star_config.get("alignIntronMax", 1000000)),
        "--outFilterType", star_config.get("outFilterType", "BySJout"),
        "--outSAMtype", *outSAMtype_args,
        "--outFileNamePrefix", output_directory,
        "--outSAMattributes", *outSAMattributes,
        "--sjdbGTFfile", "work/talisman/sthakur/bispecific/REF/genome.gtf",
        "--outSAMstrandField", star_config.get("outSAMstrandField", "intronMotif")
    ]
    
    # Run STAR alignment
    subprocess.run(star_command, shell=True, check=True)
    
    print("star run end")
    
    

# for D1 killers
forward = "/work/talisman/sthakur/bispecific/FASTQ/D1killers_1.fq"
reverse = "/work/talisman/sthakur/bispecific/FASTQ/D1killers_2.fq"
output_directory = "/work/talisman/sthakur/star_output/D1_killers"
config_file = "/work/talisman/sthakur/config.json"  
genome_dir = "/work/talisman/sthakur/index"


run_star(forward, reverse, output_directory, config_file, genome_dir)