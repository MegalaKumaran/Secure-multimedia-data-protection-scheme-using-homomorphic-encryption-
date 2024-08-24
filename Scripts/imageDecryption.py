import csv

def convert_to_binary(t):
    binary_matrix = []
    for val in t:
        binary_value = bin(int(val))[2:].zfill(8)
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

def binary_to_decimal(binary_list):
    # Convert binary list back to a decimal number
    decimal_number = int(''.join(map(str, binary_list)), 2)
    return decimal_number

def decrypt_csv(input_file, output_file, key):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            decrypted_row = []
            chunk_size = 8
            for i in range(0, len(row), chunk_size):
                chunk = row[i:i+chunk_size]
                binary_matrix = convert_to_binary(chunk)
                
                for i in range(0, len(K), 4):
                     if K[i] % 2 == 0:
                       M1 = rotate_shift_down(binary_matrix, K[i+1])
                     else:
                       M1 = rotate_shift_up(binary_matrix, K[i+1])

                     if K[i+2] % 2 == 0:
                       M2 = rotate_shift_right(M1, K[i+3])
                     else:
                       M2 = rotate_shift_left(M1, K[i+3])
                 
                for m_row in M2:
                    binary_m_row = m_row
                    decimal_number = binary_to_decimal(binary_m_row)
                    decrypted_row.append(decimal_number)

            writer.writerow(decrypted_row)

# Read the key from file
def read_key_from_file(file_path):
    with open(file_path, 'r') as file:
        key = [int(num) for num in file.read().split()]
    return key

# Example usage:
input_csv_file = 'encrypted_image_matrix.csv'
output_csv_file = 'decrypted_data.csv'
key_file_path = 'unique_numbers.txt'

K = read_key_from_file(key_file_path)
        
decrypt_csv(input_csv_file, output_csv_file, K)
print("Decryption completed!")