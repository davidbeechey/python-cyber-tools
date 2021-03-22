# Method 1 - 1 line

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

# Method 2 - longer, but better to understand what's going on

def xor_2(s1,s2):

    output = ""

    # loop through every character in the strings
    for i in range(len(s1)):

        # get current character
        current_char_s1 = s1[i]
        current_char_s2 = s2[i]

        # convert them into their ASCII values
        ascii_s1 = ord(current_char_s1)
        ascii_s2 = ord(current_char_s2)

        # apply XOR gate
        xor = ascii_s1 ^ ascii_s2

        # convert new ASCII value to a character
        character = chr(xor)

        # add that character to the output
        output += character
    
    return output

# Enter data and password

data = input("Enter the data to be encrypted/decrypted: ")
password = input("Enter the password: ")

# Test if it works

encrypted = xor_2(data,password)
print(f"Encrypted message: {encrypted}")

decrypted = xor_2(encrypted,password)
print(f"Derypted message: {decrypted}")
