# Write your solution here
def invert(dictionary: dict)-> dict:
    res = {}
    for key,value in dictionary.items():
        res[value]=key
        
    dictionary.clear()

    for key, value in res.items():
        dictionary[key] = value

if __name__=="__main__":
    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s)

# Other way to delete use meth pop()
# staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
# deleted = staff.pop("Paul", None)
# if deleted == None:
#   print("This person is not a staff member")
# else:
#   print(deleted, "deleted")