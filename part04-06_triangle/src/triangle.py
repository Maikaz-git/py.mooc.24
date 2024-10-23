# Copy here code of line function from previous exercise
def line(nr, s):
    if s != "":
        print(nr*s[0])
    else:
        print(nr*"*")
def triangle(size):
    # You should call function line here with proper parameters
    x = 1
    while x <= size:
        line(x, "#")
        x += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
