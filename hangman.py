# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 14:30:36 2018

@author: Holt88
"""

class Hangman():
    
    def __init__(self,phrase,display = [],fail_count = 0,guesses=[]):
        self.phrase = [x for x in phrase.lower()]
        self.display = ["_" if x !=" " else " " for x in self.phrase]
        self.fail_count = fail_count
        self.guesses = guesses
        
    def displayBoard(self):
        print(" ".join(self.display))
        
    def displayHangman(self):
        print("  --------")
        print("  |       |")
        print("  |        ")
        print("  |        ")
        print("  |        ")
        print("  |        ")
        print("  |        ")
        print("  |        ")
        print("__|________")
        
    def displayBodyParts(self):
        bodyparts = ['O','/','|','\\','/ ','\\']
        if self.fail_count > 0:
            return bodyparts[self.fail_count]
    
    def checkGuess(self,n):
        for l in self.phrase:
            if l == n.lower():
                return self.phrase.index(n)
        else:
            self.guesses.append(n)
            return -1
   
    def updateGuess(self,pos,n):
        self.display[pos] = n
        self.phrase[pos] = "_"
        
    def fail(self):
        self.fail_count += 1

    def checkWin(self):
        for x in self.display:
            if x=="_":
                return True
        return False    
                
        
# The program        
test=Hangman(input("Enter the phrase: "))
test.displayBoard()
test.displayHangman()
game_on = True

while game_on:
    
    attempt = input("Enter a letter to check:")
    pos = test.checkGuess(attempt)
    if pos>=0:
        test.updateGuess(pos,attempt)
        test.displayBoard()
        if test.checkWin()==False:
            print("Congratulations, you guessed the phrase!")
            game_on=False
    else:
        print("Try again")
        test.fail()
        again = test.fail_count
        if again > 2:
            print("Too many attempts, game over")
            game_on = False

#Things left to do: 
    #add in the actual hangman graphic
    #would you like to solve now?
    #display the guesses
    #display # of wrong attempts left
