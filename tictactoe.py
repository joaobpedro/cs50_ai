"""
Tic Tac Toe Player
"""

from ctypes import util
import math
from telnetlib import X3PAD

import copy

from numpy import Infinity

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

    if terminal(board):
        return None
    
    num_X = 0
    num_O = 0

    for row in board:
        for col in row:
            if col == X:
                num_X += 1
            elif col == O:
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

    if terminal(board):
        return None

    actions = set()

    for i in range(len(board[0])):
        #this assumes the board is square
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #cheack action
    if board[action[0]][action[1]] != EMPTY:
        raise ('this move is not possible')

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check rows
    for row in board:
        if len(set(row)) == 1:
            if X in set(row):
                return X
            elif O in set(row):
                return O
    
    #check columns   
    for i in range(len(board[0])):
        column = set()
        for row in board:
            column.add(row[i])
    
        if len(column) == 1:
            if X in column:
                return X
            elif O in column:
                return O
    
    #check diagonals
    diagonal1 = set()
    diagonal2 = set()
    for i in range(len(board[0])):
        
        diagonal1.add(board[i][i])
        diagonal2.add(board[i][-i-1])
        
    #check first diagonal
    if len(diagonal1) == 1:
        if X in diagonal1:
            return X
        elif O in diagonal1:
            return O

    #check second diagonal
    if len(diagonal2) == 1:
        if X in diagonal2:
            return X
        elif O in diagonal2:
            return O

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #will use the utility function as well

    list_of_board = [x for row in board for x in row]

    if winner(board) is not None:
        return True
    elif EMPTY not in list_of_board:
        return True
    else:
        return False    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            bestScore = -Infinity
            bestMove = ()
            for action in actions(board):
                board_i = result(board, action)
                score = minimax_aux(board_i, 0, False)
                if (score > bestScore):
                    bestScore = score
                    bestMove = action
            return bestMove
        elif player(board) == O:
            bestScore = Infinity
            bestMove = ()
            for action in actions(board):
                board_i = result(board, action)
                score = minimax_aux(board_i, 0, True)
                if (score < bestScore):
                    bestScore = score
                    bestMove = action
            return bestMove
  


def minimax_aux(board, depth, isMaximizing):
    #stop condition
    if terminal(board):
        return utility(board)

    if (isMaximizing):
        bestScore = -Infinity
        for action in actions(board):
            board_i = result(board, action)
            score = minimax_aux(board_i, depth + 1, False)
            if (score > bestScore):
                bestScore = score
        return bestScore

    else:
        bestScore = Infinity
        for action in actions(board):
            board_i = result(board, action)
            score = minimax_aux(board_i, depth + 1, True)
            if (score < bestScore):
                bestScore = score
        return bestScore
