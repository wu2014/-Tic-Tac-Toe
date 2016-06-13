import os

clear = lambda: os.system('cls')

# Global variables
board = [' '] * 10
game_state = True
result = ''

# Note: Game will ignore the 0 index
def reset_board():
    global board,game_state
    board = [' '] * 10
    game_state = True

def display_board():
    # This function prints out the board
    # Clear current cell output
    clear()
    # Print board
    print ("\n")
    print ("  "+board[7]+" |"+board[8]+" | "+board[9]+" ")
    print ("------------")
    print ("  "+board[4]+" |"+board[5]+" | "+board[6]+" ")
    print ("------------")
    print ("  "+board[1]+" |"+board[2]+" | "+board[3]+" ")


def is_winner(board, player):
    # Check Horizontals,Verticals, and Diagonals for a win 
    if (board[7]  ==  board[8] ==  board[9] == player) or \
        (board[4] ==  board[5] ==  board[6] == player) or \
        (board[1] ==  board[2] ==  board[3] == player) or \
        (board[7] ==  board[4] ==  board[1] == player) or \
        (board[8] ==  board[5] ==  board[2] == player) or \
        (board[9] ==  board[6] ==  board[3] == player) or \
        (board[1] ==  board[5] ==  board[9] == player) or \
        (board[3] ==  board[5] ==  board[7] == player):
        return True
    else:
        return False    

def full_board_check(board):
    # Function to check if any remaining blanks are in the board
    if " " in board[1:]:
        return False
    else:
        return True
def ask_player(mark):
    # Asks player where to place X or O mark, checks validity
    global board
    req = 'Choose where to place your: ' + mark + ' '
  
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print ("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print ("That space isn't empty!")
            continue

def player_choice(mark):
    global board,game_state,result
    #Set game blank game result
    result = ''
    #Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for player win
    if is_winner(board,mark):
        clear()
        display_board()
        result = mark +" wins! Congratulations!"
        game_state = False
    
    #Show board
    clear()
    display_board()

    #Check for a tie 
    if full_board_check(board):
        result = "Tie!"
        game_state = False
        
    return game_state, result

def play_game():
    reset_board()
    global result
    
    # Set marks
    X='X'
    O='O'
    while True:
        # Show board
        clear()
        display_board()
        
        # Player X turn
        game_state, result = player_choice(X)
        print (result)
        if game_state == False:
            break
            
        # Player O turn
        game_state,result = player_choice(O)
        print (result)
        if game_state == False:
            break
    
    # Ask player for palying again
    replay = input('Would you like to play again? y/n ')
    if replay == 'y':
        play_game()
    else:
        print ("Goodbye!")

play_game()
