# Ash Bhuiyan                                          7-4-2025
# Assignment #3
#
# This is a simple version of the game NIM, renamed as NIMGRAB!

import random

def print_header():
    print("\nNIMGRAB!")
    print("By: Ash Bhuiyan")
    print("[COM S 127 1]")

def show_rules():
    print("\n              NIMGRAB! GAME RULES")
    print("1. You can play against a friend or the computer.")
    print("2. The game starts with 20 to 25 items.")
    print("3. Each player removes 1, 2, or 3 items on their turn.")
    print("4. You can't take more items than what's left.")
    print("5. Whoever takes the LAST item loses!")
    print("6. The menu will show up again after the game ends.\n")

def show_items(left):
    print("Items left:", left)
    print("| " * left)

def valid_input(prompt, min_value, max_value, max_allowed):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value or value > max_allowed:
                print("ERROR: Invalid choice. Please choose again.")
            else:
                return value
        except:
            print("ERROR: Invalid choice. Please choose again.")

def computer_turn(left, min_value, max_value):
    if left == 1:
        return 1
    elif left <= max_value:
        return left - 1
    else:
        # picking a no. from 1, 2, or 3
        return random.choice([1, 2, 3])

def run_game(vs_pc):
    total = random.randint(20, 25)
    min_value = 1
    max_value = 3
    player_turn = 0

    while total > 0:
        show_items(total)

        if vs_pc and player_turn == 1:
            move = computer_turn(total, min_value, max_value)
            print("\nComputer takes:", move, "\n")
        else:
            if not vs_pc:
                player = "Player 1" if player_turn == 0 else "Player 2"
            else:
                player = "You"
            move = valid_input(f"{player}, how many items do you want to take [{min_value}-{max_value}]?: ", min_value, max_value, total)

        total -= move

        if total == 0:
            if vs_pc:
                if player_turn == 1:
                    print("Computer took the last item. You win!\n")
                else:
                    print("You took the last item. Computer wins!\n")
            else:
                loser = "Player 1" if player_turn == 0 else "Player 2"
                winner = "Player 2" if player_turn == 0 else "Player 1"
                print(f"{loser} took the last item. {winner} wins!\n")
            break

        player_turn = 1 - player_turn

def main():
    print_header()
    while True:
        choice = input("\nDo you want to [p]lay, read the [r]ules, or [q]uit?: ")
        if choice == 'p':
            mode = input("Play against [h]uman or [c]omputer?: ")
            if mode == 'h':
                run_game(False)
            elif mode == 'c':
                run_game(True)
            else:
                print("Invalid option. Going back to menu.")
        elif choice == 'r':
            show_rules()
        elif choice == 'q':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
