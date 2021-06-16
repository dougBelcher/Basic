import sys

import pandas as pd
import os

# os.chdir('//wrprod/wrdsup/supdata')

# files = [f for f in os.listdir('//wrprod/wrdsup/supdata') if os.path.isfile(f)]
files = [f for f in os.listdir('..') if os.path.isfile(f)]
# print(f'{os.listdir}')
# sys.exit()

merged = []

for f in files:
    filename, ext = os.path.splitext(f)
    print(f'{filename} {ext}')
    if ext == '.csv':
        read = pd.read_csv(f)
        merged.append(read)

sys.exit()

result = pd.concat(merged)

result.to_csv('merged.csv')