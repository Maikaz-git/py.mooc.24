# Write your solution here
#print("What is the weather foreast for tomorrow?")
temp = int(input('Temperature: '))
rain = input("Will it rain (yes/no): ").lower()

if temp > 20:
    print("Wear jeans and a T-shirt")
   

elif temp > 10:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well")
  

elif temp > 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
   
elif temp <= 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually/nI think gloves are in order")

if rain == 'yes':
    print("Don't forget your umbrella!")

