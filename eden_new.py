"""The Garden of Eden."""

planets = []

class World:

    """A planet with a name, capacity, and inhabitants"""

    def __init__(self, name, human_capacity):
        if not human_capacity.isdigit():
            raise ValueError(
                "Please enter a number only. '{}' is invalid."
                .format(human_capacity))\

        planets.append(name)
        self.names = []
        self.inhabitants = []
        self._human_capacity = int(human_capacity)
        self._name = name

    def name(self):
        return self._name

    def human_capacity(self):
        return self._human_capacity

    def population(self):
        return len(self.inhabitants)

    def whos_here(self):
        for x in self.inhabitants:
            if x.name() not in self.names:
                self.names.append(x.name())

    def add_human(self, *args):
        if not (len(self.inhabitants) < self._human_capacity):
            raise Exception("Population at capacity!!!")

        f = Human(
            named.get(),
            self._name)
        print("{} has been born.".format(f.name()))
        self.inhabitants.append(f)


class Human:

    """A human with a name, sex, and home planet."""

    def __init__(self, name, planet):

        if not name.isalpha():
            raise ValueError("Name cannot include numbers'{}'".format(name))

        self._planet = planet
        self._name = name

    def name(self):
        return self._name

    def planet(self):
        return self._planet


b =World(input("Give your planet a name: "), 
    input("How many people can live on your planet? "))

