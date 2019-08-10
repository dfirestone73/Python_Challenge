import os
import csv
from statistics import mean

budgetCSV=r'C:\Users\dfire\Desktop\Data Analytics\3_Intro to Python\Homework\PyBank\Resources\budget_data.csv'

monthCount=0
totalCost=0
def average(avgChange):
    return mean(avgChange)
month=0
maxProfit=0
minProfit=0
m1=0
m2=0
x=0
n=0
r=0

avgChange=[]
profitLoss=[]
month1=0
month2=0
month3=0
month4=0
avg=0




with open (budgetCSV,newline="") as csvfile:
    csvReader=csv.reader(csvfile,delimiter=",")
    header=next(csvReader)
    for row in csvReader:
        monthCount+=1
        totalCost=totalCost+float(row[1])
    #Average Change
        '''if n%2==0:
            month1=float(row[1])
        elif n%2!=0:
            month2=float(row[1])
        avgChange.append(month2-month1)
        n+=1
        if r%2!=0:
            month3=float(row[1])
        elif r%2==0:
            month4=float(row[1])
        avgChange.append(month4-month3)
        r+=1
        avg=average(avgChange)
        

        if n==0:
            month1=float(row[1])
            month2=float(row[1])
        elif n%2!=0:
            month2=float(row[1])
            avgChange.append(month2-month1)
        elif n%2==0:
            month1=float(row[1])
            avgChange.append(month1-month2)
        n+=1
        avg=sum(avgChange)/len(avgChange)'''

        profitLoss.append(row[1])
        #map turns every item in the list into an integer so sum function will work
        avg=(sum(map(int,profitLoss)))/len(profitLoss)
    #Greatest Increase
        if x==0:
            maxProfit=float(row[1])
            minProfit=float(row[1])
            m1=(row[0])
            m2=(row[0])
        elif maxProfit<float(row[1]):
            maxProfit=float(row[1])
            m1=(row[0])
    #Greatest Decrease
        elif minProfit>float(row[1]):
            minProfit=float(row[1])
            m2=(row[0])
        x+=1
    print('Financial Analysis')
    print('--------------------------------')
    print(f'Total Months: {monthCount}')
    print(f'Total: ${totalCost}')
    print(f'Average Change: ${avg}')
    print(f'Greatest Increase in Profits: {m1} (${maxProfit})')
    print(f'Greatest Decrease in Profits: {m2} (${minProfit})')


    with open('Output.txt',"w") as textFile:
        textFile.write('Financial Analysis \n -------------------------------- \n Total Months: {monthCount} \n Total: ${totalCost} \n Average Change: ${avg} \n Greatest Increase in Profits: {m1} (${maxProfit}) \n Greatest Decrease in Profits: {m2} (${minProfit})')

    
    


    #print(change[])
    #print(f'Average Change: ${avgChange}')
        
