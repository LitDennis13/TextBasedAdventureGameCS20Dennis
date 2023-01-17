from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear

class roomten:
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 9
        self.sword_damage = sword_damage
        self.sharpener_use = False
        self.room_number = 10
    def room(self):
        clear()
        room_run = True
        playerin = ""
        
        while room_run:
            clear()
            playerin = inputhandler.check_input_room("ten") # change this to room number
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
        if self.sharpener_use == True:
            print("\nTheres nothing here\n")
            inputhandler.entercon()
            return
        q = f"\nYou see a powerful sword sharpener"
        ans = inputhandler.yesno(q,"use")
        
        if ans == "yes":
            clear()
            self.sword_damage += (self.sword_damage * .32)
            print(f"you use the powerful sword sharpener and increase your sword damage by 32 percent\nyour sword damage is now {self.sword_damage}\n")
            self.sharpener_use = True
            inputhandler.entercon()
        else:
            clear()
            print(f"you not use the sword sharpener\n")
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