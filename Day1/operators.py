def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

a=int(input("Enter the first operand: "))
b=int(input("Enter the second operand: "))


print("The addition of operands: ",add(a,b))
print("The substraction of operands: ",sub(a,b))
print("The multiplication of operands: ",mul(a,b))
print("The division of operands: ",div(a,b))
print("The modulus of operands: ",mod(a,b))