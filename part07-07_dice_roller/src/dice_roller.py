# Write your solution here
from random import randint

def roll(die:str):
   res = { "a" : [3,3,3,3,3,6],
        "b" : [2,2,2,5,5,5],
        "c": [1,4,4,4,4,4]
        }
   return res[die.lower()][randint(0,5)]


def play(die1: str, die2: str, times: int)-> tuple:
    die1_won = 0
    die2_won = 0
    tie = 0

    for i in range(times):

        x = roll(die1)
        y = roll(die2)
    
        if x > y:
            die1_won += 1

        elif y > x:
            die2_won += 1
        else :
            tie += 1
            
    return (die1_won, die2_won, tie)
if __name__== "__main__":
    play("A", "C", 50)
    play("B", "B", 1000)