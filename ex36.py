from sys import exit

def start():
    hp = 100
    print("You stand in the end of a long coridor.")
    print("There are two ways you can choose.")
    print("Left or right, what will you choose?")
    choice = input("> ")
    have_revolver = False
    if choice == "Left":
        dogan()
    elif choice == "Right":
        print("You see two doors, which will you choose 1 or 2?")
        choice = input("> ")
        if choice == "1":
            dark_tower()
        elif choice == "2":
            new_york(have_revolver)
        else:
            print("1 or 2!!!!!")
            start()
    else:
        print("There are no ways except left and right!")
        start()

def die(reason):
    print(reason, "Bye bye")
    exit(0)

def dogan():
    print("You see an old ruined dogan")
    print("Will you enter?")
    choice = input("y/n ")

    if choice == "y":
        dogan_in()
    elif choice == "n":
        die("Sorry, you have been killed by low-people.....")
    else:
        print("Wroooong!")
        dogan()
def dogan_in():
    have_bag = False
    print("You came into the dogan, you see a lot of useful staff.")
    print("There are snitch, an old revolver and strange bag.")
    print("What will you take? 1 2 or 3?")
    choice = input("> ")

    if choice == "1":
        die("Snitch has blowed up in your hands.. Too stupid even for you")
    elif choice == "2":
        print("Good choice, bro")
        have_revolver = True
    elif choice == "3":
        print("Strange choice...")
        have_revolver = False
    print("You see two doors again: black and white")
    print("Choose one")
    choice = input("> ")
    if choice == "white":
        new_york(have_revolver)
    elif choice == "black":
        die("Strange choice for the White Knight.. ")
    else:
        print("BLACK AND WHITE!")
        dogan_in()




def dark_tower():
    pass

def new_york(have_revolver):
    print("You stand in the middle of 5th Avenue")
    print("There are lots of zombies!")
    print("What will you do?")
    if have_revolver == True:
        print("You can shoot them, or run from them")
        choice = input("> ")
        if choice == "shoot":
            print("You have killed all zombies and went home")
            print("Good job, you won")
            exit(0)
        elif choice == "run":
            print("You have a gun stupid coward")
            die("You'd better use it..")

    elif have_revolver == False:
        print("You can only run from them")
        print("Oops, they seemed slow AAAAAA AAA AAAARHGH")
        die("No luck for you today")

    pass

start()
