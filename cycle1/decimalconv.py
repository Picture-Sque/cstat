decimal_number = int(input("Enter a decimal number: "))

binary = bin(decimal_number)
octal = oct(decimal_number)
hexadecimal = hex(decimal_number)

print(f"Binary: {binary[2:]}")
print(f"Octal: {octal[2:]}")
print(f"Hexadecimal: {hexadecimal[2:].upper()}")
