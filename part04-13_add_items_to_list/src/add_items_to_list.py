# Write your solution here

nr_of_items = int(input("How many items: "))
lst = []

while nr_of_items > 0:
    nr = 1
    
    item = int(input(f"Item {nr}:"))
    
    lst.append(item)
    nr += 1
    nr_of_items -= 1

print(lst)