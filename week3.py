def calculate_discount(price, discount_percent):
    #Calculates the final price after applying a discount.
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"Final price after applying discount: ${final_price:.2f}")
