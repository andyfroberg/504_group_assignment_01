"""
In addition to the team solution specified above, the team should write an
input generating program whose output can be used as input to test your
solutions. Place this in a project of its own. This program does not require
unit tests or Docstring comments.
"""
from random import random, randint


class MinesweeperInputGenerator:
    """
    Creates input to be used by the MinesweeperSolver solver class.
    """
    def __init__(self, output_path):
        """
        Creates a MinesweeperInputGenerator object.
        :param output_path: string - the path of the output file
        """
        self.__output_path = output_path
        self.__full_text = ""
        self.__count = 0

    # Generates a random minefield to be input into the MinesweeperSolver.
    # Optionally, the user can input a width and height if
    def generate_random_field(self):
        """
        Generates a random minefield of between 1-100 rows, and 1-100
        columns. The probability of a mine spawning in any given cell is
        roughly 50%.
        :return: None
        """
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

    def generate_field_uniform(self, rows, cols, all_mines=False):
        """
        Generates a field of m rows by n columns with either all mines
        or all empty cells (depending on whether the user sets the
        all_mines boolean to True or False.
        :param rows: number - the number of rows in the minefield
        :param cols: number - the number of columns in the minefield
        :param all_mines: boolean - sets all mines or no mines
        :return: None
        """
        filler = ""
        if all_mines:
            filler = "*"
        else:
            filler = "."

        new_field = ""
        for i in range(rows):
            new_row = ""
            for j in range(cols):
                new_row += filler
            new_field += f"{new_row}\n"

        self.__full_text += f"{rows} {cols}\n"
        self.__full_text += new_field

    def generate_field_with_string(self, minefield):
        """
        Genereates a minefield given an input string.
        :param minefield: string - the inpt string to generate a minefield
        :return: None
        """
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

    def add_terminating_str(self):
        """
        Adds the terminating string ("0 0\n") to ensure the MinesweeperSolver
        class has valid input and can stop properly.
        :return: None
        """
        self.__full_text += f"0 0\n"


    def write_output(self):
        """
        Writes the solved minesweeper puzzle to the output file given an
        output file path as an argument in the constructor of the
        MinesweeperSolver class.
        :return: None
        """
        with open(self.__output_path, "w", encoding='utf-8') as m:
            m.write(self.__full_text)

    ######################################################
    ########### Unit Test Helper Methods #################
    ######################################################
    # The following helper methods are for testing the program and include
    # docstrings to satisfy the assignment requirements (even though the
    # following methods are not part of the public interface).
    def get_text(self):
        """
        Returns the full text of the object.
        :return: string - the full text of this object.
        """
        return self.__full_text


if __name__ == "__main__":
    mig = MinesweeperInputGenerator("test_output_100x100_all_mines.txt")
    # mig.generate_field_with_string("1 1\n.\n")
    mig.generate_field_uniform(100,100,True)
    mig.add_terminating_str()
    mig.write_output()
