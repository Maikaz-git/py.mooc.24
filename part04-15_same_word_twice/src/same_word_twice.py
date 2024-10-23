# Write your solution here
lst = []
while True:

    word = input("Word: ")
    
    if word not in lst:
        lst.append(word)
    else:
        break
print(F"You typed in {len(lst)} different words")