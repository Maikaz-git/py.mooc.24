# Write your solution here
def create_tuple(x: int, y: int, z:int)-> tuple:
    lst = [x,y,z]
    lst.sort()

    return (lst[0],lst[2], sum(lst))


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))
