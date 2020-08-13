#Import the Excel sheet on the Langzeitstatistik in Python

import pandas as pd
import os
from pandas_ods_reader import read_ods

file_path = "/Users/daniele/Desktop"
file_name =  "MIL2020_Langzeitstatistik.ods"
file_ = os.path.join(file_path, file_name)
df = read_ods(file_, "Tabelle1")
print (df)
print(df.head())
