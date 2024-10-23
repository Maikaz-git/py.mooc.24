# Write your solution here
from datetime import datetime
def is_it_valid(pic: str)-> bool:
    # finnish PICs valid format ddmmyyXyyyz
    range ="0123456789ABCDEFHJKLMNPRSTUVWXY"
    day = int(pic[0:2])
    month = int(pic[2:4])
    y = pic[4:6]
    cntr = pic[6]
    if cntr == "-":
        year = int("19" + y)
    elif cntr == "+":
        year = int("19" + y)
    elif cntr == "A":
        year = int("20" + y)
    else:
        return False
    yyy = int(pic[7:10])
    z = pic[10]
    
    
    res = ""
    for el in pic[:-1]:
        if el.isdigit():
            res += el
    index = int(res) % 31

    # print(day, month, year,  range[index])

    if z != str(range[index]) or len(pic) != 11 or month == 2 and day > 28 and cntr != "A":
        return False
    else:
        return True

if __name__=="__main__":
    print(is_it_valid("290200-1239"))
    print(19%31)