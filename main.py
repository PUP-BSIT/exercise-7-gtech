# Add list for each product detail
name_list = []
price_list = []
quantity_list = []
total_list = []

def add_product():
    print("\n---*--- ADD PRODUCT ---*---")
    # Input product details
    product_name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    # Compute for the total cost for each product
    total = price * quantity 
    # Append each values to their corresponding list
    name_list.append(product_name) 
    price_list.append(price)
    quantity_list.append(quantity)
    total_list.append(total)

def ask_to_add_product():
    while True:
        # Call add_product function to add a product
        add_product()
        # Ask the user if they want to add another product
        user_choice = input("\nWould you like to add another product?"
                            " (y/n): ").lower()   
        # Validate input to ensure it is either 'y' or 'n'
        while user_choice not in ['y', 'n']:
            user_choice = input("Invalid input. Please enter 'y' to add "
                                "another product or 'n' to proceed: ").lower()
        # Exit in the loop when 'n' is entered
        if user_choice == 'n':
            break

def senior_discount(subtotal, senior_id):
    # Check if senior ID is provided
    if senior_id != "":
        # Calculate 10% discount and apply to subtotal
        discount = subtotal * 0.10 
        return subtotal - discount 
    # Return the full subtotal if no senior ID is provided
    return subtotal

def print_receipt():
    # TODO (Hoshea Lopez, Grace Lim):
    # Add a function that displays:
    # - Items (product name, price, quantity, total)
    # - Customer Name
    # - Senior ID no.
    # - Grand Total
    pass

# TODO (Rain Romero):
# Add a code that will allow the user to input 
# Customer Name and Senior ID (Optional).
# Use "senior_deduction" function to compute for the grand total

# TODO (Grace Lim):
# Compute the grand total outside of the function for direct computation

# TODO (Rain Romero):
# call the "print_receipt" function as final output