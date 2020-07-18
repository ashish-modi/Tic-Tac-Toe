# Multiplayer

import os
from common import Common

class multiplayer(Common):
    def show_Board(self,Board):  # displays the board
        os.system('clear')
        print("_______________TIC-TAC-TOE__________________\n")
        print("\n Choose the positions as shown:\n")
        self.Input_GameBoard(Board)
        print("\tPLAYER 1  : X ")
        print("\tPLAYER 2  : 0 \n")
        self.GameBoard(Board)

    def TicTacToe(self,Board):      # main game function
        over1,over2 = 1,1
        while(over1 or over2):
            self.show_Board(Board)
            choice=input("Player 1's turn: ")
            x,y=Common.dictionary[choice]    # player's chosen position
            while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == "0":    # # check whether the position is occupied
                choice=input("That space is already filled, Enter again: ")
                x,y=Common.dictionary[choice]
            Board[int(x)][int(y)]="X"
            self.show_Board(Board)
            over1=self.Is_game_over(Board)       # checks whether the game is over after the previous move
            if over1 == 0:
                print("Player 1 wins")
                break
            is_empty = self.Is_empty(Board)     # checks whether there is an empty place on the board
            if is_empty == 0:
                print("GAME DRAW")
                break
            self.show_Board(Board)
            choice=input("Player 2's turn: ")
            x,y=Common.dictionary[choice]
            while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == "0":
                choice=input("That space is already filled, Enter again: ")
                x,y=Common.dictionary[choice]
            Board[int(x)][int(y)]="0"
            self.show_Board(Board)
            over2=self.Is_game_over(Board)
            if over2 == 0:
                print("Player 2 wins")
                break
        print("\nTHE GAME IS OVER\n")
        c = input("Press any key to go to the main menu")
        return
