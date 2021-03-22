# Method 1 - 1 line

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

# Method 2 - use for loop

def xor_2(s1,s2):

    output = ""

    for i in range(len(s1)):
        output += chr(ord(s1[i]) ^ ord(s2[i]))
    
    return output

# Enter data and password

data = input("Enter the data to be encrypted/decrypted: ")
password = input("Enter the password: ")

# Test if it works

encrypted = xor_2(data,password)
print(f"Encrypted message: {encrypted}")

decrypted = xor_2(encrypted,password)
print(f"Derypted message: {decrypted}")
