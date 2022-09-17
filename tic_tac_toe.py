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
    
    # set up while loop for multi-game play
    while multi_play:
        
        # declare empty game_list
        game_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        # determine if x or o goes first using random number
        first = random.randint(0,1)
        if first == 0:
            player = "x"
        else:
            player = "y"

        # set up game loop to run until there is a winner or a draw
        while game_loop:

            # display current game state
            display(game_list)
            validate = True   
            
            # loop until a valid input is given
            while validate:
            
                # display player's turn, error check the input, insert into game list
                position = input(f"\nIt is {player}'s turn. Choose untaken spot: ")
                if position.isdigit():
                    position = int(position)
                    if position >= 1  and position < 10:
                        position -= 1
                        if game_list[position] != "x" and game_list[position] != "y":
                            game_list[position] = player
                            validate = False
                            
                            # change player's turn 
                            if player == "x":
                                player = "y"
                            else:
                                player = "x"

                            # check for winner
                            result = winner_check(game_list)
                            if result != "s":
                                game_loop = False
                        else:
                            print("You can't choose a spot already taken!")
                    else:
                        print("Choice must be a valid number!")
                else:
                    print("Choice must be a number!")
                            
        # display game outcome
        if result == "d":
            print("\nThe game is a draw!\n")
        else:
            print(f"\nThe winner is {result}!\n")  
        display(game_list)          

        # ask player if they want to play again, set multi_play accordingly
        play = input("\nWould you like to play again y/n? ")
        if play.lower() == "n":
            multi_play = False   
            print() 
        else:
            game_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            game_loop = True
            print()
    
    # print out who won
    

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
        elif game_list[i] == "y" and game_list[i + 1] == "y" and  game_list[i + 2] == "y":
            return "y"
    
    # loop to see if a player has won by getting three in a row vertically,
    # if so, return winner
    for i in range(0, 3):
        if game_list[i] == "x" and game_list[i + 3] == "x" and  game_list[i + 6] == "x":
            return "x"
        elif game_list[i] == "y" and game_list[i + 3] == "y" and  game_list[i + 6] == "y":
            return "y"
    
    # loop to see if a player has won by getting one of the diagonals, if so
    # return winner
    if game_list[0] == "x" and game_list[4] == "x" and  game_list[8] == "x":
        return "x"
    elif game_list[2] == "x" and game_list[4] == "x" and  game_list[6] == "x":
        return "x"
    elif game_list[0] == "y" and game_list[4] == "y" and  game_list[8] == "y":
        return "y"
    elif game_list[2] == "y" and game_list[4] == "y" and  game_list[6] == "y":
        return "y"
    
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
    # display current game before move, indicate which player's turn it is
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("\n-+-+-")
        print(game_list[i], end="")
        if i != 2 and i != 5 and i != 8:
            print("|", end="")
    print()

# run main unless imported
if __name__ == "__main__":
    main()