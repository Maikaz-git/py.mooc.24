# Write your solution here

def filter_incorrect():
    # week x;
    # 7 integers, between 1-39
    with open("lottery_numbers.csv") as new_file:
        res = {}
        for line in new_file:
            row = line.split(";")
            week, numbers = row
            w = week.split(" ")
            if w[1].isdigit():
                wk = week
                xn = numbers

                nums = xn.strip()
                ns =nums.split(',')
                if len(ns) == 7:
                    lst = []
                    for el in ns:
                        if el.isdigit() and ns.count(el) == 1 and int(el) >= 1 and int(el) <= 39:
                            lst.append(el)
                    if len(lst) ==7:
                        res[wk] = lst

    with open("correct_numbers.csv", "w") as new_file:
        for k,v in res.items():
            new_file.write(f"{k};{','.join(v)}\n") 
    return res
    
if __name__=="__main__":
   res= filter_incorrect()
   for k,v in res.items():
       print(k,v)
   print(len(res))