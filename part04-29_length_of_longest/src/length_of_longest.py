# Write your solution here
def length_of_longest(lst):
    remember = len(lst[0])
    for el in lst:
        if remember < len(el):
            remember = len(el)
    return remember

if __name__ == "__main__":
    res = length_of_longest(['hola', "when", 'happening'])
    print(res)
