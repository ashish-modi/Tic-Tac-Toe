# singleplayer

import os
from common import Common

class singleplayer(Common):
    def Computer_row_chance(self,Board):          
        for i in range(3):
            pos_i,pos_j,count_pos,count_cross=-1,-1,0,0
            for j in range(3):
                if Board[i][j] == "-":
                    pos_i=i
                    pos_j=j
                    count_pos+=1
                    if count_pos == 2:
                        break
                elif Board[i][j] == "X":
                    count_cross+=1
            else:
                if count_cross == 2 and (pos_i != -1 and pos_j != -1):
                    Board[pos_i][pos_j] = "0"
                    return 1
        else:
            return 0
                
    def Computer_col_chance(self,Board):             
        for i in range(3):
            pos_i,pos_j,count_pos,count_cross=-1,-1,0,0
            for j in range(3):
                if Board[j][i] == "-":
                    pos_i=i
                    pos_j=j
                    count_pos+=1
                    if count_pos == 2:
                        break
                elif Board[j][i] == "X":
                    count_cross+=1
            else:
                if count_cross == 2 and (pos_i != -1 and pos_j != -1):
                    Board[pos_j][pos_i] = "0"
                    return 1
        else:
            return 0

    def Computer_diagonal_chance(self,Board):           
        count_cross,count_zeros=0,0
        pos_i,pos_j=-1,-1
        for i in range(3):
            for j in range(3):
                if i == j:
                    if Board[i][j] == "-":
                        pos_i=i
                        pos_j=j
                    elif Board[i][j] == "X":
                        count_cross+=1
                    elif Board[i][j] == "0":
                        count_zeros+=1
        if count_cross == 2 and (pos_i != -1 and pos_j != -1) or ((count_cross == 1 and count_zeros == 1) and (pos_i != 1 and pos_j != 1)):
            Board[pos_i][pos_j] = "0"
            return 1
        else:
            return 0

    def Computer_wins_row(self,Board):           # checks whether computer can win after placing in a row
        for i in range(3):
            count_pos,count_zeros,pos_i,pos_j=0,0,-1,-1
            for j in range(3):
                if Board[i][j] == "0":
                    count_zeros+=1
                elif Board[i][j] == "-":
                    pos_i=i
                    pos_j=j
                    count_pos+=1
                    if count_pos == 2:
                        break
            else:
                if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                    Board[pos_i][pos_j] = "0"
                    return 1

    def Computer_wins_column(self,Board):           # checks whether computer can win after placing in a column
        for i in range(3):
            count_pos,count_zeros,pos_i,pos_j=0,0,-1,-1
            for j in range(3):
                if Board[j][i] == "-":
                    pos_i=i
                    pos_j=j
                    count_pos+=1
                    if count_pos == 2:
                        break
                elif Board[j][i] == "0":
                    count_zeros+=1
            else:
                if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                    Board[pos_j][pos_i] = "0"
                    return 1

    def Computer_wins_diagonal(self,Board):           # checks whether computer can win after placing in diagonal
        count_zeros=0
        pos_i,pos_j=-1,-1
        for i in range(3):
            for j in range(3):
                if i == j:
                    if Board[i][j] == "-":
                        pos_i=i
                        pos_j=j
                    elif Board[i][j] == "0":
                        count_zeros+=1
            else:
                if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                    Board[pos_i][pos_j] = "0"
                    return 1
        if Board[0][2] == "0" and Board[1][1] == "0" and Board[2][0] == "-":
            Board[2][0] = "0"
            return 1
        elif Board[0][2] == 0 and Board[1][1] == "-" and Board[2][0] == "0":
            Board[1][1] = "0"
            return 1
        elif Board[0][2] == "-" and Board[1][1] == "0" and Board[2][0] == "0":
            Board[0][2] = "0"
            return 1


    def Computer(self,Board,count):                     # computer's turn
        if count == 1:
            if Board[1][1] == "-":
                Board[1][1] = "0"
            else:
                Board[0][2] = "0"
        elif count == 2:
            # checks whether computer can win
            if self.Computer_wins_row(Board) or self.Computer_wins_column(Board) or self.Computer_wins_diagonal(Board):
                pass
            elif self.Computer_row_chance(Board) or self.Computer_col_chance(Board) or self.Computer_diagonal_chance(Board):
                pass
            # if computer cannot win, choose the position where it cannot lose
            elif Board[0][0] == "X" and Board[2][2] == "X" or Board[0][2] == "X" and Board[2][0] == "X":
                Board[1][0] = "0"
            elif Board[0][2] == "X" and Board[2][0] == "-":    
                Board[2][0] = "0"
            elif Board[2][0] == "X" and Board[0][2] == "-":
                Board[0][2] = "0"
            elif Board[0][0] == "-":
                Board[0][0] = "0"
        elif count == 3:
            if self.Computer_wins_row(Board) or self.Computer_wins_column(Board) or self.Computer_wins_diagonal(Board):
                pass
            elif self.Computer_row_chance(Board) or self.Computer_col_chance(Board) or self.Computer_diagonal_chance(Board):
                pass
            elif Board[2][2] == "-" and Board[2][0] == "X":
                Board[2][2] = "0"
            elif Board[0][2] == "-" and (Board[0][0] == "X" or Board[0][0] == "0"):
                Board[0][2] = "0"
            else:
                if Board[0][1] == "X":
                    pass 
                else:
                    Board[0][1] = "0"
        elif count == 4:
            if self.Computer_wins_row(Board) or self.Computer_wins_column(Board) or self.Computer_wins_diagonal(Board):
                pass
            elif self.Computer_row_chance(Board) or self.Computer_col_chance(Board) or self.Computer_diagonal_chance(Board):
                pass
            elif Board[2][1] == "-":
                Board[2][1] = "0"
            elif Board[0][1] == "-":
                Board[0][1] = "0"
            elif Board[1][0] == "-":
                Board[1][0] = "0"
            elif Board[2][2] == "-":
                Board[2][2] = "0"
            elif Board[1][2] == "-" and Board[0][2] == "X" or Board[1][2] == "0":
                Board[1][2] = "0"
            elif Board[0][2] == "-":
                Board[0][2] = "0"

    def show_Board(self,Board):                     # shows board after every turn
        os.system('clear')
        print("_______________TIC-TAC-TOE__________________\n")
        print("\n Choose the positions as shown:\n")
        self.Input_GameBoard(Board)
        print("\tPLAYER 1  : X ")
        print("\tCOMPUTER  : 0 \n")
        self.GameBoard(Board)

    def TicTacToe(self,Board):                             # main function 
        count,over1,over2=0,1,1
        print("\n You are Player 1 and you will play first.:\n")
        while(True):
            self.show_Board(Board)                  
            choice=input(" Player 1's turn: ")
            x,y=Common.dictionary[choice]           # player's chosen position
            while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == "0":  # check whether the position is occupied
                choice=input(" That space is already filled, Enter again: ")
                x,y=Common.dictionary[choice]
            Board[int(x)][int(y)]="X"
            count+=1
            self.show_Board(Board)
            over1=self.Is_game_over(Board)   # checks whether the game is over after player's move
            if over1 == 0:
                print(" You win !!")
                break
            is_empty = self.Is_empty(Board)   # checks whether there is an empty place on the board
            if is_empty == 0:           # if all the places are occupied, Game draws
                print(" Game Draws")
                break
            self.Computer(Board,count)     # Computer's turn 
            over2=self.Is_game_over(Board)
            if over2 == 0:
                self.show_Board(Board)
                print(" Computer wins.")
                break
        print("\n THE GAME IS OVER")
        choice=input("\n Press any key to go to the main menu")
        return
