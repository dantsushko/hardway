from sys import exit
from textwrap import dedent


class Place(object):
    def enter(self):
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


class Gilead(Place):
    print(dedent("""
        Hello Dan, you are in Gilead right now.
        The only reason of you life is to get to the Dark Tower.
        To stop the world from shifting.
        Unfortunately you've lost your ammunition and you have only six bullets..
    """))




class DarkTower(Place):
    pass

class NewYork(Place):
    pass

class Discordia(Place):
    pass

class Death(Place):
    quips = [
        "You died. Sea monsters ate you",
        "Shut up and remember the face of your father",
        "No luck for you today",
        "Hail to Crimson King"
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class Finished(Place):

    def enter(self):
        print("You've killed the Crimson King, Roland, good job")
        return 'finished'

class Person(object):
    def __init__(self, hp, bullets):
        self.hp = hp
        self.bullets = bullets

class Gunslinger(Person):
    self.bullets = 6

class ManInBlack(Person):
    pass


class Door(object):
    pass

class DiscordiaDoor(Door):
    pass

class NewYorkDoor(Door):
    pass


class Map(object):
    scenes = {
        'gilead': Gilead(),
        'darktower': DarkTower(),
        'newyork': NewYork(),
        'Discordia': Discordia(),
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


a_map = Map('gilead')
a_game = Engine(a_map)
a_game.play()
