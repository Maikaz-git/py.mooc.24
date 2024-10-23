# Write your solution here
temp_F = int(input("Please type in a temperature (F):"))
        #(32°F − 32) × 5/9 = 0°C
temp_c = (temp_F - 32) * (5/9)

if temp_c < 0:
    print(f"{temp_F} degrees Fahrenheit equals {temp_c} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{temp_F} degrees Fahrenheit equals {temp_c} degrees Celsius")