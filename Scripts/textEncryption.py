import sys
import ctypes

if len(sys.argv) < 2:
    print("Usage: python textEncryption.py <text>")
    sys.exit(1)

def convert_to_binary_ascii(text):
    binary_matrix = []
    for char in text:
        binary_value = bin(ord(char))[2:].zfill(8)
        binary_matrix.append([int(bit) for bit in binary_value])
    return binary_matrix

def rotate_shift_up(matrix, k1):
    for _ in range(k1):
        row = matrix.pop(0)
        matrix.append(row)
    return matrix

def rotate_shift_down(matrix, k1):
    for _ in range(k1):
        row = matrix.pop()
        matrix.insert(0, row)
    return matrix

def rotate_shift_left(matrix, k3):
    for _ in range(k3):
        for row in matrix:
            row.append(row.pop(0))
    return matrix

def rotate_shift_right(matrix, k3):
    for _ in range(k3):
        for row in matrix:
            row.insert(0, row.pop())
    return matrix

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def flatten_matrix(matrix):
    return [elem for row in matrix for elem in row]

def encode_text(T):
    encoded_text = ""
    count = 1
    prev_bit = T[0]
    for bit in T[1:]:
        if bit == prev_bit:
            count += 1
        else:
            encoded_text += str(count) + str(prev_bit) + '#'
            count = 1
            prev_bit = bit
    encoded_text += str(count) + str(prev_bit)
    return encoded_text

# Input from user
P = sys.argv[1]
K = [0, 2, 1, 3]

binary_matrix = convert_to_binary_ascii(P)

if K[0] % 2 == 0:
    M1 = rotate_shift_up(binary_matrix, K[1])
else:
    M1 = rotate_shift_down(binary_matrix, K[1])

if K[2] % 2 == 0:
    M2 = rotate_shift_left(M1, K[3])
else:
    M2 = rotate_shift_right(M1, K[3])

transposed_matrix = transpose_matrix(M2)

flattened_T = flatten_matrix(transposed_matrix)

cipher_text = encode_text(flattened_T)

# Writing the output to a file
with open("cipherText.txt", "w") as file:
    file.write(cipher_text)

# Displaying the cipher text using the print function
print("Cipher Text:")
print(cipher_text)

# Displaying a pop-up message box using system's MessageBox
#MessageBox = ctypes.windll.user32.MessageBoxW
#MessageBox(None, cipher_text, "Cipher Text", 0)