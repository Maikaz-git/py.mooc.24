# Write your solution here
from random import sample
def lottery_numbers(amount:int, lower:int, upper:int)->list:

    num_pool= list(range(lower, upper))
    draw = sample(num_pool, amount)
    draw.sort()
    return draw

if __name__=="__main__":
    lottery_numbers(9, 1, 59)