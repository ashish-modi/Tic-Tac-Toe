# Here are the common functions of the game

class Common:
    # maps the player's input to the place on the board
    dictionary={
        "1":(0,0),"2":(0,1),"3":(0,2),
        "4":(1,0),"5":(1,1),"6":(1,2),
        "7":(2,0),"8":(2,1),"9":(2,2)
        }

    # displays the board
    def GameBoard(self,Board):
        print()
        for i in range(3):
            for j in range(3):
                print("\t",Board[i][j],end=" ")
            print("\n")
        print()
    
    # displays the positions to fill the board
    def Input_GameBoard(self,Board):
        k=1
        for i in range(3):
            for j in range(3):
                print("\t",k,end= " ")
                k+=1
            print("\n")

    # checks whether all elements in any row are same
    def check_row(self,Board):
        for i in range(3):
            count_row1,count_row2=0,0
            for j in range(3):
                if Board[i][j] == "X":
                    count_row1+=1
                if Board[i][j] == "0":
                    count_row2+=1
            if count_row1 == 3 or count_row2 == 3:
                return 0

    # checks whether all elements in any column are same
    def check_column(self,Board):
        for i in range(3):
            count_col1,count_col2=0,0
            for j in range(3):
                if Board[j][i] == "X":
                    count_col1+=1
                if Board[j][i] == "0":
                    count_col2+=1
            if count_col1 == 3 or count_col2 == 3:
                return 0

    # checks whether right diagonal elements are same
    def check_diagonal_right(self,Board):
        if Board[0][0] == "X" and Board[1][1] == "X" and Board[2][2] == "X" or Board[0][0] == "0" and Board[1][1] == "0" and Board[2][2] == "0":
            return 0

    # checks whether left diagonal elements are same
    def check_diagonal_left(self,Board):
        if Board[0][2] == "X" and Board[1][1] == "X" and Board[2][0] == "X" or Board[0][2] == "0" and Board[1][1] == "0" and Board[2][0] == "0":
            return 0
        
    # checks whether there is an empty place on the board
    def Is_empty(self,Board):
        for i in range(3):
            for j in range(3):
                if Board[i][j] == "-":
                    return 1
        else:
            return 0
        
    # checks whether the game is over
    def Is_game_over(self,Board):
        row = self.check_row(Board)
        if row == 0:
            return 0
        column = self.check_column(Board)
        if column == 0:
            return 0
        diagonal1 = self.check_diagonal_left(Board)
        if diagonal1 == 0:
            return 0
        diagonal2 = self.check_diagonal_right(Board)
        if diagonal2 == 0:
            return 0
        else:
            return 1
