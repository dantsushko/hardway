from sys import exit
from random import randint
from textwrap import dedent

class  Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()


class Death(Scene):
    quips = [
        "You died. You kinda suck at this..",
        "Your mom would be proud of you. If she were smarter.",
        "Shut up and go to Valhalla",
        "No luck for you today, little dermodemon",
        "You are worse than your dad's jokes"
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and destroyed
            your entire crew. You are the last surviving member and your last
            mission is to get the neutron distract bomb from the
            Weapons Armory, put it in the brige and blow the ship after
            getting in the escape pod.

            You are running down the central coridor to the weapons armory
            when a Gothon jumps out, red scaly skin, dark grimy teeth, and evil
            clown costume flowing around his hate-filled body. He is blocking
            the door to the armory and about to pull a weapon to blast you
            """
            ))
        action = input("> ")

        if action == "shoot":
            print(dedent("""
                 Quick on the draw you yank out your blaster and fire
                 it at the Gothon. His clown costume is flowing and
                 moving around his body, which throws off your aim.
                 Your laser hits his costume but misses him entirely.
                 This completely ruins his brand new costume his mother
                 bought him, which makes him fly into an insane rage
                 and blast you repeatedly in the face until you are
                 dead. Then he eats you.
                 """
                 ))
            return 'death'

        elif action == "dodge":
            print(dedent("""
                Like a world class boxer you dodge, weave,
                slip and slide right as the Gothon's blaster cranks a laser
                past your head. In the middle of your artful dodge your foot
                slips and you bang your head on the metal wall and pass out.
                You wake up shortly after only to die as the Gothon stomps
                on your head and eats you. """))
            return 'death'

        elif action == 'tell a joke':
            print(dedent("""
                Lucky for you they made you learn Gothon insults in the academy
                You tell the one Gothon joke you know: Lbbhe zbgure kjksad snf
                jura, asqwij popo ashia. The Gothon stops trying not to laugh,
                the busts up laughing and cant move. While he's laughing you
                run up and shoot him in the head then jump through the Weapon
                Armory door.
            """
            ))
            return 'laser_weapon_armory'
        else:
            print("DOESNT COMPUTE!")
            return 'central_corridor'



class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan
            the room for more Gothons that might be hiding. It's dead
            quiet, too quiet. You stand up and run to the far side of
            the room and find the neutron bomb in its container.
            There's a keypad lock on the box and you need the code to
            get the bomb out. If you get the code wrong 10 times then
            the lock closes forever and you cant get a bomb. the code is 3 digits
            You can try to guess it or use your computer to break it
            """))
        def break_code(code):
            key = ""
            while key != code:
                key = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
            print(key)
            return key
        code = f"{randint(0,9)}{randint(0,9)}{randint(0,9)}"
        choice = input("> ")
        if choice == "break the code":
            guess = break_code(code)
        else:
            guess = input("[keypad] > ")
        guesses = 0
        while guess != code and guesses < 9:
            print("BBZZZZZEEEEEEDDD")
            guesses += 1
            guess = input("[keypad] > ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal brakes, letting gas out
                You grab the bomb and run as fast as you can to the bridge, where
                you must place a bomb
            """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and the you hear a sound of
                container closing forever. You decide to sit here and finally
                the Gothons caught you and you died in harmful pain.
            """))
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
                You burst onto the bridge with the neuron destruct bomb and
                surprise five Gothons who are trying to take control of the ship
                They havent pulled their weapons off as they see active bomb
                under your arm.
            """))
        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you throw the bomb in a group of Gothons and make a
                leap for the door. Right as you drop it Gothon shots you Right
                in back killing you. You died knowing that they blowed up with
                you
            """))
            return 'death'

        elif action == "slowly place a bomb":
            print(dedent("""
                 You point your blaster at the bomb under your arm and
                 the Gothons put their hands up and start to sweat.
                 You inch backward to the door, open it, and then
                 carefully place the bomb on the floor, pointing your
                 blaster at it. You then jump back through the door,
                 punch the close button and blast the lock so the
                 Gothons can't get out. Now you run to the escape pod

            """))
            return 'escape_pod'
        else:
            print("Does not COMPUTE")
class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes. It seems
            like hardly any Gothons are on the ship, so your run is
            clear of interference. You get to the chamber with the
            escape pods, and now need to pick one to take. Some of
            them could be damaged but you don't have time to look.
            There's 5 pods, which one do you take?
         """))
        good_pod = randint(1, 2)
        guess = input("Pod #")

        if int(guess) != good_pod:
            print(dedent(f"""
             You jump into pod {guess} and hit the eject button.
             The pod escapes out into the void of space, then
             implodes as the hull ruptures, crushing your body into
             jam jelly.
             """))
            return 'death'
        else:
            print(dedent(f"""
                 You jump into pod {guess} and hit the eject button.
                 The pod easily slides out into space heading to the
                 planet below. As it flies to the planet, you look
                 back and see your ship implode then explode like a
                 bright star, taking out the Gothon ship at the same
                 time. You won!
                 """))

            return 'finished'
class Finished(Scene):

    def enter(self):
        print("You won, good job Captain")
        return 'finished'


class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()

    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
