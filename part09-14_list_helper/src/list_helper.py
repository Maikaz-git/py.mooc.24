# WRITE YOUR SOLUTION HERE:
class ListHelper:

   @classmethod
   def greatest_frequency(self,my_list: list):
        lst = []  
        for el in my_list:
            lst.append((my_list.count(el), el))            
        return max(lst)[1]

   @classmethod
   def doubles(self, my_list: list):
        count = 0
        lst = []
        for el in my_list:
            if my_list.count(el) >= 2 and el not in lst:
                lst.append(el)
                count +=1

        return count


if __name__=="__main__":
    numbers = [1, 1, 1, 2, 2, 3]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))