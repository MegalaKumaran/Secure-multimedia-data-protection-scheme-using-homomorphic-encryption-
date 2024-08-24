import cv2
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
import os
from collections import Counter
import sys

# Load the ResNet50 model
resnet_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

def encrypt_image(image_path):
    # Step 1: Preprocess the image (Convert to grayscale)
    original_image = cv2.imread(image_path)
    #gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Extract features using ResNet50
    original_image_resized = cv2.resize(original_image, (224, 224))
    original_image_resized = np.expand_dims(original_image_resized, axis=0)
    original_image_resized = preprocess_input(original_image_resized)
    features = resnet_model.predict(original_image_resized)

    # Convert features to integer type
    features = features.astype(int)

    # Dummy encryption: Return features as they are
    return features

# Check if the image path is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python featureExtraction.py <image_path>")
    sys.exit(1)

image_path = sys.argv[1]
key_features = encrypt_image(image_path)

flattened_key_features = key_features.flatten()

# Count the occurrences of unique numbers
unique_numbers_count = Counter(flattened_key_features)

key = []
for number, count in unique_numbers_count.items():
    key.append(number)

while len(key) % 4 != 0:
    random_number = np.random.randint(20)
    if random_number not in key:
        key.append(random_number)

# Save the unique numbers to an output file as a list
output_file = 'unique_numbers.txt'
with open(output_file, 'w') as f:
    f.write(' '.join(map(str, key)))

print(f"Unique numbers saved to {output_file}")
