def start_game():
    print("Welcome to the Adventure Game!")
    print("You are lost in a dark forest.")
    first_choice()

def first_choice():
    print("\nYou have two paths in front of you:")
    print("1. Go left")
    print("2. Go right")
    choice = input("Make your choice (1 or 2): ")

    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    else:
        print("Invalid choice! Try again.")
        first_choice()

def go_left():
    print("\nYou go left and encounter a wolf!")
    print("What do you want to do?")
    print("1. Run away")
    print("2. Fight the wolf")
    choice = input("Make your choice (1 or 2): ")

    if choice == "1":
        run_away()
    elif choice == "2":
        fight_wolf()
    else:
        print("Invalid choice! Try again.")
        go_left()

def go_right():
    print("\nYou go right and see an abandoned castle.")
    print("What do you want to do?")
    print("1. Enter the castle")
    print("2. Continue exploring the forest")
    choice = input("Make your choice (1 or 2): ")

    if choice == "1":
        enter_castle()
    elif choice == "2":
        explore_forest()
    else:
        print("Invalid choice! Try again.")
        go_right()

def run_away():
    print("\nYou run away and reach a safe spot. You are saved!")

def fight_wolf():
    print("\nYou fight the wolf but unfortunately lose. Game over!")

def enter_castle():
    print("\nYou enter the abandoned castle and find a treasure map!")
    # Continue the story with more options here

def explore_forest():
    print("\nYou continue exploring the forest and find a cabin.")
    # Continue the story with more options here

# Start the game
start_game()
