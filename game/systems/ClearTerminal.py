import os

def clear():
    lines = 25
    print("\n" * lines)
    print("\n" * lines)
    print("\n" * lines)
    print("\n" * lines)
    print("\n" * lines)
    print("\n" * lines)
    print("\n" * lines)
    try:
        #os.system('cls' if os.name == 'nt' else 'clear') #UNCOMMENT THIS LINE FOR USE IN TERMINAL, it will look nicer
        return
    except:
        return    
