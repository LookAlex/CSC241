def openfile():
    """Opens the document or says can not be found"""
    try:
        infile=open('accounts.txt','r')
        return infile
    except IOError:
        return None
def deposit(names, pin):
    """asks how much money to deposit updates balance"""

    deposit=''
    while deposit=='':
        try:
            deposit=eval(input('How money do you want to deposit? '))
            if deposit<=0:#makes sure that user doesn't enter 0 or lower than 0 or a letter
                print('Amount not valid')
                deposit=''
        except:
            print('Not valid amount')

    Balance=names[pin]['balance']+deposit#adds the amount into the current balance
    names[pin]['balance']=Balance
    print('Money has been deposited')
    return names
def withdraw(names, pin):
    """asks how much to withdraw updates balance"""

    withdraw=''
    while withdraw=='':
        try:
            withdraw=eval(input('How much money do you want to withdraw? '))
            if withdraw> names[pin]['balance']:#checks the current balance to see if sufficent funds
                print('You do not have enough money in your account')
                withdraw=''
            elif withdraw<=0:
                print('Not a valid amount')
        except:
            print('Not a valid amount')

    amount=names[pin]['balance']-withdraw
    names[pin]['balance']=amount
    print('Money has been withdrawn')
    return names

names={}
splitlist=[]

myfile=openfile()
if myfile !=None:
    accountinfo=myfile.readlines()
    myfile.close()

    for l in accountinfo:
        if l =='' or l=='\n':
            accountinfo.remove(l)
    for line in accountinfo:
        data={}
        splitlines=line.split()
        splitlist.append(splitlines)
        code=int(splitlines[0])
        name=splitlines[1] + ' ' + splitlines[2]
        balance=float(splitlines[3])
        data['name']=name
        data['balance']=balance
        names[code]=data
    password=names.keys()

    try:
        guess=eval(input('Enter your 4-digit code: '))
    except TypeError:
        print('Not a valid code')

    if guess in names:#if the name is in the list
        print('Welcome', names[guess]['name'])
        while True:
            wish=input('1 Deposit \n2 Withdraw \n3 Balance \n4 Quit\n')
            if wish=='1':#calls the deposit function
                deposit(names, guess)
            elif wish=='2':#calls the withdraw function
                withdraw(names, guess)
            elif wish=='3':#prints current balance
                print('Your balance is', names[guess])
            elif wish=='4':#ends the program
                print('Thank you. Please come again.')
                break
            else:
                break
        outfile=open('accounts.txt','w')
        for k in names:
            outfile.write(str(k) +' '+names[k]['name']+' '+ str(k)+names[k]['balance'])
        outfile.close()
    else:
        print('The code entered is not part of out system. Qutting...')
else:
    print('We are expierencing some internal problems. Come back soon!')
                          
              

    
