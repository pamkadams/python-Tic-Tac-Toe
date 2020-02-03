# First Tic Tac Toe Game in Python by Pam Adams 2020

#############functions###############
def setup_game():
    #dictionary to record X/O selected squares
    game = {1:" ",
        2:" ",
        3:" ",
        4:" ",
        5:" ",
        6:" ",
        7:" ",
        8:" ",
        9:" ",}

    return game


def create_game_board(game):
    # function: to display current game
    print("TIC TAC TOE")
    print("Select the square by typing the corresponding number")
    print(' 1 2 3 \n 4 5 6 \n 7 8 9\n')
    divider = '_' * 7
    print(f"{game[1]}|{game[2]}|{game[3]}|")
    print(divider)
    print(f"{game[4]}|{game[5]}|{game[6]}|")
    print(divider)
    print(f"{game[7]}|{game[8]}|{game[9]}|")


def print_game_board(board):
    #updates with latest user square selection and prints board
    divider = '_' * 7
    print(f"{board[1]}|{board[2]}|{board[3]}|")
    print(divider)
    print(f"{board[4]}|{board[5]}|{board[6]}|")
    print(divider)
    print(f"{board[7]}|{board[8]}|{board[9]}|\n")



def user_choice(player, board):
    #allows user input for square selection
    print('user is', player)
    square = input("What is your next move? ")
    location_by_num = int(square)
    #ensures square is available
    picking = True
    while picking:
        if board[location_by_num] != 'X' or board[location_by_num] != 'O':
            board[location_by_num] = player
            picking = False
        else:
            location_by_num = input("Please select a valid move")
    return (board)

def check_for_win(player, board):
    #runs existing gameboard through solution for the current user and returns true for a winning solution or tie otherwise false to keep play going
    solutions = [[1,2,3],
    [1,4,7],
    [1,5,9],
    [2,5,8],
    [3,6,9],
    [3,5,7],
    [4,5,6],
    [7,8,9]]

    for solution in solutions:
        if board[solution[0]] == player and board[solution[1]] == player and board[solution[2]] == player:
            print(f'Congratulations, {player}! You have won.')
            return True
        elif " " not in board.values():
            print('Tie! Sorry no winner.')
            return True
    return False


def win_routine(player, board):
    #input for quitting or contining to play and resetting the board
    play_again = input('Play again?')
    if play_again == 'yes':
        board.clear()
        return True
    else:
        return False
  



#############game logic#############
#control flow boolean to control when to play or stop
play_game = True

#setup game with two functions one that stores the move and the other that displays the board
game = setup_game()
game_board = create_game_board(game)
#set user turn
user = 'O'

#playing the game - functions that happen every turn
while play_game:
#display game board
    print_game_board(game)
#user selects square
    if user == 'X':
        user = user.replace('X', 'O')
    else:
        user = user.replace('O', 'X')
    user_choice(user, game)
#display updated game board
    print_game_board(game)
#check for win
    if check_for_win(user, game):
        play_again = win_routine(user, game)
#reset game or terminate game
        if play_again:
            game = setup_game()
            game_board = create_game_board(game)
        else:
            play_game = False
#terminate game
print("Thank you for playing! Good bye")
