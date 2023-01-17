import sys
from player import Player
from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
from systems.RoomSystems import roomsystems

class main:
    def Main():
        clear()
        global player
        player = Player("")
        player.name = inputhandler.get_name()
        clear()
        print("Pro tip: make sure to check each room, some room may have more then one monster or item in it and most rooms will require you to collect certain items before moving on, IT IS YOUR RESPONSIBILITY TO CHECK EACH PART OF THE ROOM\n")
        inputhandler.entercon()
        clear()
        game_run = True
        item_number = 0
        while game_run:
            clear()
            roomsystems.make_rooms(player)
            player_input = inputhandler.input_get_check()
            if player_input == "show inventory":
                item_number = 0
                clear()
                print("Showing Inventory")
                
                for item in player.inventory:
                    item_number += 1
                    print(f"\nItem {item_number}:",item)
                print()
                inputhandler.entercon()   
                continue
            elif player_input == "stats" or player_input == "stat":
                clear()
                print(f"Your name is {player.name}")
                print(f"Your total health is {player.total_health}")
                print(f"Your current health is {player.health}")
                print(f"Your sword damage is {player.sword_damage}")
                print(f"Your current room level is {player.room_number+1}\n")
                inputhandler.entercon()
            else:
                roomsystems.go_to_room(player)
                continue
main.Main()
