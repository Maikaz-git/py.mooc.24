# Write your solution here
def same_chars(string, num1, num2):
    if len(string) <= num1 or len(string) <= num2:
        return False
    return string[num1] == string[num2]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))