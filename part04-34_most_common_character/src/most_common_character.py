# Write your solution here
def most_common_character(txt:str):

    num = 0
    str = ""
    for el in txt:
        if txt.count(el) > num:
            num = txt.count(el)
            str = el
    return  str

if __name__=="__main__":
    outcome = most_common_character("exemplaryelementary")
    print(outcome)

