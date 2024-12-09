import random

def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def play_game():
    board = initialize_board()
    players = ["X", "O"]
    current_player = random.choice(players)
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        if current_player == "X":
            while True:
                try:
                    move = input("Enter your move as row,col (e.g., 1,1): ")
                    row, col = map(int, move.split(","))
                    if make_move(board, row, col, current_player):
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Invalid input. Enter row,col (e.g., 1,1).")
        else:
            move = random.choice(get_available_moves(board))
            make_move(board, move[0], move[1], current_player)
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

play_game()