"""
In addition to the team solution specified above, the team should write an
input generating program whose output can be used as input to test your
solutions. Place this in a project of its own. This program does not require
unit tests or Docstring comments.
"""
from random import random, randint


class MinesweeperInputGenerator:
    def __init__(self, output_path):
        self.__output_path = output_path
        self.__full_text = ""
        self.__count = 0

    # Generates a random minefield to be input into the MinesweeperSolver.
    # Optionally, the user can input a width and height if
    def generate_random_field(self):
        rows = randint(1, 100)
        cols = randint(1, 100)

        new_field = ""
        for i in range(rows):
            new_row = ""
            for j in range(cols):
                if randint(0, 1) == 1:
                    new_row += "*"
                else:
                    new_row += "."
            new_field += f"{new_row}\n"

        self.__full_text += f"{rows} {cols}\n"
        self.__full_text += new_field

    def generate_field(self, minefield):
        if type(minefield) is not str:
            raise AttributeError("This method accepts only a string "
                                 "of '*' or '.' characters to generate "
                                 "a minefield.")
        new_field = ""
        for ch in minefield:
            new_field += ch

        self.__full_text += new_field

        # if rows > 100 or cols > 100:
        #     raise AttributeError(f"The size of the minefield must be"
        #                          f"0 < rows, cols <= 100.")

    def generate_n_random_minefields(self, n):
        for i in range(n):
            self.generate_random_field()

        self.add_terminating_str()

    def add_terminating_str(self):
        self.__full_text += f"0 0\n"


    def write_output(self):
        """
        Writes the solved minesweeper puzzle to the output file given an
        output file path as an argument in the constructor.
        :return: None
        """
        with open(self.__output_path, "w", encoding='utf-8') as m:
            m.write(self.__output_text)

    def get_text(self):
        return self.__full_text


if __name__ == "__main__":
    mig = MinesweeperInputGenerator("mines.txt")
    mig.generate_n_random_minefields(10)
    # mig.generate_field("4 10\n***.....**\n***.....**\n***.....**\n***.....**\n")
    print(mig.get_text())
