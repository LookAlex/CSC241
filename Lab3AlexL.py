def seperate (sentence):
    for s in sentence:
            t =sentence.replace('. ', '.\n')
    print(t)

def avgLst ():
    r=eval(input('Please enter a list with starting with a [ and ending with a ] and between each number put a ,: '))
    for i in r:
        if len(r) !=0:
            return sum(r)/(len(r))
    else:
        return 0.0
