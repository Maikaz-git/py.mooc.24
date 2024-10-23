# Write your solution here:


class Task:
    id = 0
    @classmethod
    def new_id(cls):
        Task.id +=1
        return Task.id 

    def __init__(self, description:str, programmer:str, workload:int):
        self.description = description
        self.programmer = programmer
        self.workload = workload

        self.id = Task.new_id()
        self.task = "NOT FINISHED"

    def is_finished(self):
        if self.task == "NOT FINISHED":
            return False
        else: return True

    def mark_finished(self):
        self.task = "FINISHED"

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.task}" 

class OrderBook:

    def __init__(self):

        self.orders = []

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.orders.append(order)

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(set([el.programmer for el in self.orders]))

    def mark_finished(self, id:int):
        if id not in [obj.id for obj in self.orders]:
            raise ValueError("No such id")
        else: [obj.mark_finished() for obj in self.orders if obj.id == id]

    def finished_orders(self):
        return [obj for obj in self.orders if obj.is_finished() == True]

    def unfinished_orders(self):
        return [obj for obj in self.orders if obj.is_finished()== False]

    def status_of_programmer(self, programmer: str) -> tuple:
        if programmer not in [obj.programmer for obj in self.orders]:
            raise ValueError("No such programmer")
        else:
            
            finished_task = len([obj for obj in self.orders if obj.programmer == programmer and obj.is_finished() == True])
            unfin_task = len([obj for obj in self.orders if obj.programmer == programmer and obj.is_finished() == False])
            workload_finished = sum([obj.workload for obj in self.orders if obj.programmer == programmer and obj.is_finished()==True])
            workload_unf = sum([obj.workload for obj in self.orders if obj.programmer == programmer and obj.is_finished()==False])

            return (finished_task, unfin_task, workload_finished, workload_unf )

if __name__=="__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)