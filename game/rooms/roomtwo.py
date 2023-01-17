from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
from systems.MonsterBattle import monsterbattle


class roomtwo:
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 1
        self.sword_damage = sword_damage
        self.item = "head armour"
        self.got_item = False
    def room(self):
        clear()
        global monster
        monster = monsterbattle("beefy man",20,5,self.health,self.sword_damage)
        room_run = True
        playerin = ""
        while room_run:
            clear()
            playerin = inputhandler.check_input_room("two")
            clear()
            if playerin == "w":
                self.forwardpart()
            elif playerin == "d":
                self.rightpart()
            elif playerin == "a":
                self.leftpart()
            else:
                return
            
                
            
            



    def forwardpart(self):
        print("You are in the front part of the room")
        if monster.monster_dead == False:
            monster.askfight()
            self.health = monster.return_health()
            clear()

        
        if self.item in self.inventory:
            print("\nThere is nothing Here\n")
            inputhandler.entercon()
        elif monster.monster_dead == True:
            clear()
            q = f"There is some {self.item} on the ground, do you pick it up?"
            player_answer = inputhandler.yesno(q,"pickup")
            if player_answer == "yes":
                clear()
                health_percent_to_add = int(self.total_health * .1)
                self.total_health += health_percent_to_add
                self.inventory.append(self.item)
                print(f"You picked up {self.item} increasing your maximum health by {health_percent_to_add}\n")
                self.room_number = 2
                
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

    def rightpart(self):
        print("You are in the right part of the room")
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
    
    