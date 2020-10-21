print('Welcome to hangman.\nYou will be asked to guess a letter.\nYou have 8 guesses total.\nIf you have no more guesses the game is over.\nYou will be prompt to play again.\nStatistics at the end.\n')
def update(sec, cor, inc):

    string = ''
    for x in range(len(sec)):
        if sec[x] == inc:
          string = string + inc
        else:
            string = string + cor[x]
def hangman():
    """takes a random word and tells if letter entered in the word or not"""
    infile=open('dictionary.txt','r')
    word=[]
    import string
    for w in infile:
        empty=""
        for character in w:
            if character in string.ascii_letters:
               empty+=character
        word.append(empty)
    infile.close()
    guess='yes'
    while guess=='yes':
        import random
        wordss=random.choice(word)
        underscore='_ '*len(wordss)#number of _ for random word chosen
        guessleft=8
        count=1
        wins=0
        while(guess=='yes')or guessleft>-1 and not underscore==wordss:
            #if user says yes and guesses are greater than -1 and the word has not been filled
            print(underscore)
            print(str(guessleft))
            guess=input('Enter a letter: ')
            if len(guess)>1:
                print('One letter only')
            elif guess in wordss:
                print('Correct')
                underscore = update(wordss, underscore, guess)
            elif guess not in wordss:
                print('Not in word')
                guessleft-=1
            elif guessleft<0:
                print('The word was '+str(wordss))
            else:
                print('You win')
                wins+=1
        guess=input('Would you like to play again yes or no? ')
        if guess=='yes':
            count+=1
    if count==1:#count of number of games
        print('You played',count,'game')
    elif count>1 or count==0:
        print('You played', count,'games')
    elif wins==0:#count of wins user had
        print('You won',wins,'games')
    elif wins==1:
        print('You won', wins, 'game')
    elif wins>1:
        print('You won',wins,'games')



hangman()

