# Write your solution here
def sum_of_positives(lst):
    sum = 0
    for el in lst:
        if el > 0:
            sum += el
    return sum

if __name__ == "__main__":
   result  = sum_of_positives([-1, 2, 2, 6, -3])
   print(result)