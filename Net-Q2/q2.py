def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        if digit != '0' and digit != '1':
            return None
        decimal = decimal * 2 + int(digit)
    return decimal
binary_num = input("Enter a binary number: ")
decimal_num = binary_to_decimal(binary_num)

if decimal_num is not None:
    print(f"The decimal equivalent of {binary_num} is: {decimal_num}")
else:
    print("Invalid input.")