import random

# Empty cells are represented by numbers 1 to 9
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


# Function to display the board
def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


# Function to check the winner
def check_winner(player):
    # Check rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Check columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Check diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False


# Function to find empty positions
def get_empty_positions():
    empty = []

    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            empty.append(i)

    return empty


# Random computer strategy
def random_move():
    empty = get_empty_positions()
    position = random.choice(empty)
    return position


# Intelligent computer strategy
def intelligent_move():
    empty = get_empty_positions()

    # Step 1: Try to win
    for position in empty:
        old_value = board[position]
        board[position] = computer

        if check_winner(computer):
            board[position] = old_value
            return position

        board[position] = old_value

    # Step 2: Block the human player
    for position in empty:
        old_value = board[position]
        board[position] = human

        if check_winner(human):
            board[position] = old_value
            return position

        board[position] = old_value

    # Step 3: Choose the center
    if 4 in empty:
        return 4

    # Step 4: Choose a corner
    corners = [0, 2, 6, 8]
    available_corners = []

    for position in corners:
        if position in empty:
            available_corners.append(position)

    if available_corners:
        return random.choice(available_corners)

    # Step 5: Choose any remaining position
    return random.choice(empty)


# Main program
print("WELCOME TO TIC-TAC-TOE")

# Choose X or O
while True:
    human = input("Choose your symbol (X or O): ").upper()

    if human == "X" or human == "O":
        break

    print("Invalid choice! Enter X or O.")

# Computer gets the remaining symbol
computer = "O" if human == "X" else "X"

print("You are", human)
print("Computer is", computer)

print("1. Random Move Strategy")
print("2. Intelligent Move Strategy")

while True:
    choice = input("Choose strategy (1 or 2): ")

    if choice == "1" or choice == "2":
        break

    print("Invalid choice! Enter 1 or 2.")


# Game loop
while True:
    display_board()

    # Human player's turn
    while True:
        try:
            move = int(input("Enter position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
            elif board[move - 1] == "X" or board[move - 1] == "O":
                print("This position is already occupied!")
            else:
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

    board[move - 1] = human

    # Check if human wins
    if check_winner(human):
        display_board()
        print("Congratulations! You won!")
        break

    # Check for draw
    if len(get_empty_positions()) == 0:
        display_board()
        print("The game is a draw!")
        break

    # Computer's turn
    if choice == "1":
        computer_position = random_move()
    else:
        computer_position = intelligent_move()

    board[computer_position] = computer

    print("Computer selected position:", computer_position + 1)

    # Check if computer wins
    if check_winner(computer):
        display_board()
        print("Computer wins! Better luck next time.")
        break

    # Check for draw
    if len(get_empty_positions()) == 0:
        display_board()
        print("The game is a draw!")
        break
