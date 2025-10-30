# Program to swap two numbers using a third variable and without using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"\nBefore swapping: a = {a}, b = {b}")

temp = a
a = b
b = temp
print(f"After swapping using third variable: a = {a}, b = {b}")

#Reset to original values
a,b=b,a

a = a + b
b = a - b
a = a - b
print(f"After swapping without using third variable: a = {a}, b = {b}")
