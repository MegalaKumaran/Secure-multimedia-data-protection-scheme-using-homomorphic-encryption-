import csv
import sys

if len(sys.argv) < 2:
    print("Usage: python RealTimeEncryption.py <file-path>")
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

def encrypt_csv(input_file, output_file):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            encrypted_row = []
            for cell in row:
                binary_matrix = convert_to_binary_ascii(cell)
                for i in range(0, len(K), 4):
                    if K[i] % 2 == 0:
                        M1 = rotate_shift_up(binary_matrix, K[i+1])
                    else:
                        M1 = rotate_shift_down(binary_matrix, K[i+1])

                    if K[i+2] % 2 == 0:
                        M2 = rotate_shift_left(M1, K[i+3])
                    else:
                        M2 = rotate_shift_right(M1, K[i+3])

                transposed_matrix = transpose_matrix(M2)
                flattened_T = flatten_matrix(transposed_matrix)
                cipher_text = encode_text(flattened_T)
                encrypted_row.append(cipher_text)
                
            writer.writerow(encrypted_row)

# Read the key from file
def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        key = [int(num) for num in file.read().split()]
    return key

# Example usage:
input_csv_file = sys.argv[1]
output_csv_file = 'encrypted_data.csv'
key_file_path = 'key.txt'

K = read_key_from_file(key_file_path)

encrypt_csv(input_csv_file, output_csv_file)
print("Encryption completed!")
