# Write your solution here
def even_numbers(beginning: int, maximus: int):

   nr = beginning
   while nr <= maximus:
        if nr % 2 == 0:
            yield nr
            nr += 2
        else: 
            nr += 1
           
if __name__=="__main__":
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)