# Write your solution here
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

for i in range(len(sudoku)-2,2):
    for j in range(len(sudoku[i])-2,2):
        #print(block_correct(sudoku, i , j))
        print(i,j)
                