# Write your solution here
phone_book= {}
command_nr = 0

while command_nr != 3:

    command_nr = int(input("(1 search, 2 add, 3 quit): "))


    if command_nr == 1:
        name_nr = input("name: ").lower()
        for key in phone_book:
            if key == name_nr:
                print(phone_book[name_nr])

        if name_nr not in phone_book:
            print("no number")
            
                

    elif command_nr == 2:
        name_in = input("name: ").lower()
        number_in = input("number: ")
        print("ok!")
        phone_book[name_in] = number_in
        #print(phone_book)
    
print("quitting...")
