import math
# Write your solution here
student_nr = int(input("How many students on the course?"))
desired_size = int(input("Desired group size? "))

groups_formed = math.ceil(student_nr / desired_size)

print(f"Number of groups formed: {groups_formed}")