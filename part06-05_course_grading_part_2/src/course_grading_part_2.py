# wwite your solution here

# write your solution here
import pprint as p

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")

else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_points = "exam_points1.csv"
# lets make helper data structures dict

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")

        if parts[0] == "id":
            continue

        names[parts[0]] = (parts[1]) +" "+ parts[2].strip()


# p.pprint(names)

ex_compl = {} # exercises completed

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")

        if parts[0] == 'id':
            continue

        ex_compl[parts[0]] = [] # we sign list to dict key
        for grade in parts[1:]: # then we go true parts list from second el to last el
            ex_compl[parts[0]].append(int(grade.strip())) # finally append to list int that was str we stripped unnessesery parts : )

#p.pprint(ex_compl)

# print("ex_compl: ")

points = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(";")

        if parts[0] == "id":
            continue

        points[parts[0]] = []

        for grade in parts[1:]:
            points[parts[0]].append(int(grade.strip()))

#p.pprint(points)




for id, name in names.items():
    if id in ex_compl:  
        
        grade_sum = sum(points[id])
        
        # 40 completeted exesises is 100%
        compl_ex = sum(ex_compl[id])
        #print(compl_ex)
        #print(grade_sum)
        z = int((compl_ex / 40 * 10))  ## points for ex completed


        #print(int((compl_ex / 40 * 10)) )

       
        grade_sum += z

        if grade_sum < 15:
            print(f"{names[id]} 0")
        elif grade_sum < 18:
            print(f"{names[id]} 1")
        elif grade_sum < 21:
            print(f"{names[id]} 2")
        elif grade_sum < 24:
            print(f"{names[id]} 3")
        elif grade_sum < 28:
            print(f"{names[id]} 4")
        else:
            print(f"{names[id]} 5")

        
