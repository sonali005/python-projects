def make_board(rows,column,default_value):
    board = [[" " for row in range(3)] for col in range(3)]

    for row in board:
        print(row)

def print_board():
    row = 3
    column = 3
    default = " "
    return make_board(row,column,default_value)

def make_move(board, symbol):
    while True:
        try:
            row = int(input(f"player {symbol} enter your move row(0-2): "))
            column = int(input(f"player {symbol} enter your move column(0-2): "))

            if board[row][column] == " ":
                board[row][column] = symbol
                print_board[board]
                break
            else:
                print("This place is already taken.. Try Again")
        except (ValueError, IndexError):
            print("Invalid input...Please enter row and column as integers between 0 and 2")

def main():
    row = 3
    column = 3
    default = " "

    board = make_board(row,column,default)
    print("Tic Tac Toe Board")

    print_board()

    make_move(board, "X")
    make_move(board, "O")
main()
