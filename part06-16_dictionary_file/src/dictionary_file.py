# Write your solution here

while True:
    print("1-Add word, 2-Search, 3-Quit")
    nr = int(input("Function: "))


    if nr == 1:
        fin_wrd = input("The word in Finnish: ")
        eng_wrd = input("The word in English: ")
        
        with open("dictionary.txt", "a") as my_file:
            line = fin_wrd + ";" + eng_wrd
            my_file.write(line+"\n") 
        
        print("Dictionary entry added")

    elif nr == 2:
        st = input("Search term: ")

        with open("dictionary.txt") as my_file:
            for line in my_file:
                parts = line.split(";")
                if st in parts[0] or st in parts[1]:
                    print(f"{parts[0]} - {parts[1]}")

    elif nr == 3:
        print("Bye!")
        break