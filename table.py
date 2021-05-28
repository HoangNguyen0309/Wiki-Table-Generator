import pandas as pd
import openpyxl

df = pd.read_excel (r'tableexample.xlsx') 
numOfRows = df[df.columns[0]].count()
numOfColumns = df[df.rows[0]].count()
print(numOfRows)
print(numOfColumns)
