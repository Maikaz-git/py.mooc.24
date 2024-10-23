# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance:float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

   

    def subtract_from_balance(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def __str__(self):
        return f"{self.balance}"



class PaymentTerminal:
    def __init__(self):

        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        reg_lunch = 2.50
        if payment >= reg_lunch:
            self.funds += reg_lunch
            self.lunches += 1
            change = payment - reg_lunch
            return change
        else:
            return payment
            
    def eat_special(self, payment: float):
        special_lunch = 4.30
        if payment >= special_lunch:
            self.funds += special_lunch
            self.specials += 1
            change = payment - special_lunch
            return change
        else:
            return payment


    def eat_lunch_lunchcard(self, card: LunchCard):
        reg = 2.5
        if card.balance >= reg:
            card.subtract_from_balance(reg)
            
            self.lunches += 1
            return True
        else: return False


    def eat_special_lunchcard(self, card: LunchCard):
        spec = 4.3
        if card.balance >= spec:
            card.subtract_from_balance(spec)

            self.specials += 1
            return True
        else: return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount


if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)