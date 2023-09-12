def main():
    try:
        # Ask for the number of items
        num_items = int(input("Enter the number of items: "))
        
        if num_items <= 0:
            print("Please enter a valid number of items greater than 0.")
            return

        total_amount = 0

        # Ask for the price of each item and calculate the total amount
        for i in range(1, num_items + 1):
            while True:
                try:
                    item_price = float(input(f"Enter the price of item {i}: "))
                    total_amount += item_price
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")

        # Print the total amount
        print(f"The total amount for {num_items} items is: {total_amount:.2f}.")
        price_calculator(total_amount)
        

        

    except ValueError:
        print("Invalid input. Please enter a valid number of items.")

    

def price_calculator(total_amount):

    taxes = {'TX': 0.0625, 'UT': 0.0685, 'NV': 0.08, 'AL': 0.04, 'CA': 0.0825}

    state_code = str(input('Enter your state code: '))

    if state_code in taxes: 
        tax = taxes[state_code]
        taxed_amount = (1 + tax) * total_amount
        print(f"{taxed_amount:.2f} is the price with VAT.")

        discount = get_discount_rate(taxed_amount)
        discount_amount = taxed_amount * (discount / 100)
        discounted_amount = taxed_amount-discount_amount
        print(f"{discount:.2f} is the discount percentage.")
        print(f"{discount_amount:.2f} is the discount amount.")

        print(f"{discounted_amount:.2f} is the discounted total price.")
    

    else:
        print('There is no such state code available.')
    



    
def get_discount_rate(total_amount):
    if 1000 <= total_amount < 5000:
        return 3
    elif 5000 <= total_amount < 7000:
        return 5
    elif 7000 <= total_amount < 10000:
        return 7
    elif 10000 <= total_amount < 50000:
        return 10
    elif total_amount >= 50000:
        return 15
    else:
        return 0



if __name__ == "__main__":
    main()


