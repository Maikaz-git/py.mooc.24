# Write your solution here
def ask_nums():
    result = []
    while True:
        nums_str = input("Exam points and exercises completed: ")
        if nums_str == "":
            break
        grade = nums_str.split(" ")
        exam_points = int(grade[0])
        exer_comp = int(grade[1])

        result.append((exam_points, exer_comp))
    return result

results = ask_nums() #[(15,87),(10,55),(11,40),(4, 17)]

def convert_to_points(lst:list):
    sum = 0
    arr = []
    count = 0
    for i in range(len(lst)):
        if lst[i][0] < 10:
            count += 1
            arr.append(0)
        elif lst[i][0] + lst[i][1]//10 < 15:
            count += 1
            arr.append(0)
        elif lst[i][0] + lst[i][1]//10 < 18:
            arr.append(1)
        elif lst[i][0] + lst[i][1]//10 < 21:
            arr.append(2)
        elif lst[i][0] + lst[i][1]//10 < 24:
            arr.append(3)
        elif lst[i][0] + lst[i][1]//10 < 28:
            arr.append(4)
        elif lst[i][0] + lst[i][1]//10 < 31:
            arr.append(5)
        sum += lst[i][0] + lst[i][1]//10
  
    avg = f"{sum/len(lst):.1f}"

    

    print("Statistics:")
    print(f"Points average: {avg}")
    print(f"Pass percentage: {((len(arr)-count) / len(arr)) * 100:.1f}") 
    print("Grade distribution:")
    for i in range(5,-1,-1):

        print(f"{i}: {'*'* arr.count(i)}")

convert_to_points(results)