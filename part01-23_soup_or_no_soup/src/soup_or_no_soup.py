# Write your solution here
name = input("Please tell me your name: ")
if name != "Jerry":
    soup_nr = int(input("How many portions of soup? "))
    print(f"The total cost is {soup_nr * 5.9}")
    print("Next please!")
    
else:
    print("Next please!")