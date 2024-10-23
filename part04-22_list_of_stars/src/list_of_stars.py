# Write your solution here
def list_of_stars(lst:list):
    for el in lst:
        print(el * "*")
    
if __name__=="__main__":
    list_of_stars([3, 7, 1, 1, 2])