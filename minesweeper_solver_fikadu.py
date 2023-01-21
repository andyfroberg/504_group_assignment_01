class MinesweeperSolver:
    """Minesweeper class takes text file as an input and parse into fields and assign consiqutive names to each field.
    Then Calculates the total num=ber of mines to each row and column then write to the mine field already created"""

    def __init__(self, input_text_path, output_text_path):
        """ This reads the input files and returns lines in the tex files and mke ready for further processing.
        Takes the raw takes and return lines
        """
        self.__input_path = input_text_path
        self.__output_path = output_text_path
        self.__text = self.read_input()
        self.__output_text = ""
        self.__field_count = 1

    def read_input(self):
        """ This reads the input files and returns lines in the tex files and mke ready for further processing.
        Takes the raw takes and return lines
        """
        with open(self.__input_path, 'r') as infile:
            return infile.readlines()

    def write_output(self):
        """ This method takes the processed text and writes to an output file in txt format """
        with open(self.__output_path, "w") as outfile:
            outfile.write(self.__output_text)

    def create_field(self):
        """ The create_field method takes the lines which is converted to line by read_input method and creates fields
        and parses the lines and content into their respective field as specified in the specification
        """
        # Read each field's row and column to parse to Minefield. When reached a field where column = 0 and row = 0
        # The reading reached the end and break.
        for i in range(len(self.__text)):
            if self.__text[i][0:-1] == "0 0":
                break
            if i == 0 and self.__text[0][0] != "." \
                    and self.__text[0][0] != "*":
                self.__output_text += f'Field #{self.__field_count}:\n'
                self.__field_count += 1

            # Include a new line between each minefield output.
            elif i != 0 and self.__text[i][0] != "." \
                    and self.__text[i][0] != "*":
                self.__output_text += f'\nField #{self.__field_count}:\n'
                self.__field_count += 1

            else:
                self.__text[i] = list(self.__text[i])
                for j in range(len(self.__text[i])):
                    if self.__text[i][j] == "*":
                        continue
                    elif self.__text[i][j] == ".":
                        self.__text[i][j] = str(self.sum_neighbors(i, j))
                    else:  # \n
                        s = ""
                        self.__output_text += s.join(self.__text[i])

    def sum_neighbors(self, i, j):
        """ check_neighbors field calculate the total number of adjacent mines for each cell in the field to the each
        """
        count = 0
        # Check if cell left to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i - 1][j] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell right to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i + 1][j] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell South to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i][j + 1] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell North to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i][j - 1] == "*":
                count += 1
        except IndexError:
            pass

        # Check if cell South West to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i - 1][j + 1] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell North West to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i - 1][j - 1] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell South East to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i + 1][j + 1] == "*":
                count += 1
        except IndexError:
            pass
        # Check if cell North East to the current cell has a mine and increase count by one if mine is found
        try:
            if self.__text[i + 1][j - 1] == "*":
                count += 1
        except IndexError:
            pass

        print(count)
        # Finally return the total count of mine adjacent to the current cell
        return count

    def add_final_line(self):
        """
        Add final line to the out_put text file
        """
        self.__output_text += "\n"


if __name__ == "__main__":
    minesweeper = MinesweeperSolver("mines.txt", "minesweeper_ouput.txt")
    minesweeper.create_field()
    minesweeper.add_final_line()
    minesweeper.write_output()
