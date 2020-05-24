# Exercise 1
import numpy as np
import random

def create_board():
    return np.zeros((3,3), dtype=int)

board = create_board()
board


# Exercise 2
def place(board, player, position):
    if board[position] == 0:
        board[position] = player

place(board , 1 , (0,0))

board


# Exercise 3
def possibilities(board):
    not_occupied = np.where(board == 0)
    return list(zip(not_occupied[0], not_occupied[1]))

possibilities(board)


# Exercise 4
import random 
random.seed(1)

def random_place(board, player):
    available_places = possibilities(board)
    x = random.choice(available_places)
    place(board, player, x)
    
random_place(board, 2)

board


# Exercise 5
random.seed(1)
board = create_board()

random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)
random_place(board, 1)
random_place(board, 2)

board


# Exercise 6
def row_win(board, player):
    for row in range(0, len(board)):
        if all(place == player for place in board[row]):
            return True
        
    return False;

row_win(board, 1)


# Exercise 7
def col_win(board, player):
    return row_win(board.T, player)

col_win(board, 1)


# Exercise 8
board[1,1] = 2

def diag_win(board, player):
    diagonal_values = np.diagonal(board)
    anti_diag = np.flipud(board).diagonal()[::-1]
    return all(place == player for place in diagonal_values) or all(place == player for place in anti_diag)

diag_win(board, 2)


# Exercise 9
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
            pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)


# Exercise 10
random.seed(1)

def play_game():
    board = create_board()
    game_result = 0
    while game_result == 0:
        for player in [1,2]:
            random_place(board, player)
            game_result = evaluate(board)
            if game_result != 0:
                break
    return game_result


game_results = []
for time in range(0,1000):
    game_results.append(play_game())
    
game_results.count(1)



# Exercise 11
random.seed(1)
  
def play_strategic_game():
    board, game_result = create_board(), 0
    board[(1,1)] = 1
    while game_result == 0:
        for player in [2,1]:
            random_place(board, player)
            game_result = evaluate(board)
            if game_result != 0:
                break
    return game_result

strategic_game_results = []
for time in range(1000):
    strategic_game_results.append(play_strategic_game())
    
strategic_game_results.count(1)