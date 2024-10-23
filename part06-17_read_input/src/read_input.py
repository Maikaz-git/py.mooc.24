# Write your solution here
def read_input(txt:str, x, y):

    while True:

        try:
            input_str = input(f"{txt} ")
            nr = int(input_str)
            if nr > x and nr < y:
                #print("fine")
                return nr
            else:
                print(f"You must type in an integer between {x} and {y}") 

        except ValueError:
            print(f"You must type in an integer between {x} and {y}") 



            

if __name__=="__main__":
    number = read_input("Please type in a number: ", 1, 5)
    print("You typed in:", number)  