from systems.InputHandler import inputhandler
from systems.ClearTerminal import clear
import random
import sys
class bossroom:
    def __init__(self, player_name,player_health,player_total_health,player_inventory,sword_damage):
        self.name = player_name
        self.health = player_health
        self.total_health = player_total_health
        self.inventory = player_inventory
        self.room_number = 12
        self.sword_damage = sword_damage
    def room(self):
        clear()
        words = ["abroad","accept","access","battle","behind","bottle","border","branch","center","county","danger","losing","marked","marker","market","margin","nights","second","signed","senior","simply","summer","taking","yellow","scammer","hello","red","epic","game","gamer","school","nice","student","bus","assignment","hangman","gaming","chair","computer","science","easy","guess","words","keyboard","mouse","phone","apple","microsoft","google","bossed","quick","brown","fox","lazy","knight"]
        word = random.choice(words)
        room_run = True
        dmg = random.randint(200,1323)
        boss_health = len(word) * dmg
        
        while room_run:
            clear()
            print("you enter the boss room\n")
            inputhandler.entercon()
            clear()
            print("as you walking in all of your gear randomly disappears\n")
            inputhandler.entercon()
            clear()
            print("as you try to leave\n")
            inputhandler.entercon()
            clear()
            print("THE HANGING MAN ENTERS THE ROOM\n")
            inputhandler.entercon()
            clear()
            print("you jump back out of shock\n")
            inputhandler.entercon()
            clear()
            print("you see a cannon and run to it\n")
            inputhandler.entercon()
            clear()
            print(f"the cannon has {len(word)*2} shots in it, each shot does {dmg} damage per each shot\n")
            inputhandler.entercon()
            clear()
            print(f"the hangin man has {boss_health} health meaning that you need to hit at least {len(word)} shots to kill it\n")
            inputhandler.entercon()
            clear()
            print("THE HANGING MAN IS WALKING TOWARDS YOU\n")
            inputhandler.entercon()
            clear()
            print(f"How to defeat: to defeat the hanging man you must guess the letters in a {len(word)} letter word that will be presented to you, the hangin man will continue to get closer to you, you must guess the letters to hit the hanging man to do damage to it, if you miss it will keep coming toward you and if you do not kill the hanging in {len(word)*2} shots you die.\n")
            inputhandler.entercon()
            clear()
            print("Are you ready?,if not type quit to quit game\n")
            inputhandler.entercon()
            clear()
            self.hangman(word,boss_health,dmg)
            inputhandler.entercon()
            

    def hangman(self,word,health,dmg):
        wordchars = []
        for char in range(0,len(word)):
            wordchars.append(word[char])
        wordhash = []
        for char in wordchars:
            wordhash.append("#")
        hashedword = ""
        run_hangman = True
        guesses= len(word) * 2
        guessed_letters = []
        non_guessed = 0
        while run_hangman:
            non_guessed = 0
            for i in wordhash:
                if i == "#":
                    non_guessed += 1
            
            if (guesses <= 0 or guesses < non_guessed) and health != 0:
                if guesses < non_guessed and guesses != 0:
                    clear()
                    print(f"you have {guesses} guesses but there are still {non_guessed} letters to be guessed\n")
                    inputhandler.entercon()
                    clear()
                    print("you will not have enough guesses to finish the word\n")
                    inputhandler.entercon()
                else:
                    clear()
                    print("you have ran out of guesses\n")
                    inputhandler.entercon()
                clear()
                print(f"the word was {word}\n")
                inputhandler.entercon()
                clear()
                print("the hangin man has not died\n")
                inputhandler.entercon()
                clear()
                print("the hangin man gets to you and rips you to pieces\n")
                inputhandler.entercon()
                clear()
                print("you have died\n")
                inputhandler.entercon()
                clear()
                print("GAME OVER\n")
                inputhandler.entercon()
                clear()
                sys.exit(0)
            elif health <= 0:
                clear()
                print("YOU GOT THE WORD\n")
                inputhandler.entercon()
                clear()
                print(f"the word was {word}\n")
                inputhandler.entercon()
                clear()
                print("YOU HAVE DEFEATED THE HANGING MAN\n")
                inputhandler.entercon()
                clear()
                for i in range(0,100):
                    print("WWOWOWOoowowWOOOOO")
                print()
                inputhandler.entercon()
                clear()
                print("GAME OVER\n")
                inputhandler.entercon()
                clear()
                print("congratulations,YOU WIN\n")
                inputhandler.entercon()
                clear()
                sys.exit(0)
            first = True
            for char in wordhash:
                if first == True:
                    hashedword += char
                    first = False
                else:
                    hashedword += "-"+char
                
            
            guess = inputhandler.hangmanguess(hashedword,guesses)
            hashedword = ""
            
            if guess in wordchars:
                clear()
                guesses -= 1
                index=0
                for i in range(len(wordchars)):
                    if wordchars[i] == guess:
                        index = i
                        break               
                wordhash[index] = guess
                wordchars[index] = "#"                
                health -= dmg
                guessed_letters.append(guess)
                print("YOU HIT THE HANGING MAN\n")
                inputhandler.entercon()
                clear()
                print(f"the hanging man is now at {health} health\n")
                inputhandler.entercon()
                clear()
            elif guess in guessed_letters:
                clear()
                print(f"you already guessed {guess}\n")
                inputhandler.entercon()
                clear()
            else:
                clear()
                guesses -= 1
                guessed_letters.append(guess)
                print(f"you missed the the hanging man, you have {guesses} guesses left\n")
                inputhandler.entercon()
                clear()
            
                
            
            

        

    
            
