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
                    item_price = float(input(f"Enter the price of item {i}: $"))
                    total_amount += item_price
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid price.")

        # Print the total amount
        print(f"The total amount for {num_items} items is: ${total_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter a valid number of items.")

    taxes = {'TX': 0.0625, 'UT': 0.0685, 'NV': 0.08, 'AL': 0.04, 'CA': 0.0825}

    state_code = str(input('Enter your state code: '))
    if taxes.has_key(state_code): 


if __name__ == "__main__":
    main()