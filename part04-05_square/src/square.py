# Copy here code of line function from previous exercise
def line(nr, s):
    if s != "":
        print(nr*s[0])
    else:
        print(nr*"*")

def square(size, character):
    # You should call function line here with proper parameters
    times = size
    while times > 0:

        line(size, character)
        times -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")