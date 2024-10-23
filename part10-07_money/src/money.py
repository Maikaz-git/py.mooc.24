# TEE RATKAISUSI TÄHÄN:
class Money:
    
    def __init__(self, euros: int, _cents: int):
        c = 0
        self._cents = _cents
        self._euros = euros
        
        self._amount = self._euros + self._cents / 100

    def __str__(self):    
        return f"{self._amount:.2f} eur"

    def __eq__(self, another):      
        return another == self._amount

    def __lt__(self, another):
        return self._amount < another

    def __gt__(self, another):
        return self._amount > another
    def __ne__(self, another):
        return self._amount != another

    def __add__(self, another):
        total_eur = self._euros + another._euros
        total_cents = self._cents + another._cents
        if total_cents >= 100:
            total_eur += total_cents // 100
            total_cents = total_cents % 100
        
        return Money(total_eur, total_cents)
    
    def __sub__(self, other):
        other_money = other._euros + other._cents / 100
        if self._amount < other_money:
            raise ValueError(f"a negative result is not allowed")
        else:
            eur = self._euros - other._euros
            cents = self._cents - other._cents
            if cents < 0:
                eur -= 1
                cents += 100  
            return Money(eur ,cents)
if __name__=="__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

