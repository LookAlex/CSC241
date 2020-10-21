print('Hello User Welcome')
data=input('Do you want to enter data? Please only enter these two either (y/n): ')
if data=='n':
    exit()#user enter's n into program kill statment shows
counter=1
lst1=[]
lst2=[]
GPA=[]
while (data=='y'):
    miles=eval(input('Distance ran in miles: '))
    lst1.append(miles)
    time=eval(input('Time needed to run milage in minutes: '))
    lst2.append(time)
    pace=time/miles
    print('Your pace for this run was:',pace,'minutes per mile')
    exit_value=len(lst2)
    for i in range(exit_value):
        GPA.append(lst2[i]/lst1[i])
    data=input('Would you to play again? (y/n): ')
    if data=='y':#if y entered counter goes up 1 
        counter+=1
        
print('Thank You for using pace tracker')
if counter==1:
    print('You entered data for',counter, 'run')
else:
    print('You entered data for',counter, 'runs')
print('Total milage was '+str(sum(lst1))+ ' miles')#total miles
print('The longest run you entered was',max(lst1),'miles long')#longest run
print('Your overall pace was ',sum(GPA)/float(len(GPA)),' minutes per mile')#find pace=total time/total milage
