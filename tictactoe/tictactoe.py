"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for row in board:
        for column in board[row]:
            if board[row][column] != EMPTY:
                count += 1

    if count % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in board:
        for column in board[row]:
            if board[row][column] == EMPTY:
                possible_moves.add((row, column))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy

    current_player = player(board)
    board_copy = copy.deepcopy(board)
    if action not in actions(board):
        raise Exception("That is not a valid move")
    else:
        row = action[0]
        column = action[1]
        board_copy[row][column] = current_player
        return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check for diagonal winner
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for row in board:
        # Check winner horizontally
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return board[row][0]
        # Check winner vertically
        if row == 0:
            for column in board[row]:
                if (
                    board[row][column] == board[row + 1][column]
                    and board[row + 1][column] == board[row + 2][column]
                ):
                    return board[row][column]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    current_player = player(board)
    if winner(board) == None and len(actions(board)) == 0:
        return True
    elif winner(board) == None and len(actions(board)) != 0:
        return False
    elif winner(board) != None:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
