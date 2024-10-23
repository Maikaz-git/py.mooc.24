class Item:

    def __init__(self, name:str, weight:int):

        self.__name = name
        self.__weight = weight
        
  
    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:

    def __init__(self, max_weight:int):

        self.__max_weight = max_weight
        self.case = []


    def add_item(self, item:Item):

        case_w = sum([it.weight() for it in self.case])

        if case_w + item.weight() <= self.__max_weight:
            return self.case.append(item)


    def print_items(self):
        for item in self.case:
            print(item)

    def weight(self):
        return sum([it.weight() for it in self.case])

    def heaviest_item(self):
        if len(self.case) == 0:
            return None
        else:
            return max(self.case, key=lambda x:x.weight())

    def __str__(self):
        case_w = sum([it.weight() for it in self.case])
        it = "items"
        if len(self.case) == 1: it = 'item'
             
        return f"{len(self.case)} {it} ({case_w} kg)"


class CargoHold:

    def __init__(self, max_weight:int):

        self.__max_weight = max_weight
        self.cargo = []

    def add_suitcase(self, case:Suitcase):

        cargo_w = sum([it.weight() for it in self.cargo])

        if cargo_w + case.weight() <= self.__max_weight:
            return self.cargo.append(case)


    def print_items(self):
        for i in self.cargo:
            if i.print_items() != None:
                print(i.print_items())

    def __str__(self):
        space_left = self.__max_weight -  sum([it.weight() for it in self.cargo])
        suit_c = 'suitcase' if len(self.cargo) == 1 else "suitcases"
        return f"{len(self.cargo)} {suit_c}, space for {space_left} kg"


if __name__=="__main__":
    hold = CargoHold(100)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)