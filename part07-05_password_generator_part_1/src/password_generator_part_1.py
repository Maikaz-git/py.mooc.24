# Write your solution here
from random import sample

def generate_password(num:int):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    pas = sample(alph, num)
    return "".join(pas)


if __name__=="__main__":
    generate_password(8)
    for i in range(5):
        print(generate_password(8))