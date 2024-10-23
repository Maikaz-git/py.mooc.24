# Write your solution here
def list_sum(lst1, lst2):
    result = []
    for i in range(len(lst1)):
        result.append(lst1[i]+lst2[i])
    return result

if __name__=="__main__":
    print(list_sum([1,3,5], [3,76,33]))