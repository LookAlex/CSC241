#Function wordCount
def wordCount(string):
    punct=(',.?!:;-‘“') 
    for word in string:
        if word in punct:
            string=string.replace(word, '')
            print(string)


#User inputs a sentence into function wordCount
wordstring=eval(input('Please enter a string, and only a string please: '))
wordlist=wordstring.lower()
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))
print(wordlist)
print(wordfreq)
wordfreq.sort()
print('Your string has: ',wordfreq[0],'word(s) of length 1')
print('Your string has: ',wordfreq[1],'word(s) of length 2')
print('Your string has: ',wordfreq[2],'word(s) of length 3')
print('Your string has: ',wordfreq[3],'word(s) of length 4')
print('Your string has: ',wordfreq[4],'word(s) of length 5')
print('Your string has: ',wordfreq[5],'word(s) of length 6')
print('Your string has: ',wordfreq[6],'word(s) of length 7')
print('Your string has: ',wordfreq[7],'word(s) of length 8')
print('Your string has: ',wordfreq[8],'word(s) of length 9')
print('Your string has: ',wordfreq[9],'word(s) of length 10')
