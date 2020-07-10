import os

inputs=[]

Board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]

dictionary={
        "1":(0,0),"2":(0,1),"3":(0,2),
        "4":(1,0),"5":(1,1),"6":(1,2),
        "7":(2,0),"8":(2,1),"9":(2,2)
        }
def Input_GameBoard():
    k=1
    for i in range(3):
        for j in range(3):
            print("\t",k,end= " ")
            k+=1
        print("\n")


def GameBoard(Board):                                                 # BOARD
    print()
    for i in range(3):
        for j in range(3):
            print("\t",Board[i][j],end=" ")
        print("\n")
    print()


def Computer_row_chance(Board):                                        # DEFENCE (ROW)

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
                pass
        else:
            if count_cross == 2 and (pos_i != -1 and pos_j != -1):
                Board[pos_i][pos_j] = 0
                return 1
    else:
        return 0
            

def Computer_col_chance(Board):                                         # DEFENCE (COLUMN)
    
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
                pass
        else:
            if count_cross == 2 and (pos_i != -1 and pos_j != -1):
                Board[pos_j][pos_i] = 0
                return 1
    else:
        return 0


def Computer_diagonal_chance(Board):                                      # DEFENCE (DIAGONAL)

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
                elif Board[i][j] == 0:
                    count_zeros+=1

    if count_cross == 2 and (pos_i != -1 and pos_j != -1) or ((count_cross == 1 and count_zeros == 1) and (pos_i != 1 and pos_j != 1)):
        Board[pos_i][pos_j] = 0
        return 1
    else:
        return 0


def Computer_wins_row(Board):                                              # COMPUTER WINS (ROW)

    for i in range(3):
        count_pos,count_zeros,pos_i,pos_j=0,0,-1,-1
        for j in range(3):
            if Board[i][j] == 0:
                count_zeros+=1
            elif Board[i][j] == "-":
                pos_i=i
                pos_j=j
                count_pos+=1
                if count_pos == 2:
                    break
            else:
                pass
        else:
            if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                Board[pos_i][pos_j] = 0
                return 1



def Computer_wins_column(Board):                                            # COMPUTER WINS (COLUMN)

    for i in range(3):
        count_pos,count_zeros,pos_i,pos_j=0,0,-1,-1
        for j in range(3):
            if Board[j][i] == "-":
                pos_i=i
                pos_j=j
                count_pos+=1
                if count_pos == 2:
                    break
            elif Board[j][i] == 0:
                count_zeros+=1
            else:
                pass
        else:
            if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                Board[pos_j][pos_i] = 0
                return 1


def Computer_wins_diagonal(Board):                                           # COMPUTER WINS (DIAGONAL)

    count_zeros=0
    pos_i,pos_j=-1,-1
    for i in range(3):
        for j in range(3):
            if i == j:
                if Board[i][j] == "-":
                    pos_i=i
                    pos_j=j
                elif Board[i][j] == 0:
                    count_zeros+=1
                else:
                    pass
        else:
            if count_zeros == 2 and pos_i != -1 and pos_j != -1:
                Board[pos_i][pos_j] = 0
                return 1

    if Board[0][2] == 0 and Board[1][1] == 0 and Board[2][0] == "-":
        Board[2][0] = 0
        return 1
    elif Board[0][2] == 0 and Board[1][1] == "-" and Board[2][0] == 0:
        Board[1][1] = 0
        return 1
    elif Board[0][2] == "-" and Board[1][1] == 0 and Board[2][0] == 0:
        Board[0][2] = 0
        return 1


