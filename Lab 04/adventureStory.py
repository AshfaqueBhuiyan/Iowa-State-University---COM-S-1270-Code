# Ash Bhuiyan                                       07-02-2025
# Lab 4 - My mock version of Uncharted 3 as an adventure story

def main():
    print()
    print("Welcome to the Sands of Atlantis Adventure!")
    print("By: Ash Bhuiyan")
    print()
    print("You are Nathan Drake, deep in the Rub' al Khali desert, standing at the gates of a buried city.")
    direction = input("Do you go [left] toward the collapsed tower, [right] toward the echoing tunnel, or [forward] into the throne hall?: ")

    if direction == "left":
        print("You carefully approach the ruins of the tower. The structure creaks ominously.")
        action = input("Do you want to [climb] the tower remains or [inspect] the base?: ")
        if action == "climb":
            print("As you climb, the tower collapses! You barely make it out alive with an old map in hand.")
        elif action == "inspect":
            print("You discover ancient carvings and a hidden dagger beneath the sand.")

    elif direction == "right":
        print("You enter a dark tunnel. The air is cool, and your flashlight flickers.")
        choice = input("Do you [proceed] deeper or [turn] back?: ")
        if choice == "proceed":
            print("You find a hidden chamber filled with gold... and traps!")
        elif choice == "turn":
            print("You avoid danger, but miss a valuable clue.")

    elif direction == "forward":
        print("You step into the grand throne hall, echoing with history.")
        explore = input("Do you [examine] the throne or [search] the walls?: ")
        if explore == "examine":
            print("Under the throne you find T.E. Lawrence’s journal, revealing the city’s secrets!")
        elif explore == "search":
            print("You trigger a mechanism — the floor opens to reveal a spiral staircase!")

    else:
        print("You hesitate too long... a sandstorm blows in and buries the city again. Game over.")

if __name__ == "__main__":
    main()
