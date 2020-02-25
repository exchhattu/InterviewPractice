"""
Tue Feb 25 10:16:50 2020
Connect 4
"""

import numpy as np
from numpy.random import randint 


class Connect4:

    def __init__(self, board_size):
        """
        set a board size, it should be square and board_size is greater than 4
        """
        self._board_size = board_size
        if self._board_size < 4:
            print("Invalid board size")
            sys.exit()

        # initailize a board
        self._board = [ [0]* self._board_size for _ in range(self._board_size)] 
        self._is_computer = True

    def init_first_ball(self):
        col = randint(0, self._board_size -1) 
        self._board[0][col] = 1

    def udpate_user(self, user):
        self._is_computer = user

    def user_input(self, col):
        """
        check the validity of inputs by user
        """

        for row in range(self._board_size):
            if self._board[row][col] == 0:
                if self._is_computer: 
                    self._board[0][col] = -1
                    break
                else:
                    self._board[0][col] = 1
                    break

        def row_matches(self, row):
            """ check for each column """
            # Two point apporach, BFS is perfect suit here
            for col in range(self._board_size)-4:
                k = col 
                j = col + 4
                player = self._board[row][j]
                while k < j:
                    if self._board[row][k] == self._board[row][j]:  
                        k+=1
                        j-=1
                        return player
                    else:
                        break
            return ""

        def col_matches(self, col):
            """ check for each row"""
            # Two point apporach, BFS is perfect suit here
            for row in range(self._board_size)-4:
                k = row 
                j = row + 4
                player = self._board[k][col]
                while k < j:
                    if self._board[k][col] == self._board[j][col]:  
                        k+=1
                        j-=1
                        return player
                    else:
                        break
            return ""

        def matches_dig1(self, row, col):
            """ check for diagonal with increasing order"""
            # Two point apporach, BFS is perfect suit here
            i, j = row, col
            player = self._board[row][col]
            while count < 4 and i < len(self._board) and j< len(self._board[0]):
                if self._board[i][j] == self._board[i+1][j+1]:  
                    i, j = i+1, j+1 
                else:
                    return ""
                count += 1
            return player

        def matches_dig2(self, row, col):
            """ check for diagonal with increasing order"""
            # Two point apporach, BFS is perfect suit here
            i, j = row, col
            player = self._board[row][col]
            while count < 4 and i > -1 and j > -1 :
                if self._board[i][j] == self._board[i+1][j+1]:  
                    i, j = i+1, j+1 
                else:
                    return ""
                count += 1
            return player

        def check_winning_cond(self):
            for i in range(self._board_size):
                row_result  = self.row_matches(i)
                if row_result: 
                    print("Winner: ", row_result)
                    return True

                col_result = self.col_matches(j)
                if col_result: 
                    print("Winner: ", col_result)
                    return True

            for i in range(self._board_size):
                for j in range(self._board_size):
                    r1 = matches_dig1(i, j)
                    if r1:  
                        print("Winner: ", r1)
                        return True
                    r2 = matches_dig2(i, j)
                    if r2:
                        print("Winner: ", r2)
                        return True
            if self.check_empty():
                return False
            return True


        def check_empty(self):
            for i in range(len(self._board)):
                for j in range(len(self._board[0])):
                    if self._board[i][j] == 0:
                        return False
            return True

        def print_board(self):
            """ print a current state of board """

            for i in range(len(self._board)):
                for j in range(len(self._board[0])):
                    print(self._board[i][j] + ",")
                print("\n")



c4 = Connect4(6)
c4.init_first_ball()
while True:
    if c4._is_computer: 
        col = input("select: ")
        c4.user_input(col)
        c4.udpate_user(False)
    elif not c4._is_computer: 
        col = randint(0, c4._board_size -1) 
        c4.user_input(col)
        c4.udpate_user(True)
    c4.print_board()
    if c4.check_winning_cond(): break

