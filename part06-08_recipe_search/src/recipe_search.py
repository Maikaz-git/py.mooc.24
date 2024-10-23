# Write your solution here


def search_by_name(filename: str, word:str)-> list:

    with open(filename) as new_file:
        lst = []

        for line in new_file:
            part = line.replace("\n", "")
            lst.append(part)

        res = []
        for i in range(len(lst)):
            if word in lst[i].lower() and lst[i].lower() != word+"s":
                res.append(lst[i])
        return res
       
# found_recipes = search_by_name("recipes1.txt", "cake")

# for recipe in found_recipes:
#     print(recipe)

def search_by_time(filename: str, prep_time: int)->list:
    with open(filename) as new_file:
        lst = []

        for line in new_file:
            part = line.replace("\n", "")
            if part.isdigit():
                lst.append(int(part))
            else:
                lst.append(part)
        #print(lst)

        res = []
        for i in range(len(lst)):
            if type(lst[i]) == int and lst[i] <= prep_time:
                res.append(f"{lst[i-1]}, preparation time {lst[i]} min")
        return res

        
# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)

def search_by_ingredient(filename: str, ingredient: str):

    with open(filename) as new_file:
        lst = []
        matrx_lst = []
        for line in new_file:
            part = line.replace("\n", "")
            if part == "":
                lst.append(matrx_lst)
                matrx_lst = []
            else:
                matrx_lst.append(part)
        lst.append(matrx_lst)
       # print(lst)
        res = []

        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if ingredient == lst[i][j]:
                    res.append(f"{lst[i][0]}, preparation time {lst[i][1]} min")
        return res
    

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)

if __name__=="__main__":
    found_recipes = search_by_name("recipes2.txt", "oat")
    print(found_recipes)

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)