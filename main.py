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
    user_choice = 'y'
    while user_choice == 'y':
        # Call add_product function to add a product
        add_product()
        # Ask the user if they want to add another product
        user_choice = input("\nWould you like to add another product?"
                            " (y/n): ").lower()   
        # Validate input to ensure it is either 'y' or 'n'
        while user_choice not in ['y', 'n']:
            user_choice = input("Invalid input. Please enter 'y' to add "
                                "another product or 'n' to proceed: ").lower()

def senior_discount(subtotal, senior_id):
    # Check if senior ID is provided
    if senior_id != "":
        # Calculate 10% discount and apply to subtotal
        discount = subtotal * 0.10 
        return subtotal - discount 
    # Return the full subtotal if no senior ID is provided
    return subtotal

def print_receipt(customer_name, senior_id, grand_total):
    # Print the receipt header
    print("\n----*---*---*---* RECEIPT *---*---*---*----")
    print("------------------------------------------")
    # Print the table headers for the items
    print(f"{'Item':<15}{'Price':<10}{'Qty':<10}{'Total':<10}")
    print("------------------------------------------")

    # Loop through each product in the lists and print details
    for product_index in range(len(name_list)):
        # Item name 
        print(f"{name_list[product_index]:<15}" 
             # Item price formatted to 2 decimal places
             f"{price_list[product_index]:<10.2f}" 
             # Quantity of items
             f"{quantity_list[product_index]:<10}"
             # Total cost formatted to 2 decimal places
             f"{total_list[product_index]:<10.2f}")
         
    print("------------------------------------------")
    # Print customer details and grand total
    print(f"Customer Name: {customer_name}")
    print(f"Senior ID No.: {senior_id}")
    print(f"Grand Total: {grand_total:.2f}")
    print("------------------------------------------")

# Call function ask_to_add_product
ask_to_add_product()
print("\n---*--- CUSTOMER INFORMATION ---*---")
# Input customer name and senior ID (leave blank if N/A)
customer_name = input("Enter Customer Name: ") 
# TODO (Althea Aragon): Add error handling for senior ID. Accept numbers only.
senior_id = input("Enter Senior ID (blank if not senior citizen): ")
# Calculate subtotal and apply senior discount if applicable
subtotal = sum(total_list)
# Compute grand total applying senior discount if applicable
grand_total = senior_discount(subtotal, senior_id)
# Print the final receipt
print_receipt(customer_name, senior_id, grand_total)