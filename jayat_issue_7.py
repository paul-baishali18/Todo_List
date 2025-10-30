#convert binary number to decimal number

def binary_to_decimal(binary_str):
    decimal_number = 0
    binary_str = binary_str[::-1]  # Reverse the string to process from least significant bit
    for index, digit in enumerate(binary_str):
        if digit == '1':
            decimal_number += 2 ** index
    return decimal_number
def main():
    binary_input = input("Enter a binary number: ")
    decimal_output = binary_to_decimal(binary_input)
    print("The decimal equivalent of binary", binary_input, "is", decimal_output)

main()
