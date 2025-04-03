def calculate_discount(price: int, discount_percent: int) -> int:
    if discount_percent >= 20:
        return price - (price * (discount_percent / 100))
    else:
        return price


price = int(input("Enter the original price of the product: "))
discount_percent = int(input("Enter the percentage discount you'd like to apply: "))
print(f"The final price of your product is {calculate_discount(price, discount_percent)}")
