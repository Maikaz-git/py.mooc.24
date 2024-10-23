# Write your solution here
def even_numbers(lst):
    result = []
    for nr in lst:
        if nr % 2 == 0:
            result.append(nr)
    return result

if __name__ == "__main__":
  even_numbers()