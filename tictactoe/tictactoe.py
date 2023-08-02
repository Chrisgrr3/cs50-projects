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
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == X:
                xCount += 1
            elif board[row][column] == O:
                oCount += 1

    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(0, len(board)):
        for column in range(0, len(board[row])):
            if board[row][column] == EMPTY:
                possible_moves.add((row, column))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_copy = copy.deepcopy(board)

    board_copy[action[0]][action[1]] = player(board)
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check winner diagonally
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for row in range(0, len(board)):
        # Check winner horizontally
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            return board[row][0]
        # Check winner vertically
        if row == 0:
            for column in range(len(board[row])):
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
    if winner(board) is not None or (
        not any(EMPTY in sublist for sublist in board) and winner(board) is None
    ):
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
    current_player = player(board)
    if terminal(board):
        return None
    else:
        if current_player == X:
            value, move = max_val(board)
            return move
        else:
            value, move = min_val(board)
            return move


def max_val(board):
    if terminal(board):
        return utility(board), None
    value = float("-inf")
    move = None
    for action in actions(board):
        aux, act = min_val(result(board, action))
        if aux > value:
            value = aux
            move = action
            if value == 1:
                return value, move

    return value, move


def min_val(board):
    if terminal(board):
        return utility(board), None
    value = float("inf")
    move = None
    for action in actions(board):
        aux, act = max_val(result(board, action))
        if aux < value:
            value = aux
            move = action
            if value == -1:
                return value, move
    return value, move
