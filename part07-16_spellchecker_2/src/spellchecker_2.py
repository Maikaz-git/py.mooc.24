# Write your solution here
import difflib

with open("wordlist.txt") as file:
    dictionary = []
    for line in file:
        word = line.strip("\n")
        dictionary.append(word)

# make input # compare input # print out mistakes

text = input("write text:")


words = text.split()



suggestions = []
p_list = []
dic = {}


for word in words[1:]:

    if word not in dictionary:
        suggestions = difflib.get_close_matches(word, dictionary)
        dic[word] = suggestions
        p_list.append(f"*{word}*")
    else:
        p_list.append(word)


print(words[0]+" " + " ".join(p_list))
print("suggestions:")    

for k,v in dic.items():
    print(f"{k}:{','.join(v)}")