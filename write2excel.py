import pandas as pd
import openpyxl

bruh = "[[11, 21, 31], [12, 22, 32], [31, 32, 33]], index=['one', 'two', 'three'], columns=['a', 'b', 'c']"
df = pd.DataFrame(bruh)

print(df)