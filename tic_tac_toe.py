import random

board = [' ' for _ in range(9)]

def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_win(player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                      (0, 4, 8), (2, 4, 6)]             # Diagonals
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def check_full():
    return ' ' not in board

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is taken!")
        except (ValueError, IndexError):
            print("Please enter a valid move.")

def computer_move():
    empty_spots = [i for i, spot in enumerate(board) if spot == ' ']
    move = random.choice(empty_spots)
    board[move] = 'O'

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    print_board()

    while True:
        # Player's turn
        player_move()
        print_board()
        if check_win('X'):
            print("You win!")
            break
        if check_full():
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer's turn:")
        computer_move()
        print_board()
        if check_win('O'):
            print("Computer wins!")
            break
        if check_full():
            print("It's a tie!")
            break

# Start the game
tic_tac_toe()
