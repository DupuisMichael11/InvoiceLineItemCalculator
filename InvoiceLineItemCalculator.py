#Michael Dupuis CIS261 Invoice Linee Item Calculator App


def get_price():
    while True:
        try:
            price = float(input("Enter Price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
            
def get_quantity():
    while True:
        try:    
            quantity = int(input("Enter Quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity. Please try again.")
            
if __name__ == "__main__":
    print("The Invoice Line Item Calculator\n")
    
    answer = "y"
    while answer.lower() == "y":
        price = get_price()
        quantity = get_quantity()
        
        total = price * quantity
        
        print()
        print("Price:  ", f"{price: .2f}")
        print("Quantity: ", quantity)
        print("Total: ",  f"{total: .2f}")
        answer = input("Enter another line item? (y/n): ")
        print()
        
    print("Have a good day!")
        
    
            
            
