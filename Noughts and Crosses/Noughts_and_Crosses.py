
# This is a program to play noughts and crosses

def Board(boardMarks): # Function for creating the board in the console with a dictionary for marks made on the board
    
    print("    A   B   C  ")
    print("  +---+---+---+")
    print("1 | " + boardMarks["a1"]+ " | " + boardMarks["b1"] + " | " + boardMarks["c1"] + " |")
    print("  +---+---+---+")
    print("2 | " + boardMarks["a2"] + " | " + boardMarks["b2"] + " | " + boardMarks["c2"] + " |")
    print("  +---+---+---+")
    print("3 | " + boardMarks["a3"] + " | " + boardMarks["b3"] + " | " + boardMarks["c3"] + " |")
    print("  +---+---+---+")

def MakingAMove(boardMarks, playerMark):
        
        print("Please enter your choice (e.g a1, b1 etc.")

        Board(boardMarks) # Run the Board() function to print the board
                                
        playerInput = input("--> ")

        bLoop = True

        while bLoop == True:

            try:

                boardMarks[playerInput] = playerMark

            except:

                print("Please enter a valid grid space...")

            else:

                bLoop = False

        return 

def WinConditions(boardMarks):
    
    pass

def Menu(menuItems): # Function for printing a menu
    
    print("\nPlease choose an option\n")

    menuItems.append("Exit") # Append "Exit" to the end of the list, so the last option is always the exit option

    bLoop = True
    
    while bLoop == True:

        for i in range(0, len(menuItems)): # Print the menu

            print(str(i+1) + ": " + menuItems[i])

        try:

            userChoice = int(input("--> ")) # Try to get an input from the user and convert it to an integer

            if userChoice < 1 or userChoice > len(menuItems): # If the user enters a number that's not an option, raise an IndexError exception

                raise IndexError

        except ValueError: # Error checking for the user input

            print("\nPlease enter a valid whole number\n")

        except IndexError:

            print("\nPlease enter a valid option\n")

        except:

            print("\nAn unknown error occurred, please enter the option you chose again\n")

        else: # If no error is triggered, exit the loop and continue the program

            bLoop = False

    if userChoice == len(menuItems): # If the user chooses the last option (i.e exit), return "exit" instead of the number

        return "exit"

    else:

        return userChoice # Return the number the user chose

def Main(): # Main body of the program inside a function

    boardMarks = {"a1":" ","a2":" ","a3":" ","b1":" ","b2":" ","b3":" ","c1":" ","c2":" ","c3":" "} # Create a dictionary for marks on the board, with each key corresponding
    # to a position on the board, initially set to blank spaces

    print("\nWelcome to my noughts and crosses game!")

    bContinue = True

    while bContinue:

        menuItems = ["Start"]

        userChoice = Menu(menuItems)

        if userChoice == "exit": # If userChoice is "exit", exit the program

            bContinue = False 

        elif userChoice == 1:

            print("\n") # Print a blank line

            MakingAMove(boardMarks)


Main() # Run the main program
