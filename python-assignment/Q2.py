number = 312     # Replace with any number you want

# Get the binary representation of the number
binary_str = bin(number)[2:]     # Remove the '0b' prefix

# Make the 2 most significant bits one
new_binary_str = '11' + binary_str[2:]

# Convert the new binary string back to decimal
new_number = int(new_binary_str, 2)

# Print the results
print("Original number:", number)
print("Original number in binary:", bin(number)[2:])
print("New number:", new_number)
print("New number in binary:", new_binary_str)
