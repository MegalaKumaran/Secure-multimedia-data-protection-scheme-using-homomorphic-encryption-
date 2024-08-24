import csv
import os
import random

# Initialize a cryptographic RNG
crypto_rng = random.SystemRandom()

# Read the CSV file and choose a random line
def get_random_line_from_csv(filename):
    with open(filename, 'r') as file:
        lines = list(csv.reader(file))
        random_line = crypto_rng.choice(lines)  # Using cryptographic RNG
        return random_line[0]

# Function to remove repeated letters and spaces
def remove_repeated_characters(line):
    unique_chars = []
    for char in line:
        if char not in unique_chars and char != ' ':
            unique_chars.append(char)
    return ''.join(unique_chars)

# Function to convert characters to ASCII and perform modulus operation
def convert_to_ascii_and_modulo(line):
    ascii_modulo = [ord(char) % 10 for char in line]
    return ascii_modulo

# Write numbers to a text file
def write_to_text_file(numbers, filename):
    with open(filename, 'w') as file:
        for num in numbers:
            file.write(str(num) + ' ')

# Generate random numbers below 10 to make the count of numbers a multiple of four
def generate_random_numbers(total_count, filename):
    count_to_generate = 4 - (total_count % 4)
    with open(filename, 'a') as file:
        for _ in range(count_to_generate):
            random_num = crypto_rng.randint(0, 9)  # Using cryptographic RNG
            file.write(str(random_num) + ' ')

# Main function
def main():
    # Change the filename to your CSV file
    filename = 'datasetSample.csv'
    
    # Get a random line from the CSV file
    random_line = get_random_line_from_csv(filename)
    
    # Remove repeated characters and spaces
    modified_line = remove_repeated_characters(random_line)
    
    # Convert characters to ASCII and perform modulus operation
    ascii_modulo_numbers = convert_to_ascii_and_modulo(modified_line)
    
    # Write numbers to a text file
    output_filename = 'key.txt'
    write_to_text_file(ascii_modulo_numbers, output_filename)
    
    # Count the number of values in the output file
    with open(output_filename, 'r') as file:
        count = len(file.read().split())
    
    # If count is not a multiple of four, generate random numbers below 10
    if count % 4 != 0:
        generate_random_numbers(count, output_filename)
    
    print("Output written to", output_filename)

if __name__ == "__main__":
    main()
