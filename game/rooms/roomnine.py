from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear

class roomnine:
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 8
        self.sword_damage = sword_damage
        self.item = "iron"
        self.made_armour = False
    def room(self):
        clear()
        room_run = True
        playerin = ""
        
        while room_run:
            clear()
            playerin = inputhandler.check_input_room("nine") # change this to room number
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



    def rightpart(self):
        print("You are in the right part of the room")
        print("\nTheres nothing here\n")
        inputhandler.entercon()
        return
    
    def forwardpart(self):
        
        print("You are in the front part of the room")
        if self.made_armour == True:
            print("\nTheres nothing here\n")
            inputhandler.entercon()
            return
        
        q = f"\nYou see {self.item} on the floor"
        ans = inputhandler.yesno(q,"pickup")
        
        if ans == "yes":
            clear()
            self.health += (self.health * .5)
            print(f"you picked up the {self.item} and it magically bonded with your armour making you armour much better and increasing your health by 50 percent\nYou health is now {self.health}\n")
            self.room_number = 9
            self.made_armour = True
            inputhandler.entercon()
        else:
            clear()
            print(f"you did not pick up the {self.item}\n")
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