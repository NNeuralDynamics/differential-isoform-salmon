import numpy as np
import pandas as pd
import glob

df = pd.read_csv("../samples.csv")
file_names = []
for i in df['sample_type']:
    file = glob.glob(f"../salmon_output/{i}/*.sf")
    file_names.extend(file)
print(file_names)

# file = glob.glob(f"../salmon_output/{i}/*.sf")