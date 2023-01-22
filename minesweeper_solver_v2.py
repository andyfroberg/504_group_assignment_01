

############ TO DO ###################
#
# [X] Read in each minefield individually
# [ ] Based on where we check in the minefield, call check_nw, etc.
#     appropriately (e.g., if we are in position (0,0) in the current
#     minefield, then don't call check_nw).
#
#
#
#

# Citations used
# Python Documentation - 7.2 Reading and Writing Files
# https://docs.python.org/3/tutorial/inputoutput.html

class MinesweeperSolver2:
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
        self.__current_field = []
        self.__field_start = 0
        self.__field_end = 0

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

    def solve_all_minefields(self):
        while self.__text[self.__field_end][0:] != "0 0\n":
            self.get_next_minefield()
            print(f"curr line is {self.__field_start}")
            self.get_hints()

    def get_hints(self):
        # The first field marking should not have a new line before it.
        # All other field markings should have a new line before them.
        self.__output_text += f'Field #{self.__field_count}:\n'
        self.__field_count += 1
        # # Include a new line between each minefield output.
        # if i != 0 and self.__text[i][0] != "." \
        #         and self.__text[i][0] != "*":
        #     self.__output_text += f'\nField #{self.__field_count}:\n'
        #     self.__field_count += 1

        if self.__field_end - self.__field_start == 0:  # Single row
            # if len(self.__current_field[self.__field_start]) <= 1:
            if self.__current_field[self.__field_start][0] == "*":
                return
            else:
                self.__current_field[self.__field_start][0] = "0"
                return

        for i in range(len(self.__current_field)):
            for j in range(len(self.__current_field[i])):
                if self.__current_field[i][j] == "*":
                    continue
                elif self.__current_field[i][j] == ".":
                    self.__current_field[i][j] = "0"
                    self.check_neighbors(i, j)
                else:
                    # self.check_neighbors(i, j)
                    # self.__output_text += "".join(self.__text[i])
                    pass

        print(f"self.__current_field: {self.__current_field}\n")

    def get_next_minefield(self):

        # Clear current minefield and set new start marker
        self.__current_field = []
        self.__field_start = self.__field_end

        # Get the size of the next minefield
        field_str = self.__text[self.__field_start].split("\n")
        field_size = field_str[0].split(" ")
        field_size[0], field_size[1] = int(field_size[0]), int(field_size[1])
        self.__field_start += 1  # Go to the next line after reading the size
        self.__field_end = self.__field_start + field_size[0]  # USED TO HAVE - 1 at the end
        print(f"current field size: {field_size}")

        # read the input
        for i in range(self.__field_start, self.__field_end):
            # Remove "\n"
            current_row_no_newline = self.__text[i].split("\n")[0]
            current_list_no_newline = list(current_row_no_newline)
            self.__current_field.append(current_list_no_newline)

    def check_neighbors(self, i, j):
        # Special case where there is a single row/col
        if len(self.__current_field) == 1 and len(
                self.__current_field[i]) == 1:
            if self.__current_field[i][j] == "*":
                return
            else:  # "."
                self.__current_field[i][j] = "0"
                return

        # Special case where there is a single row (of 1 > length <= 100)
        if len(self.__current_field) == 1 and len(self.__current_field[i]) > 1:
            if i == 0:
                if j == 0:
                    self.check_east(i, j)
                elif j == len(self.__current_field[i]) - 1:
                    self.check_west(i, j)
                else:  # Middle columns
                    self.check_west(i, j)
                    self.check_east(i, j)
            return

        # Special case where there is a single column (of 1 > height <= 100)
        if len(self.__current_field) > 1 and len(
                self.__current_field[i]) == 1:
            if i == 0:
                self.check_south(i, j)
            elif i == len(self.__current_field) - 1:
                self.check_north(i, j)
            else:  # Middle columns
                self.check_north(i, j)
                self.check_south(i, j)
            return

        if i == 0:  # Top row
            if j == 0:  # Left column
                self.check_east(i, j)
                self.check_south(i, j)
                self.check_southeast(i, j)
            elif j == len(self.__current_field[i]) - 1:  # Right column
                self.check_west(i, j)
                self.check_southwest(i, j)
                self.check_south(i, j)
            else:  # Top row middle columns
                self.check_east(i, j)
                self.check_west(i, j)
                self.check_southwest(i, j)
                self.check_south(i, j)
                self.check_southeast(i, j)
        elif i == len(self.__current_field) - 1:  # Bottom row
            if j == 0:  # Left column
                self.check_north(i, j)
                self.check_northeast(i, j)
                self.check_east(i, j)
            elif j == len(self.__current_field[i]) - 1:  # Right column
                self.check_northwest(i, j)
                self.check_north(i, j)
                self.check_west(i, j)
            else:  # Bottom row middle columns
                self.check_northwest(i, j)
                self.check_north(i, j)
                self.check_northeast(i, j)
                self.check_east(i, j)
                self.check_west(i, j)
        else:  # Middle rows
            if j == 0:  # Left column
                self.check_north(i, j)
                self.check_northeast(i, j)
                self.check_east(i, j)
                self.check_south(i, j)
                self.check_southeast(i, j)
            elif j == len(self.__current_field[i]) - 1:  # Right column
                self.check_northwest(i, j)
                self.check_north(i, j)
                self.check_west(i, j)
                self.check_southwest(i, j)
                self.check_south(i, j)
            else:  # Middle rows middle columns
                self.check_northwest(i, j)
                self.check_north(i, j)
                self.check_northeast(i, j)
                self.check_east(i, j)
                self.check_west(i, j)
                self.check_southwest(i, j)
                self.check_south(i, j)
                self.check_southeast(i, j)

    def check_north(self, i, j):
        if self.__current_field[i - 1][j] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_northwest(self, i, j):
        if self.__current_field[i - 1][j - 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_northeast(self, i, j):
        if self.__current_field[i - 1][j + 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_west(self, i, j):
        if self.__current_field[i][j - 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_east(self, i, j):
        if self.__current_field[i][j + 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_south(self, i, j):
        if self.__current_field[i + 1][j] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_southwest(self, i, j):
        if self.__current_field[i + 1][j - 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def check_southeast(self, i, j):
        if self.__current_field[i + 1][j + 1] == "*":
            self.__current_field[i][j] = str(int(self.__current_field[i][j]) + 1)

    def DEBUG_get_self__text(self):
        return self.__text

if __name__ == "__main__":
    m = MinesweeperSolver2("mines.txt", "minesweeper_output.txt")
    m.solve_all_minefields()
