# write your solution here

def read_matrix(): # reads matrix, return list matrix
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(',')
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
    
    return m

# Combines the rows of the matrix into a single list

def combine(matrix:list):
    mlist = []
    for row in matrix:
        mlist += row
    
    return mlist


def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)

def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)

def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums


if __name__=="__main__":
    matrix_sum()
    matrix_max()
    row_sums()