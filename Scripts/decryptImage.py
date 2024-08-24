import cv2
import numpy as np
import os
import csv

# Save Grayscale Image to CSV
def save_image_to_csv(image_matrix, csv_filename):
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in image_matrix:
            writer.writerow(row)

# Example Usage
image_path = 'encrypted_image.png'
csv_filename = 'encrypted_image_matrix.csv'

# Read the grayscale image
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Save the grayscale image matrix to CSV
save_image_to_csv(image_gray, csv_filename)
