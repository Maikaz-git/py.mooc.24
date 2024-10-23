# tee ratkaisu tänne
# single responsibility funct
# program should 

import pprint as p

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_data = input("Course information: ")

else:
    course_data = "course1.txt"
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


course_tuple= ()
with open(course_data) as new_file:
    for line in new_file:
        parts = line.split(":")
        if parts[0] == "name":
            x = parts[1].strip()
        if parts[0] == "study credits":
            y = int(parts[1])
    course_tuple = (x, y)

resultxt_lst = [] 

course_p = f"{course_tuple[0]}, {course_tuple[1]} credits"

# print(course_p)
# print("=" * len(course_p))
resultxt_lst.append(course_p)
resultxt_lst.append("=" * len(course_p))


n,n1,n2,n3,n4,n5 = "name", "exec_nbr ", "exec_pts.", "exm_pts.", "tot_pts.", "grade"

#print( f"{n:<30}{n1:^10}{n2:^10}{n3:^9}{n4:^10}{n5:>6}")
resultxt_lst.append(f"{n:<30}{n1:^10}{n2:^10}{n3:^9}{n4:^10}{n5:>6}")


res_csv = []
for id, name in names.items():
    if id in ex_compl:  
        grade_sum = 0
        grade_sum = sum(points[id])
        
        # 40 completeted exesises is 100%
        compl_ex = sum(ex_compl[id])
        #print(compl_ex)
        #print(grade_sum)
        z = int((compl_ex / 40 * 10))  ## points for ex completed


        #print(int((compl_ex / 40 * 10)) )

        x = grade_sum
        grade_sum += z

        end_grade = 0
        if grade_sum < 15:
            end_grade = 0
        elif grade_sum < 18:
            end_grade = 1
        elif grade_sum < 21:
            end_grade = 2
        elif grade_sum < 24:
            end_grade = 3
        elif grade_sum < 28:
            end_grade = 4
        else:
            end_grade = 5
        
       # print(f"{names[id]: <26}{compl_ex: ^10}{z:^10}{x:^10}{grade_sum: ^ 10}{end_grade:>5}")
        resultxt_lst.append(f"{names[id]: <26}{compl_ex: ^10}{z:^10}{x:^10}{grade_sum: ^ 10}{end_grade:>5}")

        res_csv.append(f"{id};{names[id]};{end_grade}")
        #print(f"{id};{names[id]};{end_grade}")

with open("results.txt", "w") as my_file:
    for el in resultxt_lst:
        
        my_file.write(el+"\n")
my_file.close()

with open("results.csv", "w") as my_file:
    for el in res_csv:
        my_file.write(el+"\n")
my_file.close()

resultxt_lst = []
res_csv = []

print("Results written to files results.txt and results.csv")