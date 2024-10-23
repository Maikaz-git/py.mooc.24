# Write your solution here
def spruce(tall):
    star = "*"
    space = " "*tall
   
    print("a spruce!")
    while tall > 0:
        print(space[:tall - 1]+star)
        star += "**"
        tall -= 1
    print(space[0:-1] + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)