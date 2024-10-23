
# Write your solution here
def print_sudoku(sudoku:list):
    
    char = "_ "
    for i in range(len(sudoku)):
        if i % 3 ==0:
            print()
        for j in range(len(sudoku[i])):

            if j % 3 == 0 and j != 0:
                print(" ", end="")
            if sudoku[i][j] != 0:
                print(f'{sudoku[i][j] } ', end="")
            if sudoku[i][j] == 0:
                print(char, end="")

        print()
        
    print()       
   

def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    list_copy = [list(sublist) for sublist in sudoku] ## need to use loop to make new copy of list
    
    
    list_copy[row_no][column_no] = number
    
 
    return list_copy


if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)