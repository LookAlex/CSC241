x=eval(input('Enter a number between 0 and 10: '))
def inputValidation(x):

    while True:
        if x in range(0,11):
            print('You said',x)
            break
        x=eval(input('Enter a number between 0 and 10: '))
inputValidation(x)

freeBooks=0
if isPremiumCustomer==True:
    if nbooksPurchased>=5:
        freeBooks=1
elif nbooksPurchased>=8:
    freeBooks=2
if isPremiumCustomer==False:
    if nbooksPurchased>=7:
        freeBooks=1
if nbooksPurchased>=12:
    freeBooks=2
