# Write your solution here

def row_sums(my_matrix: list):


    for i in range(len(my_matrix)):

        x = sum(my_matrix[i])

        my_matrix[i].append(x)

    

if __name__=="__main__":
    my_matrix = [[1, 1], [2, 2]]
    row_sums(my_matrix)
    print(my_matrix)