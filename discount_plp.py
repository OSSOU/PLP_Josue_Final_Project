# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Output
if discount >= 20:
    print(f"Final price after {discount}% discount: {final_price}")
else:
    print(f"No discount applied. Price remains: {final_price}")
