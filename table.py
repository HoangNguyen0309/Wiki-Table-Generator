import pandas as pd
import openpyxl

df = pd.read_excel (r'tableexample.xlsx') 
numOfRows = df.shape[0]
numOfColumns = df.shape[1]
#print(numOfRows)
#print(numOfColumns)
for col in df.columns:
    print(col)
#f = open("output.txt", "w")
