
class Stopwatch:

    def __init__(self):

        self.seconds = 0
        self.minutes = 0


    def tick(self):
        self.seconds += 1

        if self.seconds >= 60:
            self.minutes += 1
            self.seconds = 0

        if self.minutes >= 60:
            self.minutes = 0


    def __str__(self):

        return "%02d:%02d" % (self.minutes, self.seconds)



if __name__=="__main__":
    watch = Stopwatch()
    for i in range(3601):
        print(watch)
        watch.tick()