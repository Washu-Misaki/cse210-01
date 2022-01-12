"""
Filename: tictactoe.py

Author: Daniel Jones
Purpose:  2-Player Tic-Tac-Toe game.
"""

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board) or draw_game(board)):
        show_board(board)
        take_turn(player, board)
        player = next_player(player)
    show_board(board)
    if has_winner(board):
        player = next_player(player)
        print(f"Congratulations!  {player} is the winner!")
    elif draw_game(board):
        print("No winner, but a well played match!  GG!")
    print("Thank you for playing!") 


def create_board():
    # Create a 3x3 grid board as a list
    board = []
    for square in range(9):
        # Modify the board numbers to match a calculator's grid in appearance
        board.append(square + 1)
    return board


def show_board(board):
    # Display the board in its current state
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def take_turn(player, board):
    # Process a player's turn and change the value of the board-list
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    if player == 'x':
        color = '\033[1;31;40m'
    elif player == 'o':
        color = '\033[1;34;40m'
    default_color = '\033[0;37;40m'
    board[square - 1] = color + player + default_color


def next_player(current):
    # Switch current player
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"


def draw_game(board):
    # Conclude a game with no empty squares and no winner
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 


def has_winner(board):
    # Conclude a game with a clear winner
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])


if __name__ == "__main__":
    main()