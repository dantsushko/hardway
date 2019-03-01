print("""You enter a dark room with two doors.
Which door will you choose?""")

door = input('>' )

if door == '1':
    print("There is a giant bear eating a cheesecake\n What will you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")
    bear = input('> ')
    if bear == '1':
        print("The bear eats your face off, good job bro))")
    elif bear == '2':
        print("The bear eats you legs off, gg")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away")

elif door == '2':
    print("You stare into the endless abyss at Ktulhu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")
    insanity = input("> ")
    if insanity == '1' or insanity == '2':
        print("Your body survives powered by a mind of jello")
        print("Good job")
    else:
        print("The insanity rots your eyes into a pool of muck")
elif door == '3':
    print("You see the Dark Tower, Roland, at last")
    print ("HAIL HILEAD!!")
    print("What will you choose, gunslinger?")
    print("1. Leave all of your ka-tet, and go alone to the Tower")
    print("2. Kill Jake again, always hated little son of a bitch")
    print("3. Finish my road with all of them")
    tower_choice = input("> ")
    if tower_choice == '1':
        print("You spent many days trying to reach the Tower\n then you heard that all of your ka-tet are in danger")
        danger_choice = input("Will you save them > ")
        print("1. Yes")
        print("2. No. The Tower is everything")
        if danger_choice == '1':
            print("You have returned but unfortunately you didnt manage to save all")
            print("You have lost everything... Looser")
        if danger_choice == '2':
            print("You have left your ka-tet again, now they are dead")
            print("One night you just died, even your rude heart didn't bear such a sin")
    elif tower_choice == '2':
        print("You decided to kill Jack, but.... You are to old, and\n Susannah shot you. GG")
    else:
        print("You have ended your journey respectfully, You have reached the tower and........")
