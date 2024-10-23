# Write your solution here
def no_vowels(txt:str) -> str:
    result = ""
    vowels = ['a','e','i','o','u']

    for ltr in txt:
        if ltr not in vowels:
            result += ltr
    return result

if __name__=="__main__":
    outcome = no_vowels("this is an example")
    print(outcome)