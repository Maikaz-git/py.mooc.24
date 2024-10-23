# Write your solution here
h_wage = float(input("Hourly wage: "))
h_worked = float(input("Hours worked: "))
day = input("Day of the week: ").lower()

daily_wage = h_wage * h_worked

if day == "sunday":
    print(f"Daily wages: {daily_wage * 2} euros")
else:
    print(f"Daily wages: {daily_wage} euros")