# Citations used
# Python Documentation - 7.2 Reading and Writing Files
# https://docs.python.org/3/tutorial/inputoutput.html

class MinesweeperSolver:
    """
    This class takes a given minesweeper puzzle as text input (in a specific
    minesweeper format), solves the puzzle, then outputs the solved puzzle
    to an output file.
    """

    def __init__(self, input_path, output_path):
        """
        Constructs a MinesweeperSolver object.
        :param input_path: The path of the minesweeper file to be solved.
        :param output_path: The path of the file to write the solved puzzle to.
        """
        self.__input_path = input_path
        self.__output_path = output_path
        self.__text = self.read_input()
        self.__output_text = ""
        self.__field_count = 1

    def read_input(self):
        """
        Reads the input from a given minesweeper puzzle file.
        :return: The full text of the input file.
        """
        with open(self.__input_path, 'r', encoding='utf-8') as f:
            return f.readlines()

    def write_output(self):
        """
        Writes the solved minesweeper puzzle to the output file given an
        output file path as an argument in the constructor.
        :return: None
        """
        with open(self.__output_path, "w", encoding='utf-8') as m:
            m.write(self.__output_text)

    def solve(self):
        """
        'Solves' the minesweeper puzzle given as input to the constructor.
        Takes the full text of the input file (stored in self.__text), then
        iterates through each character to solve the puzzle.
        :return: None
        """
        for i in range(len(self.__text)):

            # Check if the end of the minefield data has been reached.
            # (The assignment states, "The first field line where n = m = 0
            # represents the end of input and should not be processed.")
            if self.__text[i][0:-1] == "0 0":
                break

            # The first field marking should not have a new line before it.
            # All other field markings should have a new line before them.
            if i == 0 and self.__text[0][0] != "." \
                    and self.__text[0][0] != "*":
                self.__output_text += f'Field #{self.__field_count}:\n'
                self.__field_count += 1

            # Include a new line between each minefield output.
            elif i != 0 and self.__text[i][0] != "." \
                    and self.__text[i][0] != "*":
                self.__output_text += f'\nField #{self.__field_count}:\n'
                self.__field_count += 1

            # Not a field marking (i.e., is part of the minefield)
            else:
                self.__text[i] = list(self.__text[i])
                for j in range(len(self.__text[i])):
                    if self.__text[i][j] == "*":
                        continue
                    elif self.__text[i][j] == ".":
                        self.__text[i][j] = "0"
                        self.check_neighbors(i, j)
                    else:  # \n
                        s = ""
                        self.__output_text += s.join(self.__text[i])

    def check_neighbors(self, i, j):
        """
        Checks each 'neighbor' around the current position in the text file, i
        and j represent the row position and column position. If a "*" is in
        an adjacent position, then the mine count of the current position is
        incremented. This method uses a try except block to test all neighbors
        (northwest, north, northeast, west, east, southwest, south, and
        southeast) to handle any index out of bounds exceptions.
        :param i: The current row 'position' in self.__text.
        :param j: The current column 'position' in self.__text.
        :return: None
        """
        for x in range(-1, 2):
            for y in range(-1, 2):
                try:
                    if self.__text[i + x][j + y] == "*":
                        self.__text[i][j] = str(int(self.__text[i][j]) + 1)
                except IndexError:
                    pass

    def add_final_newline(self):
        """
        The "official_output.txt" file has two newlines at the bottom of the
        file. In order to make the output identical, a final newline needs to
        be added to the end of the output file.
        :return: None
        """
        self.__output_text += "\n"


if __name__ == "__main__":
    m = MinesweeperSolver("mines.txt", "minesweeper_output.txt")
    m.solve()
    m.add_final_newline()
    m.write_output()
