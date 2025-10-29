
con = int(input("MENU\n1:Convert binary to decimal\n2:Convert decimal to binary\n"))

if con == 1 or con == 2:

    num = input("Enter the number to be converted:")
    

    if con == 1:
        decimal  = int(num,2)
        print(decimal,"is the decimal number")

    elif con == 2:
        binary = bin(num,"is the binary number")
else:
    print("Invalid entry")
