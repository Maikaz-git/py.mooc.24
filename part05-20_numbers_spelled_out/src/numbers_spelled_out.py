# Write your solution here
def dict_of_numbers()-> dict:

    ones = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:"five", 6:'six', 7:"seven", 8:'eight', 9:'nine'}
    afterones = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen", 17:"seventeen",18:"eighteen",19:"nineteen"}
    tens = {20:"twenty", 30:"thirty",40:"forty",50:"fifty",60:"sixty", 70:"seventy",80:"eighty",90:"ninety"}

    res = {}
    for i in range(0,100):
        if i < 10:
            res[i] = ones[i]
        elif i > 9 and i < 20:
            res[i] = afterones[i]
        elif i >= 20 and i % 10 != 0:
            y = i % 10
            res[i] = tens[i-y]+"-"+ones[y]
        elif i >= 20:
            if i % 10 == 0:
                res[i] = tens[i]
    return res

if __name__=="__main__":
    numbers  = dict_of_numbers()
    print(numbers[5])
    print(numbers[15])
    print(numbers[18])
    print(numbers[23])