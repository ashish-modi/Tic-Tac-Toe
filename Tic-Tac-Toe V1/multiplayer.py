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

def GameBoard(Board):
    print()
    for i in range(3):
        for j in range(3):
            print("\t",Board[i][j],end=" ")
        print("\n")
    print()


def check_row(Board):
    for i in range(3):
        count_row1,count_row2=0,0
        for j in range(3):
            if Board[i][j] == "X":
                count_row1+=1
            if Board[i][j] == "0":
                count_row2+=1
        if count_row1 == 3 or count_row2 == 3:
            return 0


def check_column(Board):
    for i in range(3):
        count_col1,count_col2=0,0
        for j in range(3):
            if Board[j][i] == "X":
                count_col1+=1
            if Board[j][i] == "0":
                count_col2+=1
        if count_col1 == 3 or count_col2 == 3:
            return 0


def check_diagonal_right(Board):
    if Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X" or Board[0][0] == "0" and Board[1][1] == "0" and Board[2][2] == "0":
        return 0


def check_diagonal_left(Board):
    if Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X" or Board[0][2] == "0" and Board[1][1] == "0" and Board[2][0] == "0":
        return 0

def Is_empty(Board):
    for i in range(3):
        for j in range(3):
            if Board[i][j] == "-":
                return 1
    else:
        return 0

def Is_game_over(Board):
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


class TicTacToe():

    over1,over2=1,1
    print("\nThe game begins now:\n")
    print("Player 1: X ")
    print("Player 2: 0 \n")
    GameBoard(Board)
    while(over1 or over2):
        choice=input("Player 1's turn: ")
        x,y=dictionary[choice]

        while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == "0":
            choice=input("That space is already filled, Enter again: ")
            x,y=dictionary[choice]

        Board[int(x)][int(y)]="X"

        GameBoard(Board)
        over1=Is_game_over(Board)

        if over1 == 0:
            print("Player 1 wins")
            break

        is_empty = Is_empty(Board)

        if is_empty == 0:
            print("GAME DRAW")
            break

        choice=input("Player 2's turn: ")
        x,y=dictionary[choice]

        while Board[int(x)][int(y)] == "X" or Board[int(x)][int(y)] == "0":
            choice=input("That space is already filled, Enter again: ")
            x,y=dictionary[choice]
          
        Board[int(x)][int(y)]="0"

        GameBoard(Board)
        over2=Is_game_over(Board)
        
        if over2 == 0:
            print("Player 2 wins")
            break

    print("THE GAME IS OVER")

TicTacToe()




