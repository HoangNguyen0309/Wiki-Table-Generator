import pandas as pd
import openpyxl

df = pd.read_excel (r'tableexample.xlsx') 
numOfRows = df.shape[0]
numOfColumns = df.shape[1]
numOfRows = numOfRows + 1
print(numOfRows)
print(numOfColumns)
