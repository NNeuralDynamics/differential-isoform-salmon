"""import libraries"""
import gzip
import shutil

def unzip(path:str, output_path:str):
    with gzip.open(path,"rb") as f_in:
        with open(output_path,"wb") as f_out:
            shutil.copyfileobj(f_in,f_out)
        
unzip(path = "../REF/genome.gtf.gz",output_path = "../REF/genome.gtf")