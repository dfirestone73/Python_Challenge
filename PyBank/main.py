import os
import csv

budgetCSV=r'C:\Users\dfire\Desktop\RU-HOU-DATA-PT-07-2019-U-C\03-Python\Homework\PyBank\Resources\budget_data.csv'

monthCount=0
totalCost=0
def average(numbers)

with open (budgetCSV,newline="") as csvfile:
    csvReader=csv.reader(csvfile,delimiter=",")
    header=next(csvReader)
    for row in csvReader:
        monthCount+=1
        totalCost=totalCost+float(row[1])
    print(f'Total Months: {monthCount}')
    print(f'Total: ${totalCost}')
    print(change[])
    #print(f'Average Change: ${avgChange}')
        
