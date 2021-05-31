import pandas as pd
import openpyxl
import re
import xlwt
from xlwt import Workbook


headings_list = []
num_list = []
num_list2 = []

def parse(line):
    for x in range(len(line)):
        if x == 0:
            num_list2.append(x+1)
        if line[x] == '!' and line[x+1] == '!':
            num_list.append(x-1)
            num_list2.append(x+2)
        if x == len(line) - 1:
            num_list.append(x + 1)
def get_headings(num1, num2, line):
    headings_list.append(line[num1: num2])
f = open('file.txt') # Open file on read mode
lines = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file

encounter = False
new_list = []
cells = []
count = 0
for line in lines:
    if line[0] == '!':
        parse(line)
        for i in range(len(num_list)):
            get_headings(num_list2[i], num_list[i], line)
    if line[0] == '|' and line[1] != '-':
        new_list.append(line[1:])
    elif line[0] == '|' and (line[1] == '-' or line[1] == '}'):
        if count != 0:
            cells.append(new_list)
            new_list = []
        count = count + 1
print(cells)

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

for i in range(len(headings_list)):
    sheet1.write(0, i, headings_list[i]) #y,x, argv

count2 = 0
for i in range(len(cells)):
    i = i + 1
    for x in range(len(cells[0])):
        print(count2)
        sheet1.write(i, x, cells[count2][x])
    count2 = count2 + 1

wb.save('example4.xls')
 
