from typing import List


# create and show
def init_empty_grid() -> List[List[int]]:
    list1 = []

    for a in range(9):

        list1.append([0,0,0,0,0,0,0,0,0])

    print("\n".join(["\t".join([str(cell) for cell in row]) for row in list1]))

    return print(list1), print(len(list1))


def init_candidates() -> List[List[str]]:
    list2 = []

    for a in range(9):
        list2.append(["123456789"])

    print("\n".join(["\t".join([str(cell) for cell in row]) for row in list2]))

    return list2


def print_grid(grid: List[List[int]]):


    print("\n".join(["\t".join([str(cell) for cell in row]) for row in grid]))
    return print(grid)




def input_sudoku(arg):
    count_row = 0

    i = 0

    while True:

        row_input = input("Bitte gebe eine vollatändige Reihe für das Sodukofeld ein: ")

        for b in row_input:
            arg[count_row][i] = b

            i += 1

        count_row += 1

        if count_row == 9:
            return arg


def set_default_sudoku_grid():
    list=[[0,0,1,2,0,7,0,0,0],[0,6,2,0,0,0,0,0,0],[0,0,0,0,0,0,9,4,0],[0,0,0,9,8,0,0,0,3],[5,0,0,0,0,0,0,0,0],[7,0,0,0,3,0,0,2,1],[0,0,0,1,0,2,0,0,0],[0,7,0,8,0,0,4,1,0],[3,0,4,0,0,0,0,8,0]]
    return print(list),print("\n".join(["\t".join([str(cell) for cell in row]) for row in list]))


# Check
def is_present_in_row(grid: List[List[int]], row_index: int, digit: int) -> bool:
    List = grid
    row_part = []
    row = row_index - 1
    for i in range(row, row + 3):
        row_part.append(List[i])

    if digit in row_part:
        return True
    elif digit not in row_part:
        return False



def is_present_in_column(grid: List[List[int]], column_index: int, digit: int) -> bool:
    list = grid
    column_part = []
    column = column_index - 1
    for i in range(0, 10):
        column_part.append(list[i][column])

    if column in column_part:
        return True
    elif column not in column_part:
        return False


def is_present_in_block(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    pass


def is_possible_in_cell(grid: List[List[int]], row_index: int, column_index: int, digit: int) -> bool:
    pass


# Solve
def remove_impossible_candidates(grid: List[List[int]], candidates: List[List[str]]):
    pass


def set_value_in_cell_by_last_candidate(grid: List[List[int]], candidates: List[List[str]]) -> bool:
    pass


def find_lonely_candidate_in_row(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidate_in_column(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidate_in_block(candidates: List[List[str]], row_index: int, column_index: int):
    pass


def find_lonely_candidates(candidates: List[List[str]]):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
set_default_sudoku_grid()
