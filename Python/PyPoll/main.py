import os
import csv


electionCSV=r'C:\Users\dfire\Desktop\Data Analytics\3_Intro to Python\Homework\PyPoll\Resources\election_data.csv'

voteCount=0
candidateList=[]
KhanCount=0
KhanPercent=0
CorreyCount=0
CorreyPercent=0
LiCount=0
LiPercent=0
OTooleyCount=0
OTooleyPercent=0
Winner=0


with open (electionCSV,newline="") as csvfile:
    csvReader=csv.reader(csvfile,delimiter=",")
    header=next(csvReader)
    for row in csvReader:
        voteCount+=1
        candidate=row[2]
        if candidate not in candidateList:
           candidateList.append(row[2])
        if row[2]=="Khan":
            KhanCount+=1
        if row[2]=="Correy":
            CorreyCount+=1
        if row[2]=="Li":
            LiCount+=1
        if row[2]=="O'Tooley":
            OTooleyCount+=1
        if KhanCount>CorreyCount & KhanCount>LiCount & KhanCount>OTooleyCount:
            Winner="Khan"
        elif CorreyCount>KhanCount & CorreyCount>LiCount & CorreyCount>OTooleyCount:
            Winner="Correy"
        elif LiCount>KhanCount & LiCount>CorreyCount & LiCount>OTooleyCount:
            Winner="Li"
        elif OTooleyCount>KhanCount & OTooleyCount>LiCount & OTooleyCount>CorreyCount:
            Winner="O'Tooley"
    KhanPercent= '{:.1%}'.format(KhanCount/voteCount)
    CorreyPercent='{:.1%}'.format(CorreyCount/voteCount)
    LiPercent='{:.1%}'.format(LiCount/voteCount)
    OTooleyPercent='{:.1%}'.format(OTooleyCount/voteCount)
    
    
    #print(candidateList)
            #Khan=0, Correy=1, Li=2, O'Tooley=3
        

    print('Election Results')
    print('------------------------')
    print(f'Vote Count: {voteCount}')
    print('------------------------')
    print(f'Khan: {KhanPercent} ({KhanCount})')
    print(f'Correy: {CorreyPercent} ({CorreyCount})')
    print(f'Li: {LiPercent} ({LiCount})')
    print(f"O'Tooley: {OTooleyPercent} ({OTooleyCount})")
    print('------------------------')
    print(f'Winner: {Winner}')
    print('------------------------')

    with open('Output.txt',"w") as textFile:
        textFile.write("Election Results \n ------------------------ \n Vote Count: {voteCount} \n ------------------------ \n Khan: {KhanPercent} ({KhanCount}) \n Correy: {CorreyPercent} ({CorreyCount}) \n Li: {LiPercent} ({LiCount}) \n O'Tooley: {OTooleyPercent} ({OTooleyCount}) \n ------------------------ \n Winner: {Winner} \n ------------------------")