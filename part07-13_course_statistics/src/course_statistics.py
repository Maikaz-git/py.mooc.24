# Write your solution here
import urllib.request
import json
import math

def retrieve_all():

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    f = urllib.request.urlopen(url)
    data = f.read()
    courses = json.loads(data)

    active_courses = [(course['fullName'], course['name'], course['year'], sum(course['exercises'])) for course in courses if course['enabled']]

    return active_courses
    



def retrieve_course(course_name):
    

    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/" + course_name + "/stats"
    f = urllib.request.urlopen(url)

    data = f.read()
    d_json = json.loads(data)


    
    res = {}
    
    weeks = len(d_json)
    hours = 0
    exercises = 0

    students = 0
    
    print(d_json)

    for k,v in d_json.items():
      
        if students < v['students']:
            students = v['students']
       

        exercises += v['exercise_total']
        hours += v['hour_total']

    hours_average = math.floor(hours / students )   
    exercises_average = math.floor( exercises / students)

    res['weeks'] = weeks
    res['students'] = students
    res['hours'] = hours
    res['hours_average'] = hours_average
    res['exercises'] = exercises
    res['exercises_average'] = exercises_average

    
    return res

if __name__=="__main__":
    res = retrieve_all()
    print(res)
    print(retrieve_course("CCFUN"))