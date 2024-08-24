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
csv_filename = 'decrypted_data.csv'

# Load the grayscale image from CSV
restored_image = load_image_from_csv(csv_filename)

# Save the directory of the script
script_dir = os.path.dirname(__file__)

# Specify the filename for the restored image
restored_image_path = os.path.join(script_dir, 'restored_image.png')

# Save the restored grayscale image as JPG
cv2.imwrite(restored_image_path, restored_image)

# Display the reconstructed image
#cv2.imshow('Restored Image', restored_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()