def caesar_cipher(text, shift):
    '''
    To encrypt a message using the Caesar cipher,
    we first choose a shift value (also called the key) 
    that determines how many positions to shift each letter. 
    Then, for each letter in the plaintext message, we shift 
    it by the specified number of positions in the alphabet. 
    If we reach the end of the alphabet, we wrap around to the beginning.
    '''
    # Convert text to uppercase
    text = text.upper()

    # Initialize empty result string
    result = ""

    # Iterate over each character in the text
    for char in text:
        # If character is a letter, apply the shift and append to result
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Otherwise, append the character as-is
        else:
            result += char
    print("Encrypted Caesar String: ", result)
    return result


# Read the input file
filename = 'input.txt'
with open(filename, 'r') as file:
    text = file.read()

# Encrypt the text using Caesar cipher and XOR with a salt
shift = 3
salt = 0b10101010
encrypted = ''.join([chr(ord(char) ^ salt)
                    for char in caesar_cipher(text, shift)])

# Write the encrypted text to a new file
out_filename = f"{filename.split('.')[0]}_enc.txt"
with open(out_filename, 'w') as file:
    file.write(encrypted)
