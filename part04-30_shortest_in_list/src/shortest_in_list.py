# Write your solution here
def shortest(lst):
    remember = lst[0]

    for el in lst:
        if len(remember) > len(el):
            remember = el
    return remember


if __name__=="__main__":
    res = shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])

    print(res)