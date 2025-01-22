"""
Tic Tac Toe Player
"""

import math
import copy

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
    # raise NotImplementedError
    no_x = 0
    no_o = 0
    for row in board:
        for cell in row:
            if cell == X:
                no_x += 1
            elif cell == O:
                no_o += 1
    
    if no_o == no_x:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # raise NotImplementedError
    moves = set()
    for row, v1 in enumerate(board):
        for col, v2 in enumerate(v1):
            if v2 == EMPTY:
                moves.add((row, col))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # raise NotImplementedError
    if board[action[0]][action[1]] != EMPTY:
        raise Exception('invalid')

    newBoard = copy.deepcopy(board)
    if player(board) == X:
        newBoard[action[0]][action[1]] = X
    else:
        newBoard[action[0]][action[1]] = O
    
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    if board[0][0] == board[0][1] == board[0][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[1][0] == board[1][1] == board[1][2] and board[1][0] != EMPTY:
        return board[1][0]
    if board[2][0] == board[2][1] == board[2][2] and board[2][0] != EMPTY:
        return board[2][0]
    
    if board[0][0] == board[1][0] == board[2][0] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][1] == board[1][1] == board[2][1] and board[0][1] != EMPTY:
        return board[0][1]
    if board[0][2] == board[1][2] == board[2][2] and board[0][2] != EMPTY:
        return board[0][2]
    
    if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]) and board[1][1] != EMPTY:
        return board[1][1]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) == X or winner(board) == O:
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    else:
        raise Exception('game has not finished yet!')

def myFunc(board):
    finalMove = None
    def recursive(lBoard):
        nonlocal finalMove
        if terminal(lBoard):
            return utility(lBoard)
        if player(lBoard) == X:
            score = -10
        else:
            score = 10
        for move in actions(lBoard):
            tmp = recursive(result(lBoard, move))

            
            if player(lBoard) == X:
                if tmp > score:
                    score = tmp
                    if lBoard == board:
                        finalMove = move
            else:
                if tmp < score:
                    score = tmp
                    if lBoard == board:
                        finalMove = move
        
        return score
    
    recursive(board)
    return finalMove

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # raise NotImplementedError
    return myFunc(board)

