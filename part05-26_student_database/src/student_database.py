# Write your solution here
def add_student(dic: dict, name:str):
    # add student to dict
    dic[name] = "no completed courses"
    return dic

def print_student(dic: dict, name:str):

        if name in dic and type(dic[name]) == list:
            print(f"{name}:")
            print(f" {len(dic[name])} completed courses:")
            sum = 0
            for el in dic[name]:
                sum += el[1]
                print("  "+el[0],f"{el[1]}")
            if sum == 0:
                print("average grade 0")
            else:
                print(f" average grade {sum/len(dic[name])}")



        elif name in dic:
            print(f"{name}: \n {dic[name]}")
        else:
            print(f"{name}: no such person in the database")

def add_course(dic:dict, name:str , course_grade: tuple)->dict:
   
    # students["Peter"][0][0] value of first tuple
    if course_grade[1] == 0:
        return

    elif type(dic[name]) is not list:
        dic[name] = []
        if course_grade[1] > 0:
            dic[name].append(course_grade)

    
    for k,v in dic.items():
        for i in range(len(v)):
            if name == k and course_grade[0] == v[i][0] and course_grade[1] > v[i][1]:
                v.pop(i)
                v.append(course_grade)


            elif name == k and course_grade[0] != v[i][0] :
                #print(course_grade[0],v[i][0])
                if course_grade[0] != v[len(v)-1][0]:
                    v.append(course_grade)
            #print(f"key: {k},  value: {v}")
   
    #print(dic)
    #print(f"after:{dic}")
    
def summary(dic:dict):
   # students_nr
    student_num = len(dic)

   # most courses completed 3 Peter
    most_course = 0
    most = ()
    for el in dic:
        if most_course < len(dic[el]):
            most_course = len(dic[el])
            most = el, len(dic[el])

    name, nr = most
    print(f"students {student_num}")
    print(f"most courses completed {nr} {name}")
    
    # best average grade and student
    # grade sum / len(lst)
    highest_avrg = (0,0)
    for el in dic:

        totalgrades = 0
        for grade in dic[el]:
            totalgrades += grade[1]

        average = totalgrades / len(dic[el])
        
        if highest_avrg[1] <= average:
            highest_avrg = (el, average)
    
    stud, arg = highest_avrg
    print(f"best average grade {arg} {stud}")

if __name__=="__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)