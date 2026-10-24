def calculate_total(price, quantity):
    total = price * quantity
    return total


def calculate_discount(total, discount_percent):
    discount = total * discount_percent / 100
    return discount


def display_bill(
    product_name,
    price,
    quantity,
    subtotal,
    discount_percent,
    discount_amount,
    final_total
):
    print("\n========================================")
    print("              SHOP BILL")
    print("========================================")

    print("Product:", product_name)
    print("Price per item:", price, "AED")
    print("Quantity:", quantity)
    print("Subtotal:", subtotal, "AED")
    print("Discount:", discount_percent, "%")
    print("Discount amount:", round(discount_amount, 2), "AED")

    print("----------------------------------------")
    print("Final total:", round(final_total, 2), "AED")
    print("========================================")


def main():
    print("SHOP BILLING & DISCOUNT CALCULATOR")
    print("----------------------------------")

    product_name = input("Enter product name: ").strip()
    price = float(input("Enter price per item (AED): "))
    quantity = int(input("Enter quantity: "))
    discount_percent = float(input("Enter discount percentage (0-100): "))

    if price < 0 or quantity <= 0 or discount_percent < 0 or discount_percent > 100:
        print("Invalid input. Please check your values.")
        return

    subtotal = calculate_total(price, quantity)

    discount_amount = calculate_discount(
        subtotal,
        discount_percent
    )

    final_total = subtotal - discount_amount

    display_bill(
        product_name,
        price,
        quantity,
        subtotal,
        discount_percent,
        discount_amount,
        final_total
    )


if __name__ == "__main__":
    main()
