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
    # TODO (Grace Lim): 
    # ask the user if it wants to add another product 
    # using y (yes) or n (no)
    # if "y", call the "add_product" function
    # if "n", end the loop
    pass

def senior_discount():
    # TODO (Althea Aragon):
    # Add a function that deducts 10% of the grand total of the products
    # if the user has typed in a Senior ID no.
    pass

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