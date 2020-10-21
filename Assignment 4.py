def cesar(ofl, nfl):
    #ofl is the input file
    #nfl is the output file
    #call cesar in the runner using the file name and output file to get word count, character count, and line count after the print statements run
    #whatever the file name is will work for cesar and the output file (ie cesar('example.txt', 'test.txt'))
    fnum = 0
    inofl = open(ofl,'r')
    oflC = inofl.read()
    inofl.close()
    sNFLst = oflC.split()
    lsNFLst = oflC.split("\n")
    wordCount = len(sNFLst)
    print("There are " + str(wordCount) + " words in the file.")
    ssNFLst = list(oflC)
    charCount = len(ssNFLst)
    print("There are " + str(charCount) + " characters in the file.")
    for i in range (len(lsNFLst)):
        if lsNFLst[i] == ",":
            del(lsNFLst[i])
    with open(ofl) as f:
        for i, l in enumerate(f):
                pass
        return i -1

def e(string, shift):
     #the encryption of the file
  cip = ''
  for char in string: 
    if char == ' ':
      cip = cip+ char
    elif  char.isupper():
      cip = cip + chr((ord(char) + shift - 65) % 26 + 65)
    else:
      cip = cip+ chr((ord(char) + shift - 97) % 26 + 97)
  
  return cip
 
t = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", t)
print("encryption: ", e(t, s))


