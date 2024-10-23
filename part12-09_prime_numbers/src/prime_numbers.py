# Write your solution here
def prime_numbers():
   
    def is_prime(nr):
        if nr < 2:
            return False
        for i in range(2, int(nr**0.5)+1):
            if nr % i == 0:
                return False
        return True

    nr = 2
    while True:
        if is_prime(nr):
            yield nr
        nr += 1
   

if __name__=="__main__":
    numbers = prime_numbers()
    for i in range(5):
        print(next(numbers))