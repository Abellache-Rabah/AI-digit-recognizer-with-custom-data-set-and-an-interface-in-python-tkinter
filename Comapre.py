import numpy as np 
import json
from scipy.spatial.distance import cdist  

# Load dataset 
with open('data.json') as f:
    dataset = json.load(f)

# Extract training vectors
train_vectors = np.array([sample['vector'] for sample in dataset])
train_labels = np.array([sample['label'] for sample in dataset])

# New input vector
new_vector = [34, 15, 19, 27, 11, 24, 22, 20, 20, 49, 0, 0, 0, 0, 36, 0, 0, 0, 29, 9, 17, 23, 25, 9, 0]

# Compute distance to all training vectors
distances = cdist([new_vector], train_vectors)[0]

# Find index of nearest neighbor 
nearest_idx = np.argmin(distances)

# Look up label 
nearest_label = train_labels[nearest_idx] 
print("Nearest match label:", nearest_label)