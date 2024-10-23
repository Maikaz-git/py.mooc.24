# Write your solution here
def no_shouting(lst:list)-> list:
    result = []

    for el in lst:
        if el.upper() != el:
            result.append(el)
    return result

if __name__=="__main__":
    outcome = no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"])
    print(outcome)