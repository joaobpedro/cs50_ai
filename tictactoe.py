"""
Tic Tac Toe Player
"""

import math
from telnetlib import X3PAD

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #check if the board is the intial state
    
    num_X = 0
    num_O = 0

    for row in board:
        for col in row:
            if X in col:
                num_X += 1
            elif O in col:
                num_O += 1
    
    if num_X == 0  and num_O == 0:
        #the board is at initial state
        return X
    if num_X > num_O:
        #player X played last
        return O
    else:
        #player O played last
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    #check rows
    for row in board:
        if len(set(row)) == 1:
            if X in set(row):
                return 1
            elif O in set(row):
                return -1
    
    #check columns   
    for i in range(len(board[0])):
        column = set()
        for row in board:
            column.add(row[i])
    
    if len(column) == 1:
        if X in column:
            return 1
        elif O in column:
            return -1
    
    #check diagonals
    diagonal1 = set()
    diagonal2 = set()
    for i in range(len(board[0])):
        
        diagonal1.add(board[i][i])
        diagonal2.add(board[i][-i-1])
        
    #check first diagonal
    if len(diagonal1) == 1:
        if X in diagonal1:
            return 1
        elif O in diagonal1:
            return -1

    #check second diagonal
    if len(diagonal2) == 1:
        if X in diagonal2:
            return 1
        elif O in diagonal2:
            return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
