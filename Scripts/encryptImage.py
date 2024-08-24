import cv2
import numpy as np
import os
import csv

# Load Grayscale Image from CSV
def load_image_from_csv(csv_filename):
    with open(csv_filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        image_data = list(reader)
    image_matrix = np.array(image_data, dtype=np.uint8)
    return image_matrix

# Example Usage
csv_filename = 'encrypted_data.csv'

# Load the grayscale image from CSV
reconstructed_image = load_image_from_csv(csv_filename)

# Save the directory of the script
script_dir = os.path.dirname(__file__)

# Specify the filename for the restored image
reconstructed_image_path = os.path.join(script_dir, 'encrypted_image.png')

# Save the restored grayscale image as JPG
cv2.imwrite(reconstructed_image_path, reconstructed_image)

