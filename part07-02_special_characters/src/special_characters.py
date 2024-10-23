# Write your solution here
import string
def separate_characters(my_string:str)-> tuple:
    letters = "".join([char for char in my_string if char in string.ascii_letters])
    puncht = "".join([char for char in my_string if char in string.punctuation])
    other_char = "".join([char for char in my_string if char not in string.ascii_letters and char not in string.punctuation])

    return(letters, puncht, other_char)

if __name__=="__main__":
    rs=separate_characters("äöäöwhat737s up!!!>>")
    print(rs)