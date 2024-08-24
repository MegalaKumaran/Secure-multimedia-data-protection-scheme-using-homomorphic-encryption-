import ctypes

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def decode_text(ciphertext):
    T = []
    tokens = ciphertext.split("#")
    for token in tokens:
        if token:  # Skip empty strings
            count = int(token[:-1])
            bit = int(token[-1:])
            T.extend([bit] * count)
    return T

def flatten_matrix(matrix):
    flattened = []
    for row in matrix:
        flattened.extend(row)
    return flattened

def rotate_shift_down(matrix, k1):
    for _ in range(k1):
        row = matrix.pop()
        matrix.insert(0, row)
    return matrix

def rotate_shift_up(matrix, k1):
    for _ in range(k1):
        row = matrix.pop(0)
        matrix.append(row)
    return matrix

def rotate_shift_right(matrix, k3):
    for _ in range(k3):
        for row in matrix:
            row.insert(0, row.pop())
    return matrix

def rotate_shift_left(matrix, k3):
    for _ in range(k3):
        for row in matrix:
            row.append(row.pop(0))
    return matrix

def decrypt(ciphertext, K):
    # Step 1: Decode the ciphertext to obtain T
    T = decode_text(ciphertext)
    
    # Step 2: Create the matrix MT
    q = len(T) // 8  # Number of rows in MT
    MT = []
    for i in range(8):
        row = T[i * q:(i + 1) * q]  # Extract 'q' binary digits from T to form a row in MT
        MT.append(row)
    
    # Step 3: Revert the transposition of the matrix
    transposed_matrix = transpose_matrix(MT)
    
    # Step 4: Apply the reverse rotation and shift operations
    if K[0] % 2 == 0:
        M1 = rotate_shift_down(transposed_matrix, K[1])
    else:
        M1 = rotate_shift_up(transposed_matrix, K[1])
    if K[2] % 2 == 0:
        M2 = rotate_shift_right(M1, K[3])
    else:
        M2 = rotate_shift_left(M1, K[3])
    
    # Step 5: Convert the binary matrix to plaintext
    P = ""
    for i in range(0, len(flatten_matrix(M2)), 8):
        binary_str = ''.join(map(str, flatten_matrix(M2)[i:i+8]))  # Get 8 bits at a time
        decimal_value = int(binary_str, 2)  # Convert binary string to decimal
        P += chr(decimal_value)  # Convert decimal value to ASCII character and append to P
    
    return P

# Reading ciphertext from file
with open("cipherText.txt", "r") as file:
    cipher_text = file.read().strip()

K = [0, 2, 1, 3]
decrypted_text = decrypt(cipher_text, K)

# Writing the output to a file
with open("restoredText.txt", "w") as file:
    file.write(decrypted_text)

# Displaying the decrypted text using the print function
print("Decrypted Text:")
print(decrypted_text)

# Displaying a pop-up message box using system's MessageBox
#MessageBox = ctypes.windll.user32.MessageBoxW
#MessageBox(None, decrypted_text, "Decrypted Text", 0)

with open("decryptedText.txt", "w") as file:
    file.write(decrypted_text)
