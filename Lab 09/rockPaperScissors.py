# Ash Bhuiyan                                    07-22-2025
# Lab #9 - A Rock-Paper-Scissors game where a human plays against the computer for an odd number of rounds, with early termination if one player wins more than half.

import random
import sys

def generateComputerMove():
    """
    Returns a randomly selected move: "Rock", "Paper", or "Scissors".
    """
    return random.choice(["Rock", "Paper", "Scissors"])

def determineWinner(player_move, computer_move):
    """
    Determines the winner of a round based on player and computer moves.
    Returns "Player" if player wins, "Computer" if computer wins, or "Draw" if tied.
    """
    if player_move == computer_move:
        return "Draw"
    if (player_move == "Rock" and computer_move == "Scissors") or \
       (player_move == "Paper" and computer_move == "Rock") or \
       (player_move == "Scissors" and computer_move == "Paper"):
        return "Player"
    return "Computer"

def playRound(player_move):
    """
    Plays a single round, taking player's move, generating computer's move, and determining the winner.
    Returns a string indicating the outcome: "Player Wins", "Computer Wins", or "Draw".
    """
    computer_move = generateComputerMove()
    result = determineWinner(player_move, computer_move)
    if result == "Player":
        return "Player Wins"
    elif result == "Computer":
        return "Computer Wins"
    return "Draw"

def get_valid_rounds():
    """
    Prompts user for an odd number of rounds.
    Returns the number of rounds.
    """
    while True:
        try:
            rounds = int(input("Enter number of rounds (must be odd): "))
            if rounds % 2 == 0:
                print("ERROR: Number of rounds must be odd.")
                continue
            if rounds <= 0:
                print("ERROR: Number of rounds must be positive.")
                continue
            return rounds
        except ValueError:
            print("ERROR: Please enter a valid integer.")

def get_valid_move():
    """
    Prompts user for a valid move (Rock, Paper, Scissors).
    Returns the capitalized move.
    """
    valid_moves = ["Rock", "Paper", "Scissors"]
    while True:
        move = input("Enter your move (Rock, Paper, Scissors): ").capitalize()
        if move in valid_moves:
            return move
        print("ERROR: Please enter Rock, Paper, or Scissors.")

def main():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    print("Welcome to Rock-Paper-Scissors!")
    rounds = get_valid_rounds()
    player_wins = 0
    computer_wins = 0
    max_wins = (rounds // 2) + 1  # Majority threshold

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        player_move = get_valid_move()
        result = playRound(player_move)
        print(f"Result: {result}")
        
        if result == "Player Wins":
            player_wins += 1
        elif result == "Computer Wins":
            computer_wins += 1

        if player_wins >= max_wins:
            print(f"\nPlayer wins the game! ({player_wins} vs {computer_wins})")
            return
        if computer_wins >= max_wins:
            print(f"\nComputer wins the game! ({computer_wins} vs {player_wins})")
            return

    print(f"\nFinal Score - Player: {player_wins}, Computer: {computer_wins}")
    if player_wins > computer_wins:
        print("Player wins the game!")
    elif computer_wins > player_wins:
        print("Computer wins the game!")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    main()