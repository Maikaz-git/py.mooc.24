# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        lst = []
        for nr in new_file:

            nr = int(nr.replace("\n", ""))
            lst.append(nr)
        return max(lst)


if __name__ == "__main__":
    result = largest()
    print(result)