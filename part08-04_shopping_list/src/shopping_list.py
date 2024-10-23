# DO NOT CHANGE THE CODE OF THE CLASS
# ShoppingList. Write yous solution under it!
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]

# -------------------------
# Write your solution here:
# -------------------------
def total_units( s_lst: ShoppingList):
    sum = 0
    
    for i in range(s_lst.number_of_items()):
        sum += s_lst.amount(i+1)
    
    return sum




if __name__ == "__main__":

    shopping_list = ShoppingList()
    shopping_list.add("bananas", 10)
    shopping_list.add("apples", 5)
    shopping_list.add("pineapple", 1)

    print(shopping_list.item(1))
    print(shopping_list.amount(1))
    print(shopping_list.item(2))
    print(shopping_list.amount(2))
    print(shopping_list.number_of_items())

    print(total_units(shopping_list))
