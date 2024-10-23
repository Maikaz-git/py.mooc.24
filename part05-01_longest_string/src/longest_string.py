# Write your solution here
def longest(strings:list)->str:
    longest = ""
    for wrd in strings:
        if len(longest) < len(wrd):
            longest = wrd
    return longest

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))