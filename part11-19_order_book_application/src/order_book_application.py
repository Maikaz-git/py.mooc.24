# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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
            workload_finished = sum([int(obj.workload) for obj in self.orders if obj.programmer == programmer and obj.is_finished()==True])
            workload_unf = sum([int(obj.workload) for obj in self.orders if obj.programmer == programmer and obj.is_finished()==False])

            return (finished_task, unfin_task, workload_finished, workload_unf )

class OrderBookApp:
    def __init__(self):
        self.orderbook = OrderBook()
    
    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add_order(self):
        try:
            description = input("description: ")
            pro_wrk = input("programmer and workload estimate:")
            programmer = pro_wrk.split(" ")[0]
            workload = int(pro_wrk.split(" ")[1])

            self.orderbook.add_order(description, programmer, str(workload))
            print("added!")
        except:
            print('erroneous input')

    def list_finished_tasks(self):
        res =  self.orderbook.finished_orders()
        if len(res) == 0:
            print("no finished tasks")
            return
        else: 
            for el in res:
                print(el)

    def list_unfinished_tasks(self):
        res =  self.orderbook.unfinished_orders()
        if len(res) == 0:
            print("no unfinished tasks")
            return
        else: 
            for el in res:
                print(el)
    
    def mark_task_as_finished(self):
        try:
            id = int(input("id: "))
            self.orderbook.mark_finished(id)
            print("marked as finished")
        except: print("erroneous input")

    def programmers(self):
        for el in self.orderbook.programmers():
            print(el)

    def status_of_programmer(self):
        try:
            programmer = input("programmer: ")
            tpl = self.orderbook.status_of_programmer(programmer)
            print(f"tasks: finished {tpl[0]} not finished {tpl[1]}, hours: done {tpl[2]} scheduled {tpl[3]}")
        except: print("erroneous input")
        
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()

            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == '4':
                self.mark_task_as_finished()
            elif command == '5':
                self.programmers()
            elif command == '6':
                self.status_of_programmer()
            else:
                pass 

ob = OrderBookApp()
ob.execute()