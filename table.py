import pandas as pd
import openpyxl

df = pd.read_excel (r'tableexample.xlsx') 
numOfRows = df.shape[0]
numOfColumns = df.shape[1]
#print(numOfRows)
#print(numOfColumns)

print(df.loc[0][1])
print(len(df.loc[0]))

f = open("output.txt", "w")
f.write("{| class=\"wikitable\"\n")
count = 0
for col in df.columns:
    if count == 0:
        f.write("! " + col)
    elif count != 0:
        f.write(" !! " + col)
    elif count == numOfColumns:
        f.write(" !! " + col + "\n|-") 
    count = count + 1  
for i in range(numOfRows): 
    count2 = 0     
    for x in range(numOfColumns):
        if count2 == 0:
            f.write("| " + df.loc[i][count2] + " || ")
        elif count2 != 0:
            f.write(df.loc[i][count2] + " || ")
        elif count2 == numOfColumns:
            f.write(df.loc[i][count2] + "\n")    
        count2 = count2 + 1    
