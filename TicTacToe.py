import os
import random

def display_board(board):
    # Display the board
    # board is 3x3 list
    os.system('cls')

    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print("-----")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print("-----")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

def player_input():
    # First player chooses the marker

    marker = ""
    
    while marker not in ("x","o"):
        marker = input("Choose your marker(x or o): ")
        
    if marker == "x":
        return ("x","o")
    else:
        return ("o","x")

def place_marker(board,marker,position):
    # Takes in the board list, a marker, and a position
    # Assigns that position to the board
    
    if position in range(1,4):
        board[0][position-1] = marker
    if position in range(4,7):
        board[1][position-4] = marker
    if position in range(7,10):
        board[2][position-7] = marker
        
    return board

def win_check(board,mark):
    # Check to see if a player has won the game
    
    win = False
    
    # Check if a row has only the same marker
    if (board[0][0]==mark and board[0][1]==mark and board[0][2]==mark):
        win = True
    if (board[1][0]==mark and board[1][1]==mark and board[1][2]==mark):
        win = True
    if (board[2][0]==mark and board[2][1]==mark and board[2][2]==mark):
        win = True
        
    # Check if a column has only the same marker
    if (board[0][0]==mark and board[1][0]==mark and board[2][0]==mark):
        win = True
    if (board[0][1]==mark and board[1][1]==mark and board[2][1]==mark):
        win = True
    if (board[0][2]==mark and board[1][2]==mark and board[2][2]==mark):
        win = True

    # Check if a diagonal has only the same marker
    if (board[0][0]==mark and board[1][1]==mark and board[2][2]==mark):
        win = True
        
    if (board[0][2]==mark and board[1][1]==mark and board[2][0]==mark):
        win = True
        
    return win

def choose_first():
    # Randomly decide which player goes first
    
    flip = random.randint(1,2)
    
    if flip == 1:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    # Check to see if a position on the board is available
    
    check_free = True
    
    if position in range(1,4) and board[0][position-1] != ' ':
        check_free = False
    elif position in range(4,7) and board[1][position-4] != ' ':
        check_free = False
    elif position in range(7,10) and board[0][position-7] != ' ':
        check_free = False
    else:
        check_free = True
    
    return check_free

def full_board_check(board):
    # Check to see if the board is full
        
    if ' ' in board[0]:
        return False
    elif ' ' in board[1]:
        return False
    elif ' ' in board[2]:
        return False
    else:
        return True

def player_choice(board):
    # Ask the player's next position
    # Uses space_check
        
    position = 0
    
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Choose a position (1-9): "))
        
    return position

def replay():
    # Ask the players if they want to play again
    
    play_again = ""
    
    while play_again not in ["y","n"]:
        play_again = input("Do you wish to play again (y/n): ")
        
        if play_again == "y":
            return True
        elif play_again == "n":
            return False
        else:
            print("Invalid input.")

# Game logic

print("Welcome to Tic Tac Toe!")

while True:
    # Game set up
    
    board=[["1","2","3"],["4","5","6"],["7","8","9"]]
    
    turn = choose_first()
    print(turn+" will go first.")
    if turn == "Player 1":
        marker1,marker2 = player_input()
    else:
        marker2,marker1 = player_input()
    
    # Begin game
    play_game = input("Ready to play (y or n)? ")
    
    if play_game == "y":
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn == "Player 1":
            if not(win_check(board,marker2)):
                if not(full_board_check(board)):
                    display_board(board)
                    print("Player 1")
                    position = player_choice(board)
                    board = place_marker(board,marker1,position)
                    turn = "Player 2"
                else:
                    print("It's a tie.")
                    game_on = False
            else:
                print("Player 2 wins.")
                game_on = False
                
        if turn == "Player 2":
            if not(win_check(board,marker1)):
                if not(full_board_check(board)):
                    display_board(board)
                    print("Player 2")
                    position = player_choice(board)
                    board = place_marker(board,marker2,position)
                    turn = "Player 1"
                else:
                    print("It's a tie.")
                    game_on = False
            else:
                print("Player 1 wins.")
                game_on = False

    if not replay():
        break