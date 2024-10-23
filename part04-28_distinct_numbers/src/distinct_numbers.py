# Write your solution here
def distinct_numbers(lst):
    result = []

    for nr in lst:
        if nr not in  result:
            result.append(nr)
    return sorted(result)

if __name__ == "__main__":
    res = distinct_numbers([3, 2, 2, 1, 3, 3, 1])
    print(res)