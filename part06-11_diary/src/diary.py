# Write your solution here
run = True
while run == True:

    print("1-add an enty, 2-read entries, 0-quit")

    funct = int(input("Fuction: "))

    if funct == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as  my_file:
            my_file.write(f"{entry}\n")
        print("Diary saved")
    
    elif funct == 2:
       
        with open("diary.txt") as my_file:
            for line in my_file:
                print(line)

    elif funct == 0:
        print("Bye now")
        run = False