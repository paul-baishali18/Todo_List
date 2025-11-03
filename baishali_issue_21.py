# temperature converter issue 21
unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp= float(input("Enter the temperature you want to convert: "))
if unit=="C":
    converted_temp= (temp * 9/5) + 32
    print(f"{temp} degree Celsius is equal to {converted_temp} degree Fahrenheit.")

elif unit=="F":
    converted_temp= (temp - 32) * 5/9
    print(f"{temp} degree Fahrenheit is equal to {converted_temp} degree Celsius.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    