def cleanData(initialscores, cleanedupscores):
    infile=open(initalscores)
    myfile=infile.readlines()
    infile.close()
    elminated=[]
    cleaned=[]
    for line in myfile:
        linelst=line.split()
        line1=linelst[0]
        line2=linelst[1:]
        for num in line2:
            line2[line.index(num)]=float(num)
            if (num==0 and num==10 for num in line2):
                eleminated[line1]=line2
            else:
                elminated[line1]=line2
    nfile=(cleanscore,'r')
    for i, c in cleaned:
        nfile.write(
    nfile.close()
    return(elminated)

guess=eval(input('What file do you want to use?')
cleanData(guess('clean.txt')
elminated=cleanData(guess('clean.txt'))
score=[]
score='012345678910'
for line in cleanfile:
    linelst=line.split()
    line1=linelst[0]
    line2=linelst[1:]
    for num in line 2:
        newnum=float(' '.join
        line2.index(num)]
    line2.remove(max(line2))
    line2.remove(min(line))
    line2(sum(line2))
    score=[line1]

wish(input('Do you want to continue? y/n')
while True:
     wish=eval(input('Do you want the medal winners? Press 1'))
     if wish==1:
        for i, c in score.items():
             if scoreSorted[0]==c:
     print('Gold Medal'+i+str(scoreSorted[0]))
      for i, c in score.items():
             if scoreSorted[1]==c:
     print('Silver Medal'+i+str(scoreSorted[1]))
      for i, c in score.items():
             if scoreSorted[2]==c:
     print('Bronze Medal'+i+str(scoreSorted[2]))
     elif wish==2
         cName=input('Enter the name of a contestants final score: ')
         if cName in elminated:
         print('Sorry they have been elminated')
     elif cName in cleaned:
         print(score[cName])
     else:
         print('Name you enetered does not exist')
     elif wish==3:
         eliminatedC=input('Request the eliminated contestants')
         for i, c in eliminated[]:
     print(i+' '+str(c))
     elif wish==4
     count=0
     userpath=input('Please select the path')
     userpath=open(userpath,'w')
     print(len(score))
     while number<len(scoreSorted)):
          for i, c in score.items():
              try:
              if score[number]=c:


nfile.close()
print('here')
          
     
     
