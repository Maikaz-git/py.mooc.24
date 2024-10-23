class NumberStats:
    def __init__(self):
        self.number = 0
        self.nums = []

    def add_number(self, number:int):
        self.nums.append(number)

    def count_numbers(self):
        return len(self.nums)

    def get_sum(self):
        return sum(self.nums)

    def average(self):
        if len(self.nums) == 0:
            return 0
        else:
            return sum(self.nums) / len(self.nums)

    def sum_of_even_nums(self):
        
        return sum([nr for nr in self.nums if nr % 2 == 0])

    def sum_of_odd_nums(self):

        return sum([nr for nr in self.nums if nr % 2 != 0])
stats = NumberStats()
while True:

    input_nr = int(input("Please type in integer numbers: "))

    if input_nr == -1:
        
        print(f"Sum of numbers: {stats.get_sum()}")
        print(f"Mean of numbers: {stats.average()}")
        print(f"Sum of even numbers: {stats.sum_of_even_nums()}")
        print(f"Sum of odd numbers: {stats.sum_of_odd_nums()}")
        break
    else:
        stats.add_number(input_nr)