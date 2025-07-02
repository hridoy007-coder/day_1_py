class Coffee:
    # initialize coffee with name and price set
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    # order with empty list of coffees
    def __init__(self):
        self.items = []
    
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to the order.")
    
    def total(self):
        return sum(item.price for item in self.items)
    
    def show_order(self):
        if not self.items:
            print("no orders yet")
            return
        print("\nYour order:")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        print(f"Total: ${self.total()}\n")

    # handle checkout process
    def checkout(self):
        if not self.items:
            print("no orders yet")
            return
        
        self.show_order()
        confirm = input("Proceed to checkout? (yes/no):").strip().lower()
        if confirm == "yes":
            print("Thank you for your order!")
            self.items.clear()
        else:
            print("Order cancelled.")\

# display menu and handle user input
def main():
    menu =[
        Coffee("Espresso", 2.50),
        Coffee("Americano", 3.00),
        Coffee("Latte", 3.50),
        Coffee("Cappuccino", 3.75),
    ]
    order = Order()

    # user interaction loop
    while True:
        print("\n--Coffee Menu:")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        
        print("5. view order")
        print("6. checkout")
        print("7. exit")

        choice = input("choose an  option:")
        if choice in ['1', '2', '3', '4',]:
            order.add_item(menu[int(choice)-1])
        elif choice == '5':
            order.show_order()
        
        elif choice == '6':
            order.checkout()

        elif choice == '7':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()