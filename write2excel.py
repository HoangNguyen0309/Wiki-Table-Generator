import pandas as pd
import openpyxl
import re

headings_list = []
num_list = []
num_list2 = []

def parse(line):
    for x in range(len(line)):
        if line[x] == '!' and line[x+1] == '!':
            num_list.append[x-1]
            num_list2.append[x+2]
        if line[x] == '!' and line[x+1] != '!':
            num_list2.append[x+1]
    if x == len(line):
        num_list.append(x)
def get_headings(num1, num2, line):
    headings_list.append(line[num1: num2])
f = open('file.txt') # Open file on read mode
lines = f.read().splitlines() # List with stripped line-breaks
f.close() # Close file


for line in lines:
    if line[0] == '!':
        parse(line)
        for i in len(num_list):
            get_headings(num_list2[i], num_list[i], line)


print(headings_list)
