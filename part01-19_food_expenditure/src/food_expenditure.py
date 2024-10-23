# Write your solution here
times_cafe = float(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
money_per_week = float(input("How much money do you spend on groceries in a week?"))

daily = round(((times_cafe * lunch_price)+ money_per_week) / 7, 2)
weekly = round((times_cafe * lunch_price)+ money_per_week,2)
print("")
print(f"Average food expenditure:\nDaily: {daily} euros\nWeekly: {weekly} euros")