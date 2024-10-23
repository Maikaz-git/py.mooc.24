# Write your solution here
def line(nr, s):
    if s != "":
        print(nr*s[0])
    else:
        print(nr*"*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
