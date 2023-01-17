from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
from systems.MonsterBattle import monsterbattle


class roomseven:
    
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 1
        self.sword_damage = sword_damage
        self.item = "diamond sword"
        self.sword_sharpen_use = False
        self.monster_one_dead = False
        self.monster_two_dead = False
        
        self.got_item = False
    def room(self):
        clear()
        room_run = True
        playerin = ""        
        while room_run:
            clear()
            playerin = inputhandler.check_input_room("seven")
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
        if self.monster_one_dead == False:
            monsterone = monsterbattle("Diamond scream",80,20,self.health,self.sword_damage)
            monsterone.askfight()
            self.health = monsterone.return_health()
            self.monster_one_dead = True
            clear()

        
        if self.item in self.inventory:
            print("\nThere is nothing Here\n")
            inputhandler.entercon()
        elif self.monster_one_dead == True:
            clear()
            q = f"There is a {self.item} on the ground, do you pick it up?"
            player_answer = inputhandler.yesno(q,"pickup")
            if player_answer == "yes":
                clear()
                self.inventory.append(self.item)
                new_dmg = self.sword_damage + 10
                self.sword_damage = new_dmg
                print(f"you picked up the {self.item} and you increased your sword damage to {self.sword_damage} damage\n")
                
                self.room_number = 7
                inputhandler.entercon()
            else:
                clear()
                print(f"you did not pick up the {self.item}\n")
                inputhandler.entercon()       
        return
    




    def leftpart(self):
        print("You are in the left part of the room")
        if self.monster_two_dead == False:
            monstertwo = monsterbattle("Crazy Robot",150,40,self.health,self.sword_damage)
            monstertwo.askfight()
            self.health = monstertwo.return_health()
            self.monster_two_dead = True
            clear()

        
        if self.sword_sharpen_use == True:
            print("\nThere is nothing Here\n")
            inputhandler.entercon()
        elif self.monster_two_dead == True:
            clear()
            q = f"There is a sword sharpener at the back of the room, would you like to sharp your sword?"
            player_answer = inputhandler.yesno(q,"sharpen")
            if player_answer == "yes":
                clear()
                self.sword_damage += 10
                print(f"You sharpened your sword increasing its damage by 10\nThe sharpener has randomly disappeared\n")
                self.sword_sharpen_use = True
                print(self.sword_sharpen_use)
                inputhandler.entercon()
            else:
                clear()
                print(f"you did not use the {self.item}\n")
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
    
    