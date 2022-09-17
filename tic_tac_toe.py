"""
File: tic_tac_toe.py
Assignment - W01 Prove: Developer 
Author: Jerry Lane
Requirements: 
    The program must have a comment with assignment and author names.
    The program must have at least one if/then block.
    The program must have at least one while loop.
    The program must have more than one function.
    The program must have a function called main.
"""
import random

# main function to drive program
def main():
    """
    parameter: none
    returns: nothing
    main function sets player order, gets player input, calls make move
    function, calls winner_check to see if a player has won, and shows the
    game a win for one of the players or a draw.
    """
    # declare default variables
    multi_play = True
    game_loop = True
    result = ""
    game_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # set up while loop for multi-game play
    while multi_play:        
        
        # randomly determine if x or o goes first
        first = random.randint(0,2)
        if first == 0:
            player = "x"
        else:
            player = "o"

        # set up game loop to run until there is a winner or a draw
        while game_loop:

            # display current game state
            display(game_list)
            validate = True   
            
            # loop until a valid input is given, then take the appropriate actions
            while validate:
            
                # display player's turn, error check the input, insert into game list
                position = input(f"\nIt is {player}'s turn. Choose an untaken spot: ")
                if is_valid(position, game_list):
                    position = int(position) - 1
                    game_list[position] = player
                    validate = False
                            
                    # change player's turn 
                    if player == "x":
                        player = "o"
                    else:
                        player = "x"

                    # check for winner
                    result = winner_check(game_list)
                    
                    # if the response is anything but space available, end game loop
                    if result != "s":
                        game_loop = False
                            
        # display game outcome
        show_outcome(result)
        display(game_list)        

        # ask player if they want to play again, set multi_play accordingly
        play = input("\nWould you like to play again y/n? ")
        if play.lower() != "y":
            print("Thanks for playing Tic Tac Toe!")
            multi_play = False   
            print() 
        else:
            game_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            game_loop = True

# function to check to see if game has been won, returns player who won
def winner_check(game_list):
    """
    parameters: game_list - contains the list of game data
    returns: x, o, d, or s
    winner_check will accept the game_list, check for a win horizontally,
        vertically, or diagonally. if x or o has won, it returns the winner.
        if the game is filled but no one has won, it returns a d for draw.
        if the game has no winner but is not filled, it returns an s for space
        available.
    """
    # loop to see if a player has won by getting three in a row horizontally,
    # if so, return winner
    for i in range(0, 9, 3):
        if game_list[i] == "x" and game_list[i + 1] == "x" and  game_list[i + 2] == "x":
            return "x"
        elif game_list[i] == "o" and game_list[i + 1] == "o" and  game_list[i + 2] == "o":
            return "o"
    
    # loop to see if a player has won by getting three in a row vertically,
    # if so, return winner
    for i in range(0, 3):
        if game_list[i] == "x" and game_list[i + 3] == "x" and  game_list[i + 6] == "x":
            return "x"
        elif game_list[i] == "o" and game_list[i + 3] == "o" and  game_list[i + 6] == "o":
            return "o"
    
    # loop to see if a player has won by getting one of the diagonals, if so
    # return winner
    if game_list[0] == "x" and game_list[4] == "x" and  game_list[8] == "x":
        return "x"
    elif game_list[2] == "x" and game_list[4] == "x" and  game_list[6] == "x":
        return "x"
    elif game_list[0] == "o" and game_list[4] == "o" and  game_list[8] == "o":
        return "o"
    elif game_list[2] == "o" and game_list[4] == "o" and  game_list[6] == "o":
        return "o"
    
    # if game_list has an open space, return s indicating a space can be chosen
    for i in range(9):
        if game_list[i].isdigit():
            return "s"
    
    # return d for draw
    return "d"

# function to display game
def display(game_list):
    """
    parameters: game_list
    return: nothing
    display accepts the game list and displays the game in the terminal
    """
    # set color to white
    color = 29 

    # display clean line
    print()
    
    # display current game before move, indicate which player's turn it is
    for i in range(9):
        if game_list[i] == "x":
            color = 34
        elif game_list[i] == "o":
            color = 35
        else:
            color = 29
        if i % 3 == 0 and i != 0:
            print("\n-+-+-")
        print(f"\033[0;{color}m{game_list[i]}\033[00m", end="")
        if i != 2 and i != 5 and i != 8:
            print("|", end="")
    print()

# function to validate user input
def is_valid(user, game_list):
    """
    parameter: user - user input checked for validity
    return: bool indicating the input is valid or invalid
    This function will accept a user input, check it see if it is valid,
    (meaning it is a number between 1 and 9 and the spot is not already
    taken), and then it will return a bool indicating whether or not
    the input is valid. it will also display any error messages which 
    are needed.
    """
    if user.isdigit():
        user = int(user)
        if user >= 1 and user < 10:
            user -= 1
            if game_list[user] != "x" and game_list[user] != "o":
                return True
            else:
                print("You can't choose a spot already taken!")
        else:
            print("Choice must be a number between 1 and 9!")
    else:
        print("Choice must be an integer number!")
    return False

# function to show game outcome
def show_outcome(result):
    """
    parameter: result - response from the winner_check function
    return: nothing
    This function will accept the result from the winner_check function
    and display the outcome of o wins, x wins, or the game is a draw.
    """
    if result == "d":
        print("\nThe game is a ", end="")
        print("\033[0;31mDRAW\033[00m", end="")
        print("!")
    else:
        if result == "x":
            print("\033[0;34m\nX\033[00m", end="")
        elif result == "o":
            print("\033[0;35m\nO\033[00m", end="")
        print(" is the ", end="")
        print("\033[0;32mWINNER\033[00m", end="")
        print("!")
  
# run main unless imported
if __name__ == "__main__":
    main()