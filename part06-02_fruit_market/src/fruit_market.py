# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits = {}
        for line in new_file:
            #line = line.replace("\n", "")
            part = line.split(";")

            fruits[part[0]] = float(part[1])

        return fruits

if __name__=="__main__":
    res =read_fruits()
    print(res)