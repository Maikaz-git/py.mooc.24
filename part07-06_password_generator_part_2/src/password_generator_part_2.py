 

from random import choice, randint, sample, shuffle
from string import ascii_lowercase, digits, punctuation

def generate_strong_password(length: int, nums:bool, chars:bool)->str:
    passwd = ""
    nums_ps = ""
    chars_ps = ""

    res = ""

    for i in range(length):       
        passwd += choice(ascii_lowercase)
    if nums:
        for i in range(length//3):
            nums_ps += choice(digits)
    if chars:
        for i in range(length//3):
            chars_ps += choice("!?=+-()#")
    all = passwd[0:len(passwd)- len(nums_ps)- len(chars_ps)] + nums_ps + chars_ps

    mylist = list(all)
    shuffle(mylist)
    
    return "".join(mylist)

    
     
    

if __name__=="__main__":
    res = generate_strong_password(8, True, True)
    print(res)
    for i in range(10):
        print(generate_strong_password(5, False, True))