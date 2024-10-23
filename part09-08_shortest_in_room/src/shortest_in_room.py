# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):

        self.pers_lst = []


    def add(self, person:Person):
        self.pers_lst.append(person)


    def is_empty(self):
        
        if len(self.pers_lst) == 0:
            return True
        else: return False 
    

    def print_contents(self):
        pers_total = len(self.pers_lst)
        height_total = sum([el.height for el in self.pers_lst])
        print(f"There are {pers_total} persons in the room, and their combined height is {height_total} cm")
        for pers in self.pers_lst:
            print(pers)


    def shortest(self):
        if len(self.pers_lst) == 0:
            return None
        else:
            shortest = self.pers_lst[0].height
            pers = self.pers_lst[0]

            for el in self.pers_lst:
                if shortest > el.height:
                    pers = el
                    shortest = el.height
            return pers

    def remove_shortest(self):  
        if len(self.pers_lst) == 0:
            return None
        else:
            for el in self.pers_lst:
                if self.shortest() == el:
                    self.pers_lst.remove(el)
                    return el
        

if __name__=="__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed}")

    print()

    room.print_contents()