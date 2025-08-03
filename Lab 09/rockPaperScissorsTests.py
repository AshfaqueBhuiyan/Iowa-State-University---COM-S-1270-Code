# Ash Bhuiyan                                    07-23-2025
# Lab #9 - Unit tests for rockPaperScissors.py functions using pytest, following TDD principles.

import pytest
from rockPaperScissors import generateComputerMove, determineWinner, playRound

def test_generateComputerMove():
    move = generateComputerMove()
    assert move in ["Rock", "Paper", "Scissors"]

def test_determineWinner():
    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("Rock", "Scissors") == "Rock"
    assert determineWinner("Paper", "Scissors") == "Scissors"
    assert determineWinner("Paper", "Rock") == "Paper"
    assert determineWinner("Scissors", "Rock") == "Rock"
    assert determineWinner("Scissors", "Paper") == "Scissors"
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Paper", "Paper") == "Draw"
    assert determineWinner("Scissors", "Scissors") == "Draw"

def test_playRound(monkeypatch):
    def mock_generateComputerMove():
        return "Paper"
    monkeypatch.setattr("rockPaperScissors.generateComputerMove", mock_generateComputerMove)
    assert playRound("Rock") == "Computer Wins"
    assert playRound("Scissors") == "Computer Wins"
    assert playRound("Paper") == "Draw"