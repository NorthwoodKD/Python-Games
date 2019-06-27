# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:30:36 2018

@author: Holt88
"""

class Hangman():
    
    def __init__(self,phrase,display = [],fail_count = 0,guesses=[],bodyparts = ['O','/','|','\\','|','/ ','\\'], hangman=[" "," "," "," "," "," "," "]):
        '''This class requires a phrase    '''
        self.phrase = [x for x in phrase.lower()]
        self.display = ["_" if x !=" " else " " for x in self.phrase]
        self.fail_count = fail_count
        self.guesses = guesses
        self.bodyparts = bodyparts
        self.hangman = hangman
        
    def displayBoard(self):
        """Displays the phrase which updates if correctly guessed """
        print("PLAYER 2 guess this phrase: " + " ".join(self.display))
        
    def displayGuess(self):
        """Displays the incorrect letters guessed """
        print("LETTERS GUESSED: " + " ".join(self.guesses))
        
    def displayHangman(self):
        print("  --------")
        print("  |       |")
        print("  |       "+self.hangman[0])
        print("  |      "+ self.hangman[1] + self.hangman[2] + self.hangman[3])
        print("  |       "+self.hangman[4])
        print("  |      "+ self.hangman[5] +" " +self.hangman[6])
        print("  |        ")
        print("  |        ")
        print("  |        ")
        print("__|________")
        
    def displayBodyParts(self):
        """ Display the body parts left to assign"""
        if self.fail_count > 0:
            return bodyparts[self.fail_count]
    
    def checkGuess(self,n):
        for l in self.phrase:
            if l == n.lower():
                return self.phrase.index(n.lower())
        else:
            self.guesses.append(n)
            return -1
   
    def updateGuess(self,pos,n):
        self.display[pos] = n.lower()
        self.phrase[pos] = "_"
    
    def updateDislayHangman(self):
        self.hangman[self.fail_count] = self.bodyparts[self.fail_count]
        
    def fail(self):
        self.fail_count += 1

    def checkWin(self):
        for x in self.display:
            if x=="_":
                return True
        return False    
                
        
# The program        
test=Hangman(input("PLAYER 1, enter a phrase: "))
game_on = True

while game_on:
    test.displayHangman()
    test.displayBoard()
    test.displayGuess()
    attempt = input("PLAYER 2, Enter a letter to check:")
    pos = test.checkGuess(attempt)
    if pos>=0:
        test.updateGuess(pos,attempt)
        test.displayBoard()
        if test.checkWin()==False:
            print("Congratulations, you guessed the phrase!")
            game_on=False
    else:
        test.updateDislayHangman()
        print("Try again")
        test.fail()
        again = test.fail_count
        if again > 6:
            print("Too many attempts, game over")
            game_on = False

#Things left to do: 
    #add in the actual hangman graphic
    #would you like to solve now?
    #display # of wrong attempts left
