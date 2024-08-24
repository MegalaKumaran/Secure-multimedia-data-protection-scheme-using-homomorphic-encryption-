import csv

def compare_csv_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        reader1 = csv.reader(f1)
        reader2 = csv.reader(f2)
        
        # Iterate through rows in both files
        for row1, row2 in zip(reader1, reader2):
            # Compare length of rows
            if len(row1) != len(row2):
                print("Number of columns in rows are different.")
                return False
            
            # Compare values in each row
            for val1, val2 in zip(row1, row2):
                if val1 != val2:
                    print(f"Values '{val1}' and '{val2}' are different.")
                    return False
        
        # Check if both files have the same number of rows
        try:
            next(reader1)
            print("File 1 has more rows than File 2.")
            return False
        except StopIteration:
            pass  # File 1 ended

        try:
            next(reader2)
            print("File 2 has more rows than File 1.")
            return False
        except StopIteration:
            pass  # File 2 ended
        
        print("Both CSV files are equal.")
        return True

# Example usage:
file1 = 'decrypted_data.csv'
file2 = 'matrix.csv'
compare_csv_files(file1, file2)