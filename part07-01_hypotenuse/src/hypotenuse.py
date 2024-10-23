# Write your solution here
from math import sqrt

def hypotenuse(leg1: float, leg2: float)-> float:
    c = sqrt(leg2**2 + leg1**2)
    return c

if __name__=="__main__":
    hypotenuse(3, 4)