def Computer(Board,count):                                                     # COMPUTER'S TURN

    if count == 1:
        if Board[1][1] == "-":
            Board[1][1] = 0
        else:
            Board[0][2] = 0

    elif count == 2:
        if Computer_wins_row(Board) or Computer_wins_column(Board) or Computer_wins_diagonal(Board):
            pass
        elif Computer_row_chance(Board) or Computer_col_chance(Board) or Computer_diagonal_chance(Board):
            print("Chance")
            pass
        elif Board[0][0] == "X" and Board[2][2] == "X" or Board[0][2] == "X" and Board[2][0] == "X":
            Board[1][0] = 0
        #elif Board[0][2] == "X" and Board[2][0] == "-":    
         #   Board[2][0] = 0
        #elif Board[2][0] == "X" and Board[0][2] == "-":
         #   Board[0][2] = 0
        elif Board[0][0] == "-":
            Board[0][0] = 0
        else:
            print("No move for the computer")

    elif count == 3:
        if Computer_wins_row(Board) or Computer_wins_column(Board) or Computer_wins_diagonal(Board):
            pass
        elif Computer_row_chance(Board) or Computer_col_chance(Board) or Computer_diagonal_chance(Board):
            print("Chance")
            pass
        elif Board[2][2] == "-" and Board[2][0] == "X":            #....
            Board[2][2] = 0
        elif Board[0][2] == "-" and (Board[0][0] == "X" or Board[0][0] == 0):
            Board[0][2] = 0
        else:
            if Board[0][1] == "X":
                print("No move for the computer")
            else:
                Board[0][1] = 0

    elif count == 4:
        if Computer_wins_row(Board) or Computer_wins_column(Board) or Computer_wins_diagonal(Board):
            pass
        elif Computer_row_chance(Board) or Computer_col_chance(Board) or Computer_diagonal_chance(Board):
            print("Chance")
            pass
        elif Board[2][1] == "-":
            Board[2][1] = 0
        elif Board[0][1] == "-":
            Board[0][1] = 0
        elif Board[1][0] == "-":
            Board[1][0] = 0
        elif Board[2][2] == "-":
            Board[2][2] =0
        elif Board[1][2] == "-" and Board[0][2] == "X" or Board[1][2] == 0:
            Board[1][2] = 0
        else:
            print("No move for the computer")


def check_row(Board):
    for i in range(3):
        count_cross,count_zeros=0,0
        for j in range(3):
            if Board[i][j] == "X":
                count_cross+=1
            if Board[i][j] == 0:
                count_zeros+=1
        if count_cross == 3 or count_zeros == 3:
            return 0


def check_column(Board):
    for i in range(3):
        count_cross,count_zeros=0,0
        for j in range(3):
            if Board[j][i] == "X":
                count_cross+=1
            if Board[j][i] == 0:
                count_zeros+=1
        if count_cross == 3 or count_zeros == 3:
            return 0


def check_diagonal_right(Board):
    if Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X" or Board[0][0] == 0 and Board[1][1] == 0 and Board[2][2] == 0:
        return 0


def check_diagonal_left(Board):
    if Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X" or Board[0][2] == 0 and Board[1][1] == 0 and Board[2][0] == 0:
        return 0




def Is_empty(Board):                      # CHECK FOR EMPTY SPACES
    for i in range(3):
        for j in range(3):
            if Board[i][j] == "-":
                return 1
    else:
        return 0



def Is_game_over(Board):                               # GAME OVER
    row = check_row(Board)
    if row == 0:
        return 0

    column = check_column(Board)
    if column == 0:
        return 0

    diagonal1 = check_diagonal_left(Board)
    if diagonal1 == 0:
        return 0

    diagonal2 = check_diagonal_right(Board)
    if diagonal2 == 0:
        return 0

    else:
        return 1

def show_Board():
    os.system('clear')
    print("\n Choose the positions as shown:\n")
    Input_GameBoard()
    print("\tPLAYER 1  : X ")
    print("\tCOMPUTER  : 0 \n")
    GameBoard(Board)


def TicTacToe(Board):                                  # MAIN GAME FUNCTION

    count,over1,over2=0,1,1
    print("\n You are Player 1. The game starts now:\n")

    while(True):
        show_Board()
        choice=input(" Player 1's turn: ")
        inputs.append(choice)
        x,y=dictionary[choice]

        while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == 0:
            choice=input(" That space is already filled, Enter again: ")
            x,y=dictionary[choice]

        Board[int(x)][int(y)]="X"
        count+=1
        
        over1=Is_game_over(Board)
        if over1 == 0:
            print(" You win !!")
            break

        is_empty = Is_empty(Board)

        if is_empty == 0:
            print(" GAME DRAW")
            break

        print(" Computer's turn")        
        Computer(Board,count)
        over=Is_game_over(Board)
        if over == 0:
            show_Board()
            print(" Computer wins.  HAHAHA")
            break

    print("\n THE GAME IS OVER")
    choice=input("\n IF YOU WANT TO PLAY AGAIN, PRESS 'Y' ELSE PRESS ANY BUTTON TO EXIT ----> ");
    if choice == 'Y' or choice == 'y':
        for z in range(3):
            for y in range(3):
                Board[z][y] = '-'
        TicTacToe(Board)
    else:
        os.system('clear')
        return

TicTacToe(Board)


