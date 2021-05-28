# Program to extract number
# of rows using Python
import xlrd
 
# Give the location of the file
loc = ("path of file")
 
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)
 
# Extracting number of rows
print(sheet.nrows)