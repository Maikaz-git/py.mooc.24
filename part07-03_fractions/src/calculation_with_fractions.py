# Write your solution here
from fractions import Fraction

def fractionate(amount:int)-> list:
    lst = []
    for i in range(amount):
        lst.append(Fraction(1,amount))

    return lst


if __name__=="__main__":
    fractionate(5)