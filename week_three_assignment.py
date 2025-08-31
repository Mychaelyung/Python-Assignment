# 1. Create the calculate_discount function
def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:
        # Apply the discount
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return original price
        return price

# 2. Prompt user for input and use the function
try:
    # Get user input
    original_price = float(input("Enter the original price of the item: #"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the function
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display the result
    if discount_percentage >= 20:
        discount_amount = original_price - final_price
        print(f"Original price: #{original_price:.2f}")
        print(f"Discount applied: {discount_percentage}%")
        print(f"Discount amount: #{discount_amount:.2f}")
        print(f"Final price: #{final_price:.2f}")
    else:
        print(f"No discount applied (discount must be 20% or higher)")
        print(f"Final price: #{final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numeric values for price and discount percentage.")
