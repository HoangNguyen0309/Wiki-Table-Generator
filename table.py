# ananylze and desemble the table
import pandas as pd

def write2text(file_name):
    df = pd.read_excel(file_name) 
    numOfRows = df.shape[0]
    numOfColumns = df.shape[1]
    #print(numOfRows)
    print(numOfColumns)
    if 5 == numOfColumns -1:
        print("BRUH!")

    #print(df.loc[0][1])
    #print(len(df.loc[0]))

    f = open("output.txt", "w")
    f.write("{| class=\"wikitable\"\n")
    count = 0
    for col in df.columns:
        #print(count)
        if count == 0:
            f.write("! " + col)
        elif count != 0 and count != numOfColumns - 1:
            f.write(" !! " + col)
        elif count == numOfColumns - 1:
            print("Reaches here!")
            f.write(" !! " + col + "\n|-\n") 
        count = count + 1  
    for i in range(numOfRows):     
        for x in range(numOfColumns):
            if x == 0:
                f.write("| " + str(df.loc[i][x]) + " || ")
            elif x != 0 and x != numOfColumns - 1:
                f.write(str(df.loc[i][x]) + " || ")
            elif x == numOfColumns - 1:
                print("Reaches herw!")
                f.write(str(df.loc[i][x]) + "\n|-\n")       
