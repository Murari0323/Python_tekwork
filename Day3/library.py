def libraryManagement(d, c):
    choice = int(input("\nEnter your choice: "))

    if choice == 1:  # Add a book
        p = input("Enter book name to add: ")
        d[c] = p
        print(f"Book '{p}' added to library with ID {c}")
        c += 1
        return True, c

    elif choice == 2:  # Remove a book
        p = int(input("Enter book ID to remove: "))
        if p in d:
            val = d.pop(p)
            print(f"Book '{val}' removed from the library")
        else:
            print("Invalid book ID")
        return True, c

    elif choice == 3:  # Search by ID
        p = int(input("Enter book ID to search: "))
        if p in d:
            print(f"Book found → ID: {p}, Title: {d[p]}")
        else:
            print(f"No book with ID {p} found in the library")
        return True, c

    elif choice == 4:  # Update title
        k = int(input("Enter book ID to update: "))
        if k in d:
            v = input("Enter new title: ")
            d[k] = v
            print(f"Book ID {k} updated to '{v}'")
        else:
            print("Invalid book ID")
        return True, c

    elif choice == 5:  # Display all
        print("All books in library:")
        for key, value in d.items():
            print(f"ID: {key}, Title: {value}")
        return True, c

    elif choice == 6:  # Count
        print(f"Total number of books: {len(d)}")
        return True, c

    elif choice == 7:  # Search by title
        v = input("Enter a book title: ")
        if v in d.values():
            print("Title exists in the library")
        else:
            print("Title does not exist")
        return True, c

    elif choice == 8:  # Exit
        print("Exiting...")
        return False, c

    else:
        print("Enter Valid Choice")
        return True, c


# Main Program
d = {}
c = 101  # starting ID
k = True

while k:
    print("\nLibrary Operations:")
    print("1. Add a book\n2. Remove a book\n3. Search by ID\n4. Update title\n"
          "5. Display all books\n6. Count total books\n7. Check if title exists\n8. Exit")

    k, c = libraryManagement(d, c)
