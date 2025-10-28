#temperature convertor issue 21
def c_to_f(celsius):
	return celsius * 9.0 / 5.0 + 32.0

def f_to_c(fahrenheit):	
    return (fahrenheit - 32.0) * 5.0 / 9.0

def main():
    temp = float(input("Enter temperature: "))
    scale = input("Convert to (C/F): ").upper()
    
    if scale == 'F':
        converted = c_to_f(temp)
        print(temp, "C is", converted, "F")
    elif scale == 'C':
        converted = f_to_c(temp)
        print(temp, "F is", converted, "C")
    else:
        print("Invalid scale. Please enter 'C' or 'F'.")

main()






