def pascal_triangle(n):
    for i in range(n):
        # spacing for triangle shape
        print(" " * (n - i), end=" ")
        
        # calculate values in row
        val = 1
        for j in range(i + 1):
            print(val, end=" ")
            val = val * (i - j) // (j + 1)  # nCr formula
        print()  # new line

num = int(input("Enter number of rows: "))
pascal_triangle(num)

