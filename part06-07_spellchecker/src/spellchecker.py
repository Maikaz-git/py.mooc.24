# write your solution here
with open("wordlist.txt") as new_file:
    lst = []
    for line in new_file:
        part = line.replace('\n',"")
        lst.append(part)


txt = input("Write text: ")
txt_lst =txt.split(" ")


res_lst = []
for el in txt_lst:
    if el.lower() not in lst:
        res_lst.append("*"+el+"*")
    else:
        res_lst.append(el)

print( " ".join(res_lst))

