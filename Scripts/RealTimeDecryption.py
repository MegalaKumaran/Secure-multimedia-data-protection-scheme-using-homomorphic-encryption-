import csv

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

def decrypt_csv(input_file, output_file, K):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            decrypted_row = []
            for cell in row:
                decrypted_text = decrypt(cell, K)
                decrypted_row.append(decrypted_text)
            writer.writerow(decrypted_row)

def decrypt(ciphertext, K):
    T = decode_text(ciphertext)
    q = len(T) // 8
    MT = []
    for i in range(8):
        row = T[i * q:(i + 1) * q]
        MT.append(row)
    
    transposed_matrix = transpose_matrix(MT)

    for i in range(0, len(K), 4):
        if K[i] % 2 == 0:
            M1 = rotate_shift_down(transposed_matrix, K[i+1])
        else:
            M1 = rotate_shift_up(transposed_matrix, K[i+1])
        if K[i+2] % 2 == 0:
            M2 = rotate_shift_right(M1, K[i+3])
        else:
            M2 = rotate_shift_left(M1, K[i+3])
    
    flattened_matrix = flatten_matrix(M2)
    
    P = ""
    for i in range(0, len(flattened_matrix), 8):
        binary_str = ''.join(map(str, flattened_matrix[i:i+8]))
        decimal_value = int(binary_str, 2)
        P += chr(decimal_value)
    
    return P

# Read the key from file
def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        key = [int(num) for num in file.read().split()]
    return key

# Example usage:
input_csv_file = 'encrypted_data.csv'
output_csv_file = 'decrypted_data.csv'
key_file_path = 'key.txt'

K = read_key_from_file(key_file_path)
decrypt_csv(input_csv_file, output_csv_file, K)
print("Decryption completed!")