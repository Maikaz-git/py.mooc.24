# Write your solution here
def histogram(wrd:str):
    result = {}
    for el in wrd:
        if el not in result:
            result[el] = "*" * wrd.count(el)
    
    for el in result:
        print(f"{el} {result[el]}")

if __name__=="__main__":
    histogram("statistically")