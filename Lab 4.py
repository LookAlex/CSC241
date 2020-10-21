def empty(x):
    """return number of empty lines"""

    myFile=open(x, 'r')
    strlist=myFile.read()
    myFile.close()

    return strlist.count('\n')

def censor(string):
    """replace 4 letter word with xxxx"""
    inFile=open(string, 'r+')
    stringlist=inFile.read()
    inFile.close()
    
    punct= ',./?:\;"'
    for i in stringlist:
        if i in punct:
            listclean=stringlist.replace(i,' ')
    splitlist=listclean.split()
    
    for words in splitlist:
        if len(words)==4:
            splitlist[splitlist.index(words)]='xxxx'
    return splitlist

    outfile=open('censor.txt', 'w')
    outfile.write(' '.join(str(x) for x in splitlist))
    outFile.close()

def stats(y):
    """returns number of character, words, lines"""
    numlines=0
    charcount=0
    wordcount=0
    
    newFile=open(y, 'r')
    for line in newFile:
        words=line.split()

        numlines+=1
        charcount+=len(line)
        wordcount+=len(words)

    print('Line count '+str(numlines))
    print('Word count '+str(wordcount))
    print('Character count '+str(charcount))
