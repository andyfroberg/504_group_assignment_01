"""
In addition to the team solution specified above, the team should write an
input generating program whose output can be used as input to test your
solutions. Place this in a project of its own. This program does not require
unit tests or Docstring comments.
"""
from random import randint


class MinesweeperInputGenerator:
    def __init__(self):
        self.__full_text = ""
        self.__minefields = ""
        self.__count = 0

    # Generates a random minefield to be input into the MinesweeperSolver.
    # Optionally, the user can input a width and height if
    def generate_random_field(self, width=randint(100), height=randint(100)):
        options = ("*", ".")



