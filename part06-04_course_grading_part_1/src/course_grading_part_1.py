# write your solution here
import pprint as p

if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")

else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

# lets make helper data structures dict

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(";")

        if parts[0] == "id":
            continue

        names[parts[0]] = (parts[1]) +" "+ parts[2].strip()


# p.pprint(names)

grades = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")

        if parts[0] == 'id':
            continue

        grades[parts[0]] = [] # we sign list to dict key
        for grade in parts[1:]: # then we go true parts list from second el to last el
            grades[parts[0]].append(int(grade.strip())) # finally append to list int that was str we stripped unnessesery parts : )

# p.pprint(grades)

# print("grades: ")

for id, name in names.items():
    if id in grades:
        print(f"{names[id]} {sum(grades[id])}")