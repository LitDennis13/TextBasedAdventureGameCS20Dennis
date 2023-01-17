from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear

class roomsix:
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 5
        self.sword_damage = sword_damage
        self.item = "magic apple"
    def room(self):
        clear()
        room_run = True
        playerin = ""
        self.room_number = 6
        while room_run:
            clear()
            playerin = inputhandler.check_input_room("six") # change this to room number
            clear()
            if playerin == "w":
                self.forwardpart()
            elif playerin == "d":
                self.rightpart()
            elif playerin == "a":
                self.leftpart()
            else:
                clear()
                return



    def forwardpart(self):
        print("You are in the front part of the room")
        print("\nTheres nothing here\n")
        inputhandler.entercon()
        return
    
    def rightpart(self):
        
        print("You are in the right part of the room")
        if self.item in self.inventory:
            print("\nTheres nothing here\n")
            inputhandler.entercon()
            return
        q = f"\nYou see a {self.item} on the floor"
        ans = inputhandler.yesno(q,"eat")
        
        if ans == "yes":
            clear()
            self.inventory.append(self.item)
            print(f"you eat the {self.item} and you regenerated your health to a max health of {self.total_health}\n")
            self.health = self.total_health
            inputhandler.entercon()
        else:
            clear()
            print(f"you did not eat the {self.item}\n")
            inputhandler.entercon()
        return

    def leftpart(self):
        print("You are in the left part of the room")
        print("\nTheres nothing here\n")
        inputhandler.entercon()
        return
    def return_health(self):
        return self.health
    def return_inventory(self):
        return self.inventory
    def return_room_number(self):
        return self.room_number
    def return_sword_damage(self):
        return self.sword_damage
    def return_total_health(self):
        return self.total_health