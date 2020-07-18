# Main file

import single_p
import multi_p
import os
Board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

def clear_Board():
    for x in range(3):
        for y in range(3):
            Board[x][y] = '-'

while(True):
    os.system('clear')
    print("_______________TIC-TAC-TOE__________________\n")
    print("1.Multiplayer")
    print("2.Player VS Computer")
    print("3.Exit\n")
    inp = input("Enter your choice: ")
    if inp == '1':
        game = multi_p.multiplayer()
        game.TicTacToe(Board)
        clear_Board()
    elif inp == '2':
        game = single_p.singleplayer()
        game.TicTacToe(Board)
        clear_Board()
    elif inp == '3':
        break
    else:
        print("Invalid Input")
        inp = input("Press any key to try again")