import json
import subprocess
from pathlib import Path

def run_star(forward, reverse, output_directory, config_file, genome_dir):
    try:
        with open(config_file) as conf:
            config = json.load(conf)
    except FileNotFoundError:
        print(f"Configuration file '{config_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error decoding JSON from configuration file '{config_file}'.")
        return
    
    try:
        star_config = config['/work/talisman/sthakur/STAR/source/STAR']
    except KeyError:
        print("Key '/work/talisman/sthakur/STAR/source/STAR' not found in the configuration file.")
        return
    
    print("Started STAR Run")
    
    outSAMtype_args = star_config.get("outSAMtype", ["BAM", "SortedByCoordinate"])
    outSAMtype_args = outSAMtype_args if isinstance(outSAMtype_args, list) else [outSAMtype_args]
    outSAMattributes = star_config.get("outSAMattributes", "NH HI AS NM MD").split()

    # Access the value of runThreadN under the STAR section 
    run_thread_n = star_config.get('runThreadN', 16)
    print("runThreadN under STAR section:", run_thread_n)
    
    # Ensure output directory exists
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    
    star_command = [
        "/work/talisman/sthakur/STAR/source/STAR",
        "--readFilesIn", forward, reverse,
        "--genomeDir", genome_dir,
        "-readFilesCommand", star_config.get("readFilesCommand", "zcat"),
        "--runThreadN", str(run_thread_n),
        "--twopassMode", star_config.get("twopassMode", "Basic"),
        "--alignEndsType", star_config.get("alignEndsType", "EndToEnd"),
        "--alignSJoverhangMin", str(star_config.get("alignSJoverhangMin", 8)),
        "--alignSJDBoverhangMin", str(star_config.get("alignSJDBoverhangMin", 1)),
        "--outFilterMismatchNmax", str(star_config.get("outFilterMismatchNmax", 4)),
        "--alignIntronMin", str(star_config.get("alignIntronMin", 20)),
        "--alignIntronMax", str(star_config.get("alignIntronMax", 1000000)),
        "--quantMode", star_config.get("quantMode","Transcripto smeSAM"),
        "--outFilterType", star_config.get("outFilterType", "BySJout"),
        "--outSAMtype", *outSAMtype_args,
        "--outFileNamePrefix", output_directory + "/",
        "--outSAMattributes", *outSAMattributes,
        "--sjdbGTFfile", "/work/talisman/sthakur/bispecific/REF/genome.gtf",
        "--outSAMstrandField", star_config.get("outSAMstrandField", "intronMotif")
    ]
    print("STAR Command:", ' '.join(star_command))

    # Run STAR alignment
    try:
        result = subprocess.run(star_command, check=True, capture_output=True, text=True)
        print("STAR Run Output:", result.stdout)
        print("STAR Run Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print("STAR Run failed:", e.stderr)
    
    # Completion
    print("STAR Run completed")

# For D1 killers
forward = "/work/talisman/sthakur/bispecific/FASTQ/D1killers_1.fq"
reverse = "/work/talisman/sthakur/bispecific/FASTQ/D1killers_2.fq"
output_directory = "/work/talisman/sthakur/star_output/D1_killers"
config_file = "/work/talisman/sthakur/config.json"  
genome_dir = "/work/talisman/sthakur/index"

run_star(forward, reverse, output_directory, config_file, genome_dir)
