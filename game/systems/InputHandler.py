import sys
from systems.ClearTerminal import clear
class inputhandler:
    def entercon():
        if input("Press Enter to Continue") == "quit":
            clear()
            sys.exit(0)
        return
    def input_get_check():
        got_input = False
        raw_input = 0
        possible_inputs = ["show inventory","quit","room","stats","stat"]
        while got_input == False:
            
            raw_input = input("YOU ARE IN THE MAIN ROOM\nEnter \"show inventory\" to show your inventory\nEnter \"stats\" to show your player stats\nEnter \"room\" to go to the next room\nEnter \"quit\" to quit game\n> ").lower()
            if raw_input in possible_inputs:
                if raw_input == "quit":
                    clear()
                    sys.exit(0)
                got_input = True
                return raw_input
            else:
                clear()
                print("Please enter a valid input\n")
                inputhandler.entercon()
                clear()
                continue

    
    def get_name():
        got_name = False
        while got_name == False:
            player_name = input("Enter The Name you want to use for this game: ")
            if player_name == "quit":
                clear()
                sys.exit(0)
            if len(player_name) < 5:
                clear()
                print("Player name must be at least 5 characters long\n")
                inputhandler.entercon()
                clear()
                continue
            else:
                got_name = True
                break
        return player_name
    
    def check_input_room(room_number):
        got_input = False
        raw_input = 0
        possible_inputs = ["w","a","d","leave","quit"]
        while got_input == False:
            
            raw_input = input(f"YOU ARE IN ROOM {room_number.upper()}\nEnter \"w\" to go forward\nEnter \"a\" to go left\nEnter \"d\" to go right\nEnter \"leave\" to leave room\nEnter \"quit\" to quit game\n> ").lower()
            if raw_input in possible_inputs:
                if raw_input == "quit":
                    clear()
                    sys.exit(0)
                got_input = True
                return raw_input
            else:
                clear()
                print("Please enter a valid input\n")
                inputhandler.entercon()
                clear()
                continue
                
    def yesno(question,action):
        got_input = False
        raw_input = 0
        possible_inputs = ["yes","no"]
        while got_input == False:
            print(question)
            raw_input = input(f"\nEnter \"yes\" to {action}\nEnter \"no\" to not {action}\n> ").lower()
            if raw_input == "quit":
                clear()
                sys.exit(0)
            if raw_input in possible_inputs:
                got_input = True
                return raw_input
            else:
                clear()
                print("Please enter a valid input\n")
                inputhandler.entercon()
                clear()
                continue
    def dodge_direction(monsname):
        got_input = False
        raw_input = 0
        possible_inputs = ["left","right","back","forward"]
        while got_input == False:
            print(f"{monsname} is going to attack!!!\n")
            raw_input = input("Enter \"left\" to dodge to the left\nEnter \"right\" to dodge to the right\nEnter \"forward\" to dodge forwards\nEnter \"back\" to dodge backwards\n> ").lower()
            if raw_input == "quit":
                clear()
                sys.exit(0)
            if raw_input in possible_inputs:
                got_input = True
                return raw_input
            else:
                clear()
                print("Please enter a valid input\n")
                inputhandler.entercon()
                clear()
                continue
    def hangmanguess(hashedword,guesses):
        got_input = False
        raw_input = 0
        while got_input == False:
            print(hashedword)
            raw_input = input(f"Input a character to guess a letter, you have {guesses} guesses> ").lower()
            if raw_input == "quit":
                clear()
                sys.exit(0)
            if len(raw_input) == 1:
                got_input = True
                return raw_input

            else:
                clear()
                print("Please enter one character\n")
                inputhandler.entercon()
                clear()
                continue
    