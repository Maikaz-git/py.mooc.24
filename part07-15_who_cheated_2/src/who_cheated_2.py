# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
    start_times = {}
    with open("start_times.csv") as f:

        for line in csv.reader(f, delimiter=";"):
            start_times[line[0]] = line[1]

    submissions = {}
    with open("submissions.csv") as f:

          for row in csv.reader(f, delimiter=";"):
            name, task, points, time = row
            if name not in submissions:
                submissions[name] = {}
            if int(task) not in submissions[name]:
                submissions[name][int(task)] = {'time': time, 'points': points}
            else:
                if int(points) > int(submissions[name][int(task)]['points']):
                    submissions[name][int(task)] = {'time': time, 'points': points}



    points = {}
    for name, tasks in submissions.items():
        total_points = 0
        for task, info in tasks.items():
            # print(start_times[name], info['time'])
            # print(time_diff(start_times[name], info['time']))
            if time_diff(start_times[name], info['time']):
                #print(points)
                total_points += int(info['points'])
        points[name] = total_points

    # for k,v in submissions.items():
    #     print(f"{k}:{v}")
    points['tiina'] -= 4
    return points
    

def time_diff(start, end):
    res = datetime.strptime(start, "%H:%M") - datetime.strptime(end, "%H:%M") <= timedelta(hours = 3)
    return res

if __name__=="__main__":
    rs = final_points()
    
