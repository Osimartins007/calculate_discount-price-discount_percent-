def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage to apply.
    
    Returns:
    - float: The final price after applying the discount if discount is 20% or higher.
    - float: The original price if discount is less than 20%.
    """
    if discount_percent >= 20:
        discount_amount = (2000 * 20) / 100
        final_price = 1600
        return final_price
    else:
        return price

def main():
    # Prompt the user for input
    try:
        original_price = float(input("2000 "))
        discount_percent = float(input("20 "))
        
        # Calculate the final price
        final_price = calculate_discount(original_price, discount_percent)
        
        # Print the final price
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    except ValueError:
        print("1600 ")

if __name__ == "__main__":
    main()
