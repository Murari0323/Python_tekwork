'''
You are building a simple E-commerce application in Python. The system should maintain a list of products available in the cart. Write a Python program to perform the following operations using Lists:
1.Add a product to the cart.
2.Remove a product from the cart 
3.Search for a product in the cart 
4.Display all products in the cart
5.Show the total number of products in the cart
 
Cart Operations:
1. Add Product
2. Remove Product
3. Search Product
4. Display Cart
5. Count Products
6. Exit
 
Enter choice: 1
Enter product to add: Laptop
Product 'Laptop' added to cart.
 
Enter choice: 1
Enter product to add: Phone
Product 'Phone' added to cart.
 
Enter choice: 4
Cart: ['Laptop', 'Phone']
 
Enter choice: 3
Enter product to search: Phone
Yes, 'Phone' is in the cart.
 
Enter choice: 5
Total products in cart: 2
'''
def operations(list1):
    choice=int(input("Enter your choice: "))
    if choice==1:
        p=input("Enter product to add: ")
        list1.append(p)
        print(f"Product {p} added to cart")
        return True
    elif choice==2:
        p=input("Enter product to remove: ")
        list1.remove(p)
        print(f"Product {p} is removed from the list")
        return True
    elif choice==3:
        p=input("Enter product to search: ")
        if p in list1:
            print(f"Yes, {p} is in the cart")
        else:
            print(f"No, {p} is not present in the cart")
        return True
    elif choice==4:
        print(f"cart: {list1}")
        return True
    elif choice==5:
        print(f"Total products in cart: {len(list1)}")
        return True
    elif choice==8:
        print("Exiting...")
        return False
    elif choice==6:
        list1.sort()
        return True
        print(f"sorted list: {list1}")
    elif choice==7:
        list1.clear()
        print(f"list is cleared: {list1}")
        return True
    else:
        print("Enter Valid Choice")
        return True
  

list1=[]
c=True
while(c):
    print(f"cart operations: \n1. Add Product\n2.Remove Product\n 3. Search Product\n4. Display Cart\n5. count Products\n6.Sort items\n7.Clear items\n8. Exit")

    c=operations(list1)