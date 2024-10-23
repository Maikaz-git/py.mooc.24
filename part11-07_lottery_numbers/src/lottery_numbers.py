# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_nr:int, numbers:list):
        self.week_nr = week_nr
        self.numbers = numbers

    def number_of_hits(self, nums: list):
        return len([el for el in nums if el in self.numbers])

    def hits_in_place(self, nums:list):
        return [nr if nr in self.numbers else -1 for nr in nums]
 
if __name__=="__main__":
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))