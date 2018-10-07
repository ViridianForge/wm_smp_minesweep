'''
Simple CLI Minesweeper Game

@author Wayne Manselle
Made for exercise purposes
'''

import os
import array
import random
import math

class Minesweeper:
    def __init__(self):
        self._viewLayer = None
        self._mineLayer = None
        self._gameon = True
        self._difficulty = 0
        self._configs = [64,100,576]

    '''
    Set up game status
    '''
    def conf(self):
        #Request input to configure game
        while(self._difficulty == 0):
            print("What game difficulty would you like? \n 1. Beginner -- (8x8) 10 mines \n 2. Intermediate -- (10x10) 40 mines \n 3. Expert -- (24x24) 99 mines")
            pot_diff = input("Respond with 1 for Beginner, 2 for Intermediate, or 3 for Expert")
            if pot_diff in ["1", "2", "3"]:
                self._difficulty = int(pot_diff) #64, 100, 576
            else:
                print("That was an invalid response.")
                os.system("clear")
        
        #Initialize the gameboard
        self._viewLayer = array.array('i',(0 for i in range(0,self._configs[self._difficulty])))
        self._mineLayer = array.array('i',(0 for i in range(0,len(self._viewLayer))))

    def active(self):
        return self._gameon

    '''
    Display Game to Command Line
    '''
    def disp_game(self):
        os.system("clear")
        for i in range(0,len(self._viewLayer), int(math.sqrt(len(self._viewLayer)))):
            print(str(self._viewLayer[i:i+int(math.sqrt(len(self._viewLayer)))]) + "\n")
        return

    '''
    Get player's next moove
    '''
    def get_move(self):
        input("Make your move.")
        return

'''
Main Method
'''
def main():
    print("Welcome to Minesweeper!")
    game = Minesweeper()
    game.conf()
    while(game.active):
        game.disp_game()
        game.get_move()


if __name__ == "__main__" : main()