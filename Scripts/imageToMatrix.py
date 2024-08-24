import cv2
import numpy as np
import os
import csv
import sys

# Check if the image path is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python imageToMatrix.py <image_path>")
    sys.exit(1)

# Load the image as grayscale
image_path = sys.argv[1]
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert the image to a matrix
matrix = np.array(image)

# Save the matrix as a CSV file
matrix_file_path = os.path.join(os.path.dirname(__file__), 'matrix.csv')
with open(matrix_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(matrix)

# Display the original image 
#cv2.imshow('Original Image', image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Print the matrix shape
print("Matrix shape:", matrix.shape)
