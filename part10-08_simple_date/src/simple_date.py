# WRITE YOUR SOLUTION HERE:

class SimpleDate():

    def __init__(self, day:int, month:int, year:int):

        self._day = day
        self._month = month
        self._year = year

    def __str__(self):
        return f"{self._day}.{self._month}.{self._year}"


    #  <, >, == and !=
    def __lt__(self, another):
        a_total = (another._year * 360) + (another._month * 30) + another._day
        total = (self._day) + (self._month * 30) + (self._year * 360) 
        return total < a_total

    def __gt__(self, another):
        a_total = (another._year * 360) + (another._month * 30) + another._day
        total = (self._day) + (self._month * 30) + (self._year * 360) 
        return total > a_total

    def __eq__(self, another):
        a_total = (another._year * 360) + (another._month * 30) + another._day
        total = (self._day) + (self._month * 30) + (self._year * 360) 
        return total == a_total

    def __ne__(self, another):
        a_total = (another._year * 360) + (another._month * 30) + another._day
        total = (self._day) + (self._month * 30) + (self._year * 360)
        return total != a_total

    def __add__(self, nr:int):
        day =self._day +nr
        month = self._month
        year = self._year

        if day  > 30:
            month += day // 30
            day = day % 30
            if month > 12:             
                year += month // 12
                month = month % 12
       
        return SimpleDate(day, month, year)

    def __sub__(self,another):
        a_total = (another._year * 360) + (another._month * 30) + another._day
        total = (self._day) + (self._month * 30) + (self._year * 360)
        return abs(a_total-total)

if __name__=="__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)