"""
Build unit tests to test your team solution. Incorporate the results from your
input generator into your unit tests as you deem necessary. Your tests should
cover all edge cases (minimums, maximums) as well as some general cases. Recall
that the input to the program will be well-formed so you are not required to
test for invalid data.

- There should be individual test methods for each case you test.
- Include tests to ensure you can properly read in the rows, columns, and data
  for a single minefield.
- Include tests that validate your hint producing code/function/method.
- Include tests that validate output for a given minefield is formatted properly.
- Be sure and name your test methods so they describe the test.
"""




# Test current cell is top left corner

# Test current cell is top right corner

# Test current cell is bottom left corner

# Test current cell is bottom right corner

# Test current cell is top row (not a corner)

# Test current cell is bottom row (not a corner)

# Test current cell is left column (not a corner)

# Test current cell is right column (not a corner)

# Test current cell is a "middle" cell of a 3 x 3 with one mine (northwest)
# Test [ [*, ., .],  "c" denotes current cell
#        [., c, .],
#        [., ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (north)
# Test [ [., *, .],  "c" denotes current cell
#        [., c, .],
#        [., ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (northeast)
# Test [ [., ., *],  "c" denotes current cell
#        [., c, .],
#        [., ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (west)
# Test [ [., ., .],  "c" denotes current cell
#        [*, c, .],
#        [., ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (east)
# Test [ [., ., .],  "c" denotes current cell
#        [., c, *],
#        [., ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (southwest)
# Test [ [., ., .],  "c" denotes current cell
#        [., c, .],
#        [*, ., .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (south)
# Test [ [., ., .],  "c" denotes current cell
#        [., c, .],
#        [., *, .] ]

# Test current cell is a "middle" cell of a 3 x 3 with one mine (southeast)
# Test [ [., ., .],  "c" denotes current cell
#        [., c, .],
#        [., ., *] ]


import unittest
from minesweeper_solver import MinesweeperSolver
from minesweeper_input_generator import MinesweeperInputGenerator


class MineweeperSolverTests(unittest.TestCase):

    ########################################
    ########## ANDREW'S TESTS  #############
    ########################################
    def test_init_object_type(self):
        ms = MinesweeperSolver("mines.txt", "test_output.txt")
        self.assertEqual(type(ms) == MinesweeperSolver, True, "Constructor should create a MinesweeperSolver object")

    # Test current cell is a "middle" cell of a 3 x 3 with one mine (northwest)
    # Test [ [*, ., .],  "c" denotes current cell
    #        [., c, .],
    #        [., ., .] ]
    def test_output_1x1_mine(self):
        mig = MinesweeperInputGenerator("unit_test_input.txt")
        mig.generate_field("*\n")
        mig.add_terminating_str()
        mig_output = mig.get_text()

        ms = MinesweeperSolver("unit_test_input.txt", "test_output.txt")
        ms.solve_all_minefields()
        ms.write_output()

        correct_output = "*\n0 0\n"
        with open("test_output.txt", 'r', encoding='utf-8') as f:
            ms_output = f.readlines()
            self.assertEqual(correct_output, ms_output, True)

    ########################################
    ########## FIKADU'S TESTS  #############
    ########################################



    ##########################################
    ########## TEMESGEN'S TESTS  #############
    ##########################################


if __name__ == '__main__':
    unittest.main()
