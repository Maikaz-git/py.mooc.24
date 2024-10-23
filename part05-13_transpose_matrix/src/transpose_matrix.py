# Write your solution here

def transpose(matrix: list):
   n = len(matrix)
   for el in matrix:
    print(el)

   for i in range(n):
    for j in range(i, n):

        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

  
if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    transpose(matrix)
    for el in matrix:
        print(f"         {el}")


