import random

def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice(['H', 'T']))
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(' '.join(row))

def flip_coin(board, x, y):
    if x < 0 or x >= len(board) or y < 0 or y >= len(board):
        return
    if board[x][y] == 'H':
        board[x][y] = 'T'
    else:
        board[x][y] = 'H'
    flip_coin(board, x-1, y)
    flip_coin(board, x+1, y)
    flip_coin(board, x, y-1)
    flip_coin(board, x, y+1)

def play_game(size):
    board = create_board(size)
    print("Initial Board:")
    print_board(board)
    while True:
        x = int(input("Enter x coordinate (0-{}): ".format(size-1)))
        y = int(input("Enter y coordinate (0-{}): ".format(size-1)))
        flip_coin(board, x, y)
        print("After flip:")
        print_board(board)
        heads = sum(row.count('H') for row in board)
        tails = sum(row.count('T') for row in board)
        print("Heads: {}, Tails: {}".format(heads, tails))
        if heads == 0 or tails == 0:
            print("Game Over!")
            break

play_game(5)