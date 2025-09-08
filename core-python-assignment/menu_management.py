def add_item(menu, item):
    menu.append(item)

def remove_item(menu, item):
    if item in menu:
        menu.remove(item)

def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    return f"{item} is not available"

menu = input("Enter initial menu items separated by space: ").split()
add_item(menu, input("Enter item to add: "))
remove_item(menu, input("Enter item to remove: "))
print("Updated menu:", menu)
print("Availability:", check_item(menu, input("Enter item to check: ")))
