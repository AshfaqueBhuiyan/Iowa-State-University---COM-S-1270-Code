# Ash Bhuiyan                                    07-22-2025
# Lab #9 - Unit tests for checkWinner, checkDraw, checkForNextMoveWin, and checkAdjacent functions in fourInSequence.py using pytest.

import pytest
from fourInSequence import checkWinner, checkDraw, checkForNextMoveWin, checkAdjacent, getPlayerPiece, placePiece, getOpenRow

@pytest.fixture
def empty_board():
    return [
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "."]
    ]

def test_checkWinner_horizontal(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    for col in range(0, 4):
        placePiece(board, 5, col, piece)
    assert checkWinner(board, 1) == True
    assert checkWinner(board, 2) == False

def test_checkWinner_vertical(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    for row in range(2, 6):
        placePiece(board, row, 0, piece)
    assert checkWinner(board, 1) == True
    assert checkWinner(board, 2) == False

def test_checkWinner_diagonal_negative(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    for i in range(4):
        placePiece(board, 5 - i, i, piece)
    assert checkWinner(board, 1) == True
    assert checkWinner(board, 2) == False

def test_checkWinner_diagonal_positive(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    for i in range(4):
        placePiece(board, 2 + i, i, piece)
    assert checkWinner(board, 1) == True
    assert checkWinner(board, 2) == False

def test_checkWinner_no_win(empty_board):
    board = empty_board
    assert checkWinner(board, 1) == False
    assert checkWinner(board, 2) == False

def test_checkDraw_full_board():
    board = [
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"],
        ["X", "O", "X", "O", "X", "O", "X"],
        ["O", "X", "O", "X", "O", "X", "O"]
    ]
    assert checkDraw(board) == True

def test_checkDraw_not_full(empty_board):
    board = empty_board
    placePiece(board, 5, 0, getPlayerPiece(1))
    assert checkDraw(board) == False

def test_checkForNextMoveWin_horizontal(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    for col in range(1, 4):
        placePiece(board, 5, col, piece)
    assert checkForNextMoveWin(board, 1) == 0  # Placing in column 0 wins
    assert checkForNextMoveWin(board, 2) == -1

def test_checkForNextMoveWin_no_win(empty_board):
    board = empty_board
    assert checkForNextMoveWin(board, 1) == -1
    assert checkForNextMoveWin(board, 2) == -1

def test_checkAdjacent_with_adjacent(empty_board):
    board = empty_board
    piece = getPlayerPiece(1)  # "X"
    placePiece(board, 5, 1, piece)
    result = checkAdjacent(board, 1)
    assert result in [0, 1, 2]

def test_checkAdjacent_no_adjacent(empty_board):
    board = empty_board
    result = checkAdjacent(board, 1)
    assert result == -1