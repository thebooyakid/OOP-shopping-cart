
# start small - break it down 

# what are the objects - shopping carts
# what are their attributes - cart dictionary for item and qty
# what are the piece of functionality - add / delete / show / quit
# what do they act on? - user input

# start simple
#     prevent you from being overwhelmed
#     prevent errors

# add functionality piece by piece and test as you go


class ShoppingCart():
    def __init__(self):
        self.cart = {}

    def show_items(self):
        if self.cart == {}:
            print("Your cart is empty")
        else:
            for item in self.cart:
                print(f'You have {self.cart[item]} {item}')

    def add_item(self):
        item = input("What would you like to add? ")
        amount = int(input("How many would you like to add? "))
        if item in self.cart:
            self.cart[item] += amount
        else:
            self.cart[item] = amount

    def delete_item(self):
        item = input("What would you like to delete? ") 
        if item.lower() in self.cart:
            del self.cart[item]
        else:
            print("That item isn't in your cart")



class UI():
    def __init__(self, shopping_cart):
        self.cart = shopping_cart

    def run_program(self):
        while True:
            action = input("Would you like to add, delete, show or quit? ")
            if action.lower() == "show":
                self.cart.show_items()
            elif action.lower() == "add":
                self.cart.add_item()
            elif action.lower() == "delete":
                self.cart.delete_item()
            elif action.lower() == "quit":
                self.cart.show_items()
                break
            else:
                print("Invalid input, try again buddy")



my_cart = ShoppingCart()
ui = UI(my_cart)
ui.run_program()
