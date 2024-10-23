# Write your solution here
from random import shuffle, sample
def words(n: int, beginning: str)-> list:
    with open("words.txt") as new_file:
        lst = []
        for line in new_file:
            wrd = line.strip()
            

            if wrd.startswith(beginning):
                if wrd not in lst:
                    lst.append(wrd)
    if len(lst) < n:
        raise ValueError("Not enough suitable words can be found!")
    res =  sample(lst, n)
    
    return res


if __name__=="__main__":
    word_list = words(3, "ca")
    print(word_list)
