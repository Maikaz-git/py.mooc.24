# Write your solution here
def palindromes(word:str) -> bool:
    rev_word = "".join(reversed(word))
    if rev_word != word:
        return False
        
    else:
        return True
        
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def type_in_word():

    while True:

        wrd = input("Please type in a palindrome: ")

        if palindromes(wrd):
            print(f"{wrd} is a palindrome!")
            break
        
        print("that wasn't a palindrome")

type_in_word()
        
