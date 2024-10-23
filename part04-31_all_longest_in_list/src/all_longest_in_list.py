# Write your solution here
def all_the_longest(lst:list):
    longest  = 0
    for el in lst:
        if len(el) > longest:
            longest = len(el)

    result = []
    for item in lst:
        if len(item) == longest:
            result.append(item)
    
    return result

if __name__=="__main__":
    outcome = all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
    print(outcome)