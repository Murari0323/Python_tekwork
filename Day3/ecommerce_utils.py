def apply_discount(price, discount_percent):
    """Apply discount to price"""
    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


def add_gst(price, gst_percent=18):
    """Add GST to price"""
    gst_amount = price * (gst_percent / 100)
    return price + gst_amount


def generate_invoice(cart, discount_percent=0, gst_percent=18):
    """Generate and print invoice"""
    print("------ INVOICE ------")

    subtotal = 0
    for product, price in cart.items():
        print(f"{product:<15}: ₹{price}")
        subtotal += price

    print("-" * 21)
    print(f"Subtotal: ₹{subtotal}")

    # Apply discount
    discounted_price = apply_discount(subtotal, discount_percent)
    if discount_percent > 0:
        print(f"After {discount_percent}% discount: ₹{discounted_price}")

    # Apply GST
    final_price = add_gst(discounted_price, gst_percent)
    print(f"After {gst_percent}% GST: ₹{final_price:.2f}")
    print("-" * 21)
    print("Thank you for shopping with us!")
