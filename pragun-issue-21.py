
temp=float(input("Enter the value of the temperature:"))

unit = input("Enter the units of the temperature entered:")
unit = unit.lower()

if unit == 'c':

    far = (temp * 9 / 5) + 32
    print("The farhenheit value is:", far)

    kelvin = temp + 273.15
    print("The kelvin value is:", kelvin)

elif unit == 'k':

    c = temp - 273.15
    print("The celcius temperature is:" , c)

    far = (temp - 32) / 1.8 + 273.15
    print("The farhenheit temperature is :", far)

else:

    k = (temp - 32) * 5 / 9 + 273.15
    print("The kelvin temperature is",k)

    c = (temp - 32) * 5 / 9
    print("The celcius temperature is:", c)
