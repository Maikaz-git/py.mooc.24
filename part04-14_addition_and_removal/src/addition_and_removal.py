# Write your solution here

lst = []
print("The list is now []")
nr  = 1
while True:
    response = input("a(d)d, (r)emove or e(x)it: ").lower()

    if response == 'd':
        lst.append(nr)
        nr += 1
        print(f"The list is now {lst}")
    elif response == 'r':
        lst.pop()
        nr -= 1
        print(f"The list is now {lst}")
    elif response == 'x':
        print("Bye!")
        break