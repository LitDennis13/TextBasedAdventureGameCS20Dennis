from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
import random as r
import time
import sys
class monsterbattle:
    def __init__(self,monster_name,monster_health,monster_damage,player_health,player_damage):
        self.name = monster_name
        self.health = monster_health
        self.damage = monster_damage
        self.monster_dead = False
        self.player_health = player_health
        self.player_damage = player_damage

    def nofight(self):
        clear()
        print(f"You will not fight {self.name}")
        print()
        inputhandler.entercon()
        return

    def askfight(self):
        print()
        q = f"Theres is a monster named {self.name}, it has {self.health} health and does {self.damage} damage, do you attack?"
        player_answer = inputhandler.yesno(q,"attack")
        if player_answer == "yes":
            self.enterbattle()
        else:
            self.nofight()




    def enterbattle(self):
        clear()
        print(f"You are battling {self.name}\n")
        inputhandler.entercon()
        clear()
        monsattack = 0
        options = ["right","left","back"]
        player_choice = ""
        while self.monster_dead == False:
            if self.player_health <= 0:
                clear()
                print("You have died\n")
                inputhandler.entercon()
                clear()
                sys.exit(0)
            monsattack = r.randint(0,2)
            clear()
            print(f"You attack and do {self.player_damage} damage to {self.name}\n")
            self.health -= self.player_damage
            if self.health <= 0:
                self.health = 0
            print(f"{self.name} is at {self.health} health\n")
            print(f"You are at {self.player_health} health\n")
            inputhandler.entercon()
            clear()
            if self.health <= 0:
                clear()
                print(f"{self.name} has died\n")
                self.monster_dead = True
                inputhandler.entercon()
                return
            player_choice = inputhandler.dodge_direction(self.name)
            if player_choice == "forward":
                clear()
                print("wow\n")
                time.sleep(3)
                print(f"You dodge forward into {self.name} effectively killing yourself\n")
                time.sleep(2)
                print("GAME OVER\n")
                inputhandler.entercon()
                clear()
                sys.exit(0)

            elif player_choice == options[monsattack]:
                clear()
                print(f"{self.name} attacks to the {player_choice} and hits you for {self.damage} damage\n")
                self.player_health -= self.damage
                if self.player_health <= 0:
                    print("You are now at 0 health\n")
                    inputhandler.entercon()
                else:
                    print(f"You are now at {self.player_health} health\n")
                    inputhandler.entercon()
            else:
                clear()
                print(f"{self.name} missed the attack\n")
                inputhandler.entercon()
                print()

    def return_health(self):
        return self.player_health
            
            
            
            
            
            
