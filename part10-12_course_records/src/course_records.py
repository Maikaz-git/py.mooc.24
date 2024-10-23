class Course:
    def __init__(self, course_name:str):

        self.course_name = course_name
        self.grade = 0
        self.credits = 0

    def course_name(self):
        return self.course_name
    
    def grade(self):
        return self.grade
    
    def credits(self):
        return self.credits


    def add_grade(self, grade:int):
        if grade > self.grade:
            self.grade = grade

    def add_credits(self, credits:int):
        self.credits = credits


    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

class CourseData:
    def __init__(self):

        self.course = {}

    def add_course(self, name:str, credits:int, grade:int):
        if name not in self.course:
            self.course[name] = Course(name)
            self.course[name].add_credits(credits)
            
            self.course[name].add_grade(grade)
        else:
            self.course[name].add_grade(grade)

    def get_course_data(self, name:str):
        if name in self.course:
            print(f"{self.course[name]}")
        
        else: print("no entry for this course")

    def stats(self):
        comp_cors = len(self.course)
        total_credit = sum([self.course[name].credits for name in self.course] )
        total_grade = sum([self.course[name].grade for name in self.course] )


        print(f"{comp_cors} completed courses, a total of {total_credit} credits")

        print(f"mean {round(total_grade/comp_cors, 1)}")
        print("grade distribution")

        grade_distribution = {5: "",  4: "",  3: "",  2: "",  1: "" }
        for k,v in self.course.items():
             grade_distribution[self.course[k].grade] +="x" 
        
        for k,v in grade_distribution.items():
            print(f"{k}: {v}")

class CourseDataApp:
    def __init__(self):
        self.coursedata = CourseData()

    def help(self):
        print("1 add course")
        print("2 get courses data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.coursedata.add_course(course, credits, grade)

    def get_course_data(self):
        course =  input("course: ")
        self.coursedata.get_course_data(course)
    

    def statistics(self):
        self.coursedata.stats()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()

            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                pass


ps = CourseDataApp()
ps.execute()