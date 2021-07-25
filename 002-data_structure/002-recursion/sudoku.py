######
## SOLVE SUDOKU
#####

from pprint import pprint

def find_next_empty(puzzle):
    # finds the next row and col on the puzzle thats not filled yet --> rep with -1
    # return row, col tuple (or (None, None)) if there is None

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None

def is_valid(puzzle, guess, row, col):
    # checks if the current guess is a valid guess or not
    # if the guess is not valid we return False, else True

    rows = puzzle[row]
    if guess in rows:
        return False

    cols = [puzzle[r][col] for r in range(9)]
    if guess in cols:
        return False
    
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True

def solve_sudoku(puzzle):
    # step1: first we find the next available pos to enter a number

    row, col = find_next_empty(puzzle)

    # step2: if None is returned from find_next_empty it means no new spaces available

    if row is None:
        return True
    
    # step3: if there is a place for us to guess
    # we guess from 1 to 9 
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        # step4: we check if the guess is valid
        if is_valid(puzzle, guess, row, col):
            # if this return true then our guess is correct
            puzzle[row][col] = guess

            # step5: we recursively call our puzzle with the new set value
            if solve_sudoku(puzzle):
                return True
        
        # step6: if not valid or if our guess does not solve the puzzle
        # we backtrack and try a new number
        puzzle[row][col] = -1 
    return False


if __name__ == '__main__':
    # example_board = [
    #     [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
    #     [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
    #     [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

    #     [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
    #     [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
    #     [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

    #     [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
    #     [6, 7, -1,   1, -1, 5,   -1, 4, -1],
    #     [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    # ]

    example_board = [
        [3, -1, 6, 5, -1, 8, 4, -1, -1],
        [5, 2, -1, -1, -1, -1, -1, -1, -1],
        [-1, 8, 7, -1, -1, -1, -1, 3, 1],

        [-1, -1, 3, -1, 1, -1, -1, 8, -1],
        [9, -1, -1, 8, 6, 3, -1, -1, 5],
        [-1, 5, -1, -1, 9, -1, 6, -1, -1],

        [1, 3, -1, -1, -1, -1, 2, 5, -1],
        [-1, -1, -1, -1, -1, -1, -1, 7, 4],
        [-1, -1, 5, 2, -1, 6, 3, -1, -1]
    ]

    print(solve_sudoku(example_board))
    pprint(example_board)
