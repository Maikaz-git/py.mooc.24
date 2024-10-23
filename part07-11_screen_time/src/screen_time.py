# Write your solution here
from datetime import datetime, timedelta

f_name = input("Filename:")
s_date = input("Starting date: ")
days = input("How many days: ")

start_d = datetime.strptime(s_date, "%d.%m.%Y")
final_d = start_d + timedelta(days=(int(days)-1))
print("Please type in screen time in minutes on each day (TV computer mobile):")

lst = []
total_time = 0

for i in range(int(days)):
   s_t = input(f"Screen time {start_d.day+i}.{start_d.month}.{start_d.year}:")
   parts = s_t.split(" ")
   total_time += sum([ int(el) for el in parts])
   f_part = "/".join(parts)

   f_i= start_d + timedelta(days=i) 
   x =  f_i.strftime("%02d.%02m.%Y")
   lst.append(f"{x}: {f_part}\n")

# print(lst)
# print(total_time)
formatted_date = start_d.strftime("%02d.%02m.%Y")
form_date = final_d.strftime("%02d.%02m.%Y")

with open(f_name, "w") as f:
    f.write(f"Time period: {formatted_date}-{form_date}\n")
    f.write(f"Total minutes: {total_time}\n")
    f.write(f"Average minutes: {total_time/ int(days)}\n")
    for i in range(len(lst)):
        f.write(f"{lst[i]}\n")