import csv
import matplotlib as plt
import numpy as np
import pandas as pd

# https://pythonru.com/uroki/osnovy-pandas-1-chtenie-fajlov-dataframe-otbor-dannyh
# https://rukovodstvo.net/posts/id_599/

# with open('LogPID.csv', newline='') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         print(row)


titanic_data = pd.read_csv('LogPID.csv', delimiter=';')
# pd.article_read[['p_err', 'd_err']]
print(titanic_data)