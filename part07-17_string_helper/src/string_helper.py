# Write your solution here
import re

def change_case(orig_string: str) -> str:
    result = ""
    for ltr in orig_string:
        if ltr == ltr.lower():
            result += ltr.upper()
        elif ltr == ltr.upper():
            result += ltr.lower()
    return result

def split_in_half(orig_string: str) -> tuple:

    nr = len(orig_string) / 2
    if nr % 1 != 0:
        return (orig_string[:int(nr-0.5)], orig_string[int(nr-0.5):])
    else:
        return (orig_string[:int(nr)], orig_string[int(nr+0.5):])

def remove_special_characters(orig_string: str) -> str:
   new_string = re.sub(r'[^a-zA-Z0-9 ]+', '', orig_string)
   return new_string
    


if __name__=="__main__":
    change_case()
    split_in_half()
    remove_special_characters()