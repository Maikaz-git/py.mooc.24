# Write your solution here
def row_correct(sudoku: list, row_no: int):
   
   row = sudoku[row_no]

   lst = [1,2,3,4,5,6,7,8,9]

   for nr in lst:
       if row.count(nr) > 1:
           return False
       
   return True 

def column_correct(sudoku: list, column_no: int) -> bool:
    lst = []
    for i in range(len(sudoku)):
        if sudoku[i][column_no] > 0 and sudoku[i][column_no] in lst:
            return False
        lst.append(sudoku[i][column_no])
    return True

def block_correct(sudoku: list, row_no: int, column_no: int)-> bool:
    lst = []

    el = sudoku[row_no][column_no]

    for i in range(3):
        for j in range(3):
            lst.append(sudoku[row_no+i][column_no+j])

    for el in lst:
        if el > 0 and lst.count(el) > 1:
            return False
    return True

def sudoku_grid_correct(sudoku: list)->bool:
   
    for i in range(len(sudoku)):
        if not row_correct(sudoku, i):
            return False
        
    for j in range(9):
        if not column_correct(sudoku, j):
            return False
        
    for r in range(0,len(sudoku)-2,3):
        for col in range(0,len(sudoku[r]),3):
            if not block_correct(sudoku, r, col):
                return False
   
    return True
        
    

if __name__=="__main__":
    sudoku = [
    [ 2, 6, 7, 8, 3, 9, 5, 0, 4 ],
    [ 9, 0, 3, 5, 1, 0, 6, 0, 0 ],
    [ 0, 5, 6, 0, 0, 0, 8, 3, 9 ],
    [ 5, 1, 9, 0, 4, 6, 3, 2, 8 ],
    [ 8, 0, 2, 1, 0, 5, 7, 0, 6 ],
    [ 6, 7, 4, 3, 2, 0, 0, 0, 5 ],
    [ 0, 0, 0, 4, 5, 7, 2, 6, 3 ],
    [ 3, 2, 0, 0, 8, 0, 0, 5, 7 ],
    [ 7, 4, 5, 0, 0, 3, 9, 0, 1 ],
    ]
    print(sudoku_grid_correct(sudoku))