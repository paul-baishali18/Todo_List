# program to swap two numbers
#using temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a ={a}, b ={b}")
temp=a
a=b 
b=temp
print(f"After swapping: a ={a}, b ={b}")
#without using temporary variable
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a ={a}, b ={b}")
a=a+b
b=a-b
a=a-b
print(f"After swapping: a ={a}, b ={b}")
#using python's special feature
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(f"Before swapping: a ={a}, b ={b}")
a,b=b,a
print(f"After swapping: a ={a}, b ={b}")