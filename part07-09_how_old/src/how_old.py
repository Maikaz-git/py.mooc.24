# Write your solution here
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

millenium = datetime(1999, 12, 31)

birthday = datetime(year, month, day)

diff = millenium - birthday

if diff.days < 0:
    print(f"You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {diff.days} days old on the eve of the new millennium.")