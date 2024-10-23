# Write your solution here
import csv
from datetime import datetime

def cheaters():
    with open("start_times.csv") as f:
        dc = {}
        for line in csv.reader(f, delimiter=";"):
            print(line)
            time = line[1]
            time_obj = datetime(2000, 1, 1, *map(int, time.split(':')))
            dc[line[0]] = time_obj
    

    with open("submissions.csv") as f:
        lst = []
        for line in csv.reader(f, delimiter=";"):
            print(line)
            time =line[-1]
            time_obj2 = datetime(2000, 1, 1, *map(int, time.split(':')))
            x =(line[0], time_obj2 )
            lst.append(x)
    res = []
    for el in lst:
        for name,time in dc.items():
            if el[0] == name:
                diff = el[1] - time
                if diff.seconds / 60 > 180 and name not in res:
                    res.append(name)
                
    return res

if __name__=="__main__":
    res =cheaters()
    print(len(res))
