# Write your solution here
def filter_solutions():
     correct = []
     incorrect = []
     with open("solutions.csv") as my_file:
          for line in my_file:
              line = line.replace("\n","")
              # print(line)
              parts = line.split(";")
              if eval(parts[1]) == int(parts[2]):
                correct.append(parts)
               
              else:
                incorrect.append(parts)
    
     with open("correct.csv", "w") as new_file:
         for lst in correct:
             line = f"{lst[0]};{lst[1]};{lst[2]}"
             new_file.write(line+'\n')
    
     with open("incorrect.csv", "w") as new_file:
         for lst in incorrect:
             line = f"{lst[0]};{lst[1]};{lst[2]}"
             new_file.write(line+'\n')

if __name__=="__main__":
    
    filter_solutions()