# Write your solution here
class Checklist:

    def __init__(self, header:str, entries: str):
        
        self.header = header
        self.entries = entries


class Customer:

    def __init__(self, id:str, balance:float, discount:int):

        self.id = id
        self.balance = balance
        self.discount = discount

class Cable:

    def __init__(self, model:str, length:float, max_speed:int, bidirectional:bool):

        self.model = model
        self.length = length
        self.max_speed = max_speed
        self.bidirectional = bidirectional


 

if __name__=="__main__":
    check_list = Checklist("wu", [1])
    customer = Customer("rza", 1.4, 5)
    cable = Cable("super model", 1.3, 99, True)

    