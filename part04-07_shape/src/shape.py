# Copy here code of line function from previous exercise and use it in your solution
def line(nr, s):
    if s != "":
        print(nr*s[0])
    else:
        print(nr*"*")

def shape(nr1, string1, nr2, string2):
    x = 1
    while x <= nr1:
        line(x, string1)
        x += 1
    y = 0
    while y < nr2:
        line(nr1, string2)
        y += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")