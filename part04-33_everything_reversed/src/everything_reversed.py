# Write your solution here
def everything_reversed(lst:list)->list:
    result = []
    for el in lst:
        result.append(el[::-1])
    
    return result[::-1]

if __name__=="__main__":
    outcome = everything_reversed(["Hi", "there", "example", "one more"])
    print(outcome)