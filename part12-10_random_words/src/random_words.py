# Write your solution here:
def  word_generator(characters: str, length: int, amount: int):
    from random import randint, choice

    # for i in range(amount):
    #     ch = ""
    #     for j in range(length):
    #         ch += characters[randint(0, len(characters)-1)]
        
    #     yield ch
   
    return ("".join([choice(characters) for i in range(length)])for j in range(amount))




if __name__=="__main__":
    wordgen = word_generator("abc", 2, 1)
    for word in wordgen:
        print(word)