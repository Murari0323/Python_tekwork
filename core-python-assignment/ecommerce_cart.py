def calculate_total(cart_items):
    if not cart_items:
        return "Cart is empty"
    total = sum(cart_items.values())
    if len(cart_items) > 5:
        total *= 0.9
    return total

n = int(input("Enter number of items in cart: "))
cart_items = {}
for _ in range(n):
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    cart_items[item] = price
print("Total Price:", calculate_total(cart_items))
