class Clock:

    def __init__(self, hour:int, min:int, sec:int):
        self.hour = hour
        self.min = min
        self.sec = sec

    def tick(self):
        self.sec += 1

        if self.sec > 59:
            self.min += 1
            self.sec = 0
        
        if self.min > 59:
            self.hour += 1
            self.min = 0
        
        if self.hour > 23:
            self.hour = 0

    def set(self, hour:int, min:int):
        self.hour = hour
        self.min = min
        self.sec = 0


    def __str__(self):
        return f"{self.hour:02d}:{self.min:02d}:{self.sec:02d}"

if __name__=="__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